def df_to_dict(df, col):
    '''
    :param df: input dataframe
    :param col: column you want to sort by
    :return: dictionary, keys are unique values from col, values are dataframes where df[col] == key
    '''

    dictk = {}

    for k in df[col].unique():
        dictk.update({k: df[df[col] == k].drop([col], axis=1, inplace=False)})

    return dictk


def dict_to_dict_of_dit(dict_dfs, col):
    '''
    :param dict_dfs: dictionary of dataframes (output from df_to_dict)
    :param col: column to sort by
    :return: dictionary from input with value replaced by dictionary of k:v pairs of unique-values-from-col:df[[col] == key]
    '''

    temp_dict = {}

    for k, v in dict_dfs.items():
        temp_dict.clear

        for i in v[col].unique():
            temp_dict.update({i: v[v[col] == i].drop([col], axis=1, inplace=False)})

        dict_dfs.update({k: temp_dict})

    return dict_dfs
