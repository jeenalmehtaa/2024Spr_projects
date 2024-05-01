import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def clean_income_data(income_file):
    """
    Clean income data by dropping NaN values and filtering by LineCode

    :param income_file: Path to the income data CSV file
    :return: Cleaned income data DataFrame
    """
    df_income = pd.read_csv(income_file)
    df_income = df_income.dropna(axis=0)
    df_income['County'] = df_income['GeoName'].str.split(',').str[0]
    df_inc_filtered = df_income[df_income['LineCode'] == 3]
    df_inc_filtered['average_income'] = df_inc_filtered.loc[:, '1969':'2022'].mean(axis=1)
    df_inc_filtered = df_inc_filtered[['County', 'average_income']]
    return df_inc_filtered


def merge_income_ev(income_df, ev_df):
    """
    Merge income data with EV data by county

    :param income_df: Cleaned income data DataFrame
    :param ev_df: Cleaned EV data DataFrame
    :return: Merged DataFrame containing income and EV data
    """
    df_inc_merged = pd.merge(income_df, ev_df, on='County')
    df_inc_merged = df_inc_merged.groupby('County').mean()
    return df_inc_merged


def plot_income_ev(df_inc_merged):
    """
    Plot the relationship between average income and proportion of electric vehicles by county.

    :param df_inc_merged: Merged DataFrame containing income and EV data.
    :return: Visualization
    """
    counties = df_inc_merged.index
    average_income = df_inc_merged['average_income']
    proportion = df_inc_merged['Proportion']

    plt.figure(figsize=(15, 8))
    plt.scatter(average_income, proportion, color='blue', alpha=0.5)
    plt.title('Average Income vs Proportion of Electric Vehicles by County')
    plt.xlabel('Average Income')
    plt.ylabel('Proportion of Electric Vehicles')
    plt.grid(True)

    for i, county in enumerate(counties):
        plt.text(average_income[i], proportion[i], county)

    plt.show()


def plot_income_ev_trendline(df_inc_merged):
    """
    Plot the relationship between average income and proportion of electric vehicles by county with a trend line.

    :param df_inc_merged: Merged DataFrame containing income and EV data.
    :return: Visualization
    """
    counties = df_inc_merged.index
    average_income = df_inc_merged['average_income']
    proportion = df_inc_merged['Proportion']

    slope, intercept = np.polyfit(average_income, proportion, 1)
    trendline_x = np.array([min(average_income), max(average_income)])
    trendline_y = slope * trendline_x + intercept

    plt.figure(figsize=(12, 8))
    plt.scatter(average_income, proportion, color='blue', alpha=0.5, label='Data')
    plt.plot(trendline_x, trendline_y, color='red', linestyle='--', label='Trend Line')

    plt.title('Average Income vs Proportion of Electric Vehicles by County')
    plt.xlabel('Average Income')
    plt.ylabel('Proportion of Electric Vehicles')
    plt.grid(True)
    plt.legend()

    for i, county in enumerate(counties):
        plt.text(average_income[i], proportion[i], county)

    plt.show()



