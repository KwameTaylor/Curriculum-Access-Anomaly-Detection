import numpy as np
import pandas as pd

def acquire_access_logs(df):
    colnames = ['date', 'timestamp', 'request_method', 'user_id', 'cohort_id', 'ip']

    df = pd.read_csv('anonymized-curriculum-access.txt', header=None, index_col=False,
                    names=colnames, delim_whitespace=True, na_values='"-"')

    return df