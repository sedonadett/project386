# project386
Data is From Pro-Football-Reference.com, Accessed 11/15/2024

https://www.pro-football-reference.com/

Sphinx Documentation:
https://sedonadett.github.io/project386/ 

Streamlit: https://project386-kphrwg43qlmc4ckfhr5gs6.streamlit.app/ 

scrape.py

This module scrapes tables from pro-football-reference.com.

nfl_package.scrape.get_offensive_game_stats_no_playoffs(base_url, years)
Scrapes the offensive tables for the specified years.
Parameters: base_url (str): the url to scrape from. years (list of int): list of integers of years where the team did not play in the playoffs.
Returns: dataframe: The combined offensive data from years the team did not play in the playoffs.

nfl_package.scrape.get_offensive_game_stats_with_playoffs(base_url, years)
Scrapes the offensive tables for the specified years and combines with the playoff tables.
Parameters: base_url (str): the url to scrape from. years (list of int): list of integers of years where the team played in the playoffs.
Returns: dataframe: The combined offensive data from years the team played in the playoffs.

nfl_package.scrape.get_opp_game_stats_no_playoffs(base_url, years)
Scrapes the opponent’s offensive tables for the specified years.
Parameters: base_url (str): the url to scrape from. years (list of int): list of integers of years where the team did not play in the playoffs.
Returns: dataframe: The combined offensive data from years the team did not play in the playoffs.

nfl_package.scrape.get_opp_game_stats_with_playoffs(base_url, years)
Scrapes the offensive tables for the specified years of the opponent and combines with the playoff tables.
Parameters: base_url (str): the url to scrape from. years (list of int): list of integers of years where the team played in the playoffs.
Returns: dataframe: The combined offensive data from years the team played in the playoffs.

clean.py

This module take the scraped data and tidies the dataframe. It adds a home_away column to identify if a game was played at home or not. It tidies the columns and adds proper column names.

nfl_package.clean.clean_offense_data(df)
Cleans the offensive dataset.
Parameters: df: The dataset to be cleaned.
Returns: df: The cleaned df.

nfl_package.clean.load_data(file_path)
Loads the dataset from the given file path.
Parameters: file_path (str): The file path of the dataset.
Returns: df: The dataset as a Pandas dataframe.

nfl_package.clean.save_cleaned_data(df, output_path)
Saves the cleaned dataset to the specified output path.
Parameters: df: The dataframe to save. output_path (str): The path to save the dataframe in.
Returns: df (csv): The dataframe as a csv file in the specified output path.


analysis.py

nfl_package.analysis.make_corr_matrix(df)
This function makes a correlation matrix.
Parameters: dataframe: the data you want to get correlations for.
Returns: corr_matrix: the correlation matrix.

nfl_package.analysis.score_correlations(corr_matrix, df)
This function gets the top 5 variables correlated with points scored and prints the descriptive statistics.
Parameters: corr_matrix: the correlation matrix produced from make_corr_matrix.
Returns: mat: the matrix of highly correlated variables with points scored.

nfl_package.analysis.top_boxplot(df)
This function created boxplots of the distribution of total time of possession for each game and whether it was a win or loss.
Parameters: df: the dataframe to be plotted.
Returns: fig: the figure to be plotted.

nfl_package.analysis.win_correlations(corr_matrix, df)
This function gets the top 5 variables correlated with wins and prints the descriptive statistics.
Parameters: corr_matrix: the correlation matrix produced from make_corr_matrix.
Returns: mat: the matrix of highly correlated variables with wins.

run_scrape.py: runs the scrape.py module using the defined base_url and years. Must define the years with playoffs and years without playoffs separately. This file concatenates the tables if the team had years in the playoffs and years not in the playoffs. This file makes the offensive table and the defensive table for each team.


run_clean.py: takes the scraped dataframes and uses the clean.py module to clean and save files as clean CSVs. Input paths and output paths are defined in this file.


run_analysis.py: Uses analysis.py to create correlation matrices for each team. Prints top 5 highly correlated variables with wins and total points scored as well as their descriptive summary statistics. Boxplots are also created using the analysis module.


