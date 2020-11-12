import numpy as np
import pandas as pd

def acquire_access_logs():
    '''
    This function returns a DataFrame with access logs for the Codeup Curriculum website.
    '''
    colnames = ['date', 'timestamp', 'request_method', 'user_id', 'cohort_id', 'ip']

    df = pd.read_csv('anonymized-curriculum-access.txt', header=None, index_col=False,
                    names=colnames, delim_whitespace=True, na_values='"-"')

    return df

def prepare_logs(df):
    '''
    This function takes in a DataFrame and returns a DataFrame that is prepared for preprocessing and exploration.
    '''
    # merge date and timestamp
    df["ds"] = df["date"] +" "+ df["timestamp"]

    # drop date and timestamp
    df = df.drop(columns=['date', 'timestamp'])

    # convert date column to datetime type
    df.ds = pd.to_datetime(df.ds)

    # set ds as index and sort
    # this is a very important step!
    df = df.set_index('ds').sort_index()

    # Some IP addresses accidentally got put in the
    # cohort_id column, so I'm going to drop those rows.
    df = df.drop(df[df.cohort_id.str.len() > 4].index)

    # drop request methods that don't have a page,
    # i.e. accessing the domain/main page
    df = df.drop(df[df.request_method.str.len() < 2].index)

    return df