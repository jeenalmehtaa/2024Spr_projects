import pandas as pd


def read_county_data(filename):
    """
    reads ev_by_county dataset
    :param filename: path to the dataset
    :return: a dataframe of ev_by_county dataset
    """

    df_county = pd.read_csv(filename)
    return df_county


def clean_county_data(ev_by_county):
    """
    cleans ev_by_county dataframe
    > checks for missing values
    > deletes rows with missing values
    > extracts only the necessary columns for analysis
    > extracts year from date column
    > extracts only WA state data
    :param ev_by_county: a dataframe of ev_by_county dataset
    :return: a cleaned dataframe
    """

    ev_by_county.isna().sum()
    ev_by_county = ev_by_county.dropna(axis=0)
    ev_by_county = ev_by_county[["Date", "County", "State", "Electric Vehicle (EV) Total", "Non-Electric Vehicle Total",
                                 "Total Vehicles"]]
    ev_by_county["Date"] = pd.to_datetime(ev_by_county["Date"]).dt.year
    ev_by_county.rename(columns={"Date": "Year"}, inplace=True)
    ev_by_county = ev_by_county[ev_by_county["State"] == 'WA']
    ev_by_county.reset_index(drop=True, inplace=True)
    return ev_by_county


def calc_proportion(ev_by_county):
    """
    calculates and inserts a new column called proportion of EVs
    :param ev_by_county: cleaned dataframe
    :return: final dataframe for analysis
    """

    ev_by_county["Proportion"] = (ev_by_county['Electric Vehicle (EV) Total'] / ev_by_county['Total Vehicles'])*100
    return ev_by_county


