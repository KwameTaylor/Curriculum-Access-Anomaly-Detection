import numpy as np
import pandas as pd

def add_network_and_host(df):
    '''
    This function takes in a DataFrame and returns a DataFrame with
    two features added: Network and Host, which are derived from IP address.
    '''
    df[['network1','network2', 'host1', 'host2']] = df.ip.str.split(".",expand=True)
    
    df['network'] = df['network1'] + df['network2']
    df['host'] = df['host1'] + df['host2']

    df = df.drop(columns=['network1', 'network2', 'host1', 'host2'])

    return df

