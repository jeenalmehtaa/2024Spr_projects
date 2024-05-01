import pandas as pd


def read_population_data(filename):
    """
    reads population data from population_data.csv
    :param filename: path to dataset
    :return: population dataframe
    """

    df_pop = pd.read_csv(filename)
    return df_pop


def calculate_average_population_density(df_pop):
    """
    calculates the average total population density for each county
    :param df_pop: DataFrame containing the population data
    returns: dataframe with the average total population density for each county
    """

    df_pop['Total_Population_Density'] = df_pop.drop('COUNTY_NAME', axis=1).sum(axis=1)
    df_pop['Total_Population_Density'] = df_pop['Total_Population_Density'] / 23
    df_pop = df_pop.rename(
        columns={"Total_Population_Density": "Avg_Total_Population_Density", "COUNTY_NAME": "County"})
    df_pop_cleaned = df_pop[["County", "Avg_Total_Population_Density"]]
    return df_pop_cleaned


population_filename = "/Users/peeyu/PycharmProjects/2024Spr_projects/datasets/population_data.csv"
population_data = read_population_data(population_filename)
average_population_density = calculate_average_population_density(population_data)
print(average_population_density)
