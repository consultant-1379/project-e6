from datetime import datetime


def fix_date_time(df,dt_column):
    # empty column
    df['Date'] = None

    # iterate over all rows
    for i,r in df.iterrows():
        r['Date'] = datetime.strptime(r[dt_column], '%Y-%m-%dT%H:%M:%S.%fZ')

    # drop original column
    df.drop([dt_column], axis=1, inplace=True)

    return df
