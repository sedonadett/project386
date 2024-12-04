from nfl_package.scrape import get_game_stats

start_year = 2019
end_year = 2023

kc_template = 'https://www.pro-football-reference.com/teams/kan/{year}.htm#all_games'
kc_combined_df = get_game_stats(kc_template, start_year, end_year)

kc_combined_df.to_csv("kc_game_stats.csv", index=False)
print("Data saved to kc_game_stats.csv")