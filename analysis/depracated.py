# functions that are no longer used


def split_by_year(df):
    list_ = df['Date'].dt.year.unique()
    dict_ = {}
    for year in list_:
        temp = df[df['Date'].dt.year == year]
        dict_.update({str(year): temp})
    return dict_


def split_by_month(df):
    list_ = df['Date'].dt.month.unique()
    dict_ = {}
    for month in list_:
        temp = df[df['Date'].dt.month == month]
        dict_.update({str(month): temp})
    return dict_


def split_by_day(df):
    list_ = df['Date'].dt.day.unique()
    dict_ = {}
    for day in list_:
        temp = df[df['Date'].dt.day == day]
        temp['Date'] = temp['Date'].dt.strftime('%H:%M:%S%f')
        dict_.update({str(day): temp})
    return dict_


def split_by_date(df):
    dict = split_by_year(df)
    for k, v in dict.items():
        v = split_by_month(v)
        for i, j in v.items():
            v.update({i: split_by_day(j)})
        dict.update({k: v})
    return dict


# STEP 5!
def tree_add_date_branches(dict_tree):
    for k, v in dict_tree.items():
        for i, j in v.items():
            j = split_by_date(j)
            v.update({i: j})
        dict_tree.update({k: v})
    return dict_tree