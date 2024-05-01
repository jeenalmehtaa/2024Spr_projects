import pandas as pd


def read_education_data(filename):
    """
    reads education_data
    :param filename: path to the dataset
    :return: a dataframe education_data
    """

    df_education = pd.read_csv(filename)
    return df_education


def clean_education_data(df_education):
    """
    cleans df_education dataframe
    > checks for missing values
    > deletes rows with missing values
    > extracts only the necessary columns for analysis
    :param df_education: a dataframe of education data
    :return: a cleaned dataframe
    """

    df_education.isna().sum()
    df_education = df_education.dropna(axis=0)
    df_education = df_education[["County", "All Students"]]
    df_education.rename(columns={"All Students": "Number of Students"}, inplace=True)
    return df_education


filename = "/Users/peeyu/PycharmProjects/2024Spr_projects/datasets/education_data.csv"
read_education_data(filename)
