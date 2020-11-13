import numpy as np
import pandas as pd

# importing GeoIP database for IP geolocation
import geoip2.database
reader = geoip2.database.Reader('GeoLite2City/GeoLite2-City.mmdb')

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

def add_city(ip):
    try:
        response = reader.city(ip)
        city_name = response.city.name
        return city_name
    except:
        return np.nan

def add_country(ip):
    try:
        response = reader.city(ip)
        country_name = response.country.name
        return country_name
    except:
        return np.nan