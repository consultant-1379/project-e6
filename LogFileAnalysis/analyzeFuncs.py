def log_count_total(df):
    '''

    :param df: input dataframe, requires Date column with DateTime type
    :return: dictionary with k:v = 'yyy-MM-dd hh-mm-ss':count
    '''
    df1 = df.set_index('Date')
    df1 = df1.resample('1min').size().to_frame(name='Count')
    df1.index = df1.index.astype(str)
    return df1.to_dict()['Count']


def log_count_errors(df):
    trigger_words = ['(err)','[err]','(error)','[error]']
    df1 = df[df[4].str.contains('|'.join(trigger_words), case = False)]
    df1['Date'] = df1['Date'].astype(str)
    df1 = df1.set_index('Date')
    x,y = df1.shape
    return x