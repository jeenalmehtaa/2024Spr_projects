# IS597PR Spring 2024
## Electric Vehicle Adoption Analysis: Insights from Washington State
### By

- Jeenal Mehta
- Peeya Thacker

### Absract

Our project seeks to analyze electric vehicle (EV) data obtained from the official US government website, with a particular emphasis on data sourced from the State of Washington. Our primary objectives include examining the geographical distribution of EVs, identifying the most prominent car brands in the EV market, and pinpointing the cities where EV adoption is most prevalent.

Furthermore, we aim to explore correlations between EV adoption rates and various socio-economic factors such as population density, educational attainment, and employment rates.

By investigating these hypotheses, we hope to gain insights into the factors influencing EV popularity and the potential interplay between EV adoption and demographic trends.

### Hypotheses

1. Counties in WA State with higher average population density tend to exhibit higher electric vehicle adoption rates.
2. In counties where there is a higher average number of students, indicative of greater educational attainment, there will be a corresponding increase in the proportion of electric vehicle (EV) adoption.
3. Counties with higher average incomes are more likely to have a higher proportion of electric vehicles (EVs) than counties with lower average incomes.
4. Demographics belonging to "Hispanic/Latino" racial group have bought more EVs than other racial groups across all counties. 

### References

- States With Most Electric Vehicles: https://www.usnews.com/news/best-states/articles/2022-08-19/states-with-the-most-electric-vehicles
- Electric Vehicle Population Size History By County: https://catalog.data.gov/dataset/electric-vehicle-population-size-history-by-county
- Report Card Enrollment: https://catalog.data.gov/dataset/report-card-enrollment-2023-24-school-year
- Population Density By County: https://catalog.data.gov/dataset/waofm-april-1-population-density-by-county-2000-to-present
- Office of Financial Management, Washington: https://ofm.wa.gov/washington-data-research/statewide-data/washington-trends/economic-trends/washington-and-us-average-wages/average-wages-county-map
- Bureau of Economic Analysis, Regional Economic Accounts - https://apps.bea.gov/regional/downloadzip.htm?_gl=1*1dgd84*_ga*NjEyNDAzMTQ3LjE3MTQ1Mzc1ODA.*_ga_J4698JNNFT*MTcxNDU0MTA5Ni4yLjEuMTcxNDU0MTExNi40MC4wLjA
- ChatGPT: https://chat.openai.com/
- Claude AI: https://claude.ai/chats

### Execution of project
All datasets used in this project are stored in a folder. Code for data pre-processing performing is saved in the python module named _county.py_. Additionally, code for each hypothesis is stored in individual python modules corresponding to the topic of the hypothesis. For example, Hypothesis 3 refers to _income.py_ for its execution.
