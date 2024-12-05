from nfl_package.scrape import get_offensive_game_stats_with_playoffs, get_offensive_game_stats_no_playoffs, get_opp_game_stats_with_playoffs, get_opp_game_stats_no_playoffs
import pandas as pd 

# KC templates
kc_years_with_playoffs = [2019,2020,2021,2022,2023]
kc_template = 'https://www.pro-football-reference.com/teams/kan/{year}/gamelog/'

# KC offensive table
kc_offensive_combined_df = get_offensive_game_stats_with_playoffs(kc_template, kc_years_with_playoffs)
kc_offensive_combined_df.to_csv("kc_offensive_game_stats.csv", index=False)
print("Data saved to kc_offensive_game_stats.csv")

# KC OPP table
kc_opp_combined_df = get_opp_game_stats_with_playoffs(kc_template, kc_years_with_playoffs)
kc_opp_combined_df.to_csv('kc_opp_game_stats.csv', index = False)
print('Data saved to kc_opp_game_stats.csv')

# MIN template
min_years_no_playoffs = [2020, 2021, 2023]
min_years_with_playoffs = [2019, 2022]
min_template = 'https://www.pro-football-reference.com/teams/min/{year}/gamelog/'

# MIN offensive table
min_df1 = get_offensive_game_stats_with_playoffs(min_template, min_years_with_playoffs)
min_df2 = get_offensive_game_stats_no_playoffs(min_template, min_years_no_playoffs)
min_combined_df = pd.concat([min_df1, min_df2], axis=0)
min_combined_df.to_csv("min_offensive_game_stats.csv", index=False)
print("Data saved to min_offensive_game_stats.csv")

# MIN OPP table
min_df1_opp = get_opp_game_stats_with_playoffs(min_template, min_years_with_playoffs)
min_df2_opp = get_opp_game_stats_no_playoffs(min_template, min_years_no_playoffs)
min_combined_df_opp = pd.concat([min_df1_opp, min_df2_opp], axis=0)
min_combined_df_opp.to_csv("min_opp_game_stats.csv", index=False)
print("Data saved to min_opp_game_stats.csv")