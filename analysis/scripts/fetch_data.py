import numpy as np
import pandas as pd


def braun():
    # read column headings
    with open('/Users/stewarta/repos/iot-htsensor/data/columns.txt') as f:
        cols = f.readlines()
    cols = [ln.strip() for ln in cols]

    # read data from file: parse the date after reading, just as a sanity check
    home = pd.read_csv('/Users/stewarta/Documents/DATA/htsensor/raw.data', sep=';', decimal=',', names=cols)

    # select relevant columns
    home = home[['timestamp', 'Temp1', 'Temp2', 'Temp3', 'Temp4', 'Temp8', 'Humi1', 'Humi2', 'Humi3', 'Humi4']]

    # parse date and insert as new column
    home.insert(1, 'datetime',
                pd.to_datetime(home.timestamp, errors='coerce'))  # If ‘coerce’, then invalid parsing will be set as NaT

    # set index
    home.set_index('datetime', inplace=True)

    home.drop(columns='timestamp', inplace=True)

    return home


def dwd(start, end, url):
    '''
    Retrieves temperature and Humidy reading from Deutsch Wetter Dienst (DWD)
    :param start: first start
    :param end: last year
    :return: dataframe  humidity and temperature observations
    '''

    # parse the DWD dataset and convert date and align with home readings
    # Format dwd: yyyymmddhh
    df = pd.read_csv(url, sep=';')
    # select relevant columns
    df = df[['MESS_DATUM', 'TT_TU', 'RF_TU']]
    # rename
    df.rename(columns={'TT_TU': 'Temp', 'RF_TU': 'Humi'}, inplace=True)

    # parse date
    df.insert(2, 'datetime', pd.to_datetime(df['MESS_DATUM'], errors='coerce', format='%Y%m%d%H'))

    # humidity can not be less than 0
    outliers = df[df.Humi < 0].index
    df.drop(outliers, axis=0, inplace=True)
    df.dropna(axis=0, inplace=True)

    # fill in missing values
    df[['Temp', 'Humi']] = df[['Temp', 'Humi']].fillna(df.mean())

    # something is not working with fillna
    df.dropna(axis=0, inplace=True)

    # create index
    df.set_index('datetime', inplace=True)
    df.drop('MESS_DATUM', axis=1, inplace=True)

    # filter years
    filter = (df.index.year >= start) & (df.index.year <= end)

    # filter columns
    df = df.loc[filter, ['Temp', 'Humi']]

    df.head()
    return df
