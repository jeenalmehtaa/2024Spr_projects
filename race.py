import pandas as pd
import matplotlib.pyplot as plt


def clean_ev_data(ev_file):
    """
    Clean EV data by dropping NaN values and filtering by state.

    :param ev_file: Path to the EV data CSV file
    :return: Cleaned EV data DataFrame
    """
    df = pd.read_csv(ev_file)
    df_cleaned = df[
        ["Date", "County", "State", "Electric Vehicle (EV) Total", "Non-Electric Vehicle Total", "Total Vehicles"]]
    df_cleaned = df_cleaned.dropna(axis=0)
    df_cleaned["Year"] = pd.to_datetime(df_cleaned["Date"]).dt.year
    df_cleaned = df_cleaned.where(df_cleaned["State"] == 'WA').dropna(axis=0)
    df_cleaned["Proportion"] = (df_cleaned['Electric Vehicle (EV) Total'] / df_cleaned['Total Vehicles']) * 100
    df_cleaned.reset_index(drop=True, inplace=True)
    return df_cleaned


def merge_ev_race(ev_df, race_file):
    """
    Merge EV data with race data by county.

    :param ev_df: Cleaned EV data DataFrame
    :param race_file: Path to the race data CSV file
    :return: Merged DataFrame containing EV and race data
    """
    df_race = pd.read_csv(race_file)
    df_race_cleaned = df_race[
        ['County', 'All Students', 'American Indian/ Alaskan Native', 'Asian', 'Black/ African American',
         'Hispanic/ Latino of any race(s)', 'Native Hawaiian/ Other Pacific Islander', 'Two or More Races', 'White']]
    df_race_grouped = df_race_cleaned.groupby(['County']).sum()
    df_cleaned_2023 = ev_df[ev_df['Year'] == 2023]
    merged_data = pd.merge(df_cleaned_2023, df_race_cleaned, on='County')
    return merged_data


def plot_ev_proportion(merged_data):
    """
    Plot the average proportion of electric vehicles by county in 2023.

    :param merged_data: Merged DataFrame containing EV and race data
    :return: Visualization
    """
    average_ev_proportion = merged_data.groupby('County')['Proportion'].mean()
    average_ev_proportion.plot(kind='bar', figsize=(12, 6), color='skyblue')
    plt.title('Average Proportion of Electric Vehicles by County in 2023')
    plt.xlabel('County')
    plt.ylabel('Average Proportion of Electric Vehicles')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_race_sum(merged_data):
    """
    Plot the sum of race columns by county.

    :param merged_data: Merged DataFrame containing EV and race data
    :return: Visualization
    """
    race_columns = ['County', 'American Indian/ Alaskan Native', 'Asian', 'Black/ African American',
                    'Hispanic/ Latino of any race(s)', 'Native Hawaiian/ Other Pacific Islander',
                    'Two or More Races', 'White']
    race_data = merged_data[race_columns]
    race_data_final = race_data.groupby('County').sum().reset_index()
    race_data_final.plot(kind="bar", figsize=(12, 6), stacked=True)
    plt.xlabel('County')
    plt.ylabel('Sum')
    plt.title('Sum of Other Columns by County')
    plt.show()

