import os
import pandas as pd
from datetime import datetime


def make_readable(file):
    # step 1 clean up the configs
    deal_with_configs(file)

    # step 2 deal with extra @'s
    deal_with_delimeters(file)


def deal_with_configs(file):
    # open the temp file to which the update lines will be written to
    original = open(file, 'r')
    temp = open("temp.csv", 'w')

    line = original.readline()
    while line != "":

        if "@" in line:
            temp.write("\n" + line.replace('\n', ''))
        else:
            temp.write(line.replace('\n', ''))
        line = original.readline()

    original.close()  # close the unstructure file
    temp.close()  # close the temp file containing new structure


# deal with the delimeters
def deal_with_delimeters(file):
    # open the temp file to which the update lines will be written to
    temp = open("temp.csv", 'r')
    name = file[:-4] + '_r' + file[-4:]
    output = open(name, 'w')

    line = temp.readline()
    while line != "":

        if line.count('@') == 3:

            # print(line, end="")
            output.write(line.replace('\n', '') + "@NaN" + "\n")
        else:
            output.write(line.replace('\n', '') + "\n")
        line = temp.readline()

    temp.close()           # close the temp file
    output.close()         # close the now structured file
    #os.remove(file)        # remove original
    os.remove("temp.csv")  # remove temp


# STEP 1! (no return)
def make_all_readable(dir):

    if dir[-1] != '/':  # add trailing / if not present
        dir += '/'

    files = os.listdir(dir)     # get list of files in directory

    for file in files:
        make_readable(dir+file)     # run function on each individual file


# STEP 2! (return DF)
def import_dataframes(dir):

    if dir[-1] != '/':  # add trailing / if not present
        dir += '/'

    temp_list = []      # temp list to store dataframes

    files = os.listdir(dir)     # get list of files in directory

    for file in files:
        if file[-6:-4] == '_r':
            temp_list.append(pd.read_csv(dir+file, index_col=None, header=None, sep="@"))       # read in each csv
    df = pd.concat(temp_list, axis=0, ignore_index=True)
    return df # .head(1000)  # return df, number of rows specified in head(). comment out for full DF


# STEP 3! Fix datetime
def fix_date_time(df):

    df['Date'] = pd.to_datetime(df[0], format = '%Y-%m-%dT%H:%M:%S.%fZ', dayfirst=True)
    return df


def df_to_dict(df, col):
    dictK = {}
    for k in df[col].unique():
        dictK.update({k: df[df[col] == k].drop([col], axis=1, inplace=False).reset_index(inplace=False) })
    return dictK


# STEP 4! Turn DF into a tree structure -> {app_n : {instance_n : DF, ...}, ...}
def df_to_tree(df):
    test = df_to_dict(df, 2)
    for k, v in test.items():
        test.update({k: df_to_dict(v, 1)})
    return test


# STEP 5! Split by date!
def tree_add_date_branches(dict_tree):
    for k,v in dict_tree.items():
        for i,j in v.items():
            j = split_by_date_dmy(j)
            v.update({i:j})
        dict_tree.update({k:v})
    return dict_tree


def split_by_date_dmy(df):
    list_ = df['Date'].dt.strftime('%d-%m-%Y').unique()
    dict_ = {}
    for date in list_:
        temp = df[df['Date'].dt.strftime('%d-%m-%Y') == date]
        #temp['Date'] = temp['Date'].dt.strftime('%H:%M:%S.%f')
        dict_.update({date : temp})
    return dict_


def log_dupes(df):
    dict_metrics = {'df': df.drop_duplicates(), 'Duplicates': str(df.duplicated().sum())}
    return dict_metrics


def log_missing_msg(dict_metrics):
    # input: [df,duplicates(int)]
    df = dict_metrics.get('df')
    missing = df[3].isnull().sum()
    dict_metrics.update({'df': df.dropna(subset=[3]), 'Missing_Msg': str(missing)})
    return dict_metrics


def log_total_logs(dict_metrics):
    # input list: [df,duplicates(int),missing_msg(int)]
    df = dict_metrics.get('df')
    x, y = df.shape
    dict_metrics.update({'Total_Logs': str(x)})
    return dict_metrics


def log_total_error(dict_metrics):
    # input list: [df,duplicates(int),missing_msg(int),total_msg(int)]
    df = dict_metrics.get('df')
    df = df.dropna()
    x, y = df.shape
    dict_metrics.update({'Total_Errors': str(x)})
    return dict_metrics


def log_total_error_by_severity(dict_metrics):
    # input list: [df,duplicates(int),missing_msg(int),total_msg(int),total_errors(int)]
    df = dict_metrics.get('df')
    df = df.dropna()
    trigger_words_warning = ['(warning)', '[warning]']
    trigger_words_info = ['(info)', '[info]']

    temp = df[df[4].str.contains('(WARNING)', case=True)]
    x_warn, y_warn = temp.shape

    temp = df[df[4].str.contains('(INFO)', case=True)]
    x_info, y_info = temp.shape

    dict_metrics.update({'Total_Warning': str(x_warn), 'Total_Info': str(x_info)})

    return dict_metrics


def log_logs_and_errors_per_min(dict_metrics):
    # input list: [df,duplicates(int),missing_msg(int),total_msg(int),total_errors(int),
    # total_info_errors(int),total_warning_errors(int)]

    df = dict_metrics.get('df')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%H:%M:%S')
    df['Date'] = pd.to_datetime(df['Date'])
    df_grouped = df.resample('1min', on='Date').count()

    logs_per_min = dict(zip(df_grouped.index.astype(str).str[11:], df_grouped[3].astype(str)))
    errors_per_min = dict(zip(df_grouped.index.astype(str).str[11:], df_grouped[4].astype(str)))
    dict_metrics.update({'Logs_Per_Min': logs_per_min, 'errors_Per_Min': errors_per_min})

    return dict_metrics


def df_analysis(df):
    # call previous functions

    dict_metrics = log_dupes(df)
    dict_metrics = log_missing_msg(dict_metrics)
    dict_metrics = log_total_logs(dict_metrics)
    dict_metrics = log_total_error(dict_metrics)
    dict_metrics = log_total_error_by_severity(dict_metrics)
    dict_metrics = log_logs_and_errors_per_min(dict_metrics)
    # del dict_metrics['df']
    return dict_metrics


# STEP 6! analyze all sub-branches. just push to DB after this!
def analyze_logs(dict_):
    for k, v in dict_.items():

        for i, j in v.items():

            for x, y in j.items():
                tempp = df_analysis(y)
                del tempp['df']

                j.update({x: tempp})

            v.update({i: j})

        dict_.update({k: v})
    return dict_


def export_dict(inp):
    return dict({'_id' : 'LMI_KOHN017', 'data' : inp})


def remove_files(dir):
    if dir[-1] != '/':  # add trailing / if not present
        dir += '/'

    files = os.listdir(dir)

    for file in files:
        if file[-6:-4] == '_r':
            os.remove(dir+file)