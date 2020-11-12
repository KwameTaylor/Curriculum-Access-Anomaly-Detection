import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# default viz size settings
plt.rc('figure', figsize=(14, 9))
plt.rc('font', size=15)

# This is to make sure matplotlib doesn't throw the following error:
# The next line fixes "TypeError: float() argument must be a string or a number, not 'Timestamp' matplotlib"
pd.plotting.register_matplotlib_converters()

def plot_top_cities(df):
    city_plot_df = df.groupby('city').filter(lambda x : len(x)>900)
    city_plot_df['city'].value_counts().plot(kind='bar')
    plt.title('In what cities was the curriculum accessed the most?')
    plt.show()

    city_plot_df['city'].drop(city_plot_df[city_plot_df.city == 'San Antonio'].index).value_counts().plot(kind='bar')
    plt.title('Top cities - without San Antonio')
    plt.show()

def plot_city_anomalies(df):
    city_plot_anomalies = df.groupby('city').filter(lambda x : len(x)<4)
    city_plot_anomalies['city'].value_counts().plot(kind='bar')
    plt.title('In what cities was the curriculum accessed the least?')
    plt.show()

def plot_top_countries(df):
    country_plot_df = df.groupby('country')
    country_plot_df['country'].value_counts().plot(kind='bar')
    plt.title('In what countries was the curriculum accessed the most?')
    plt.show()

