from nfl_package.clean import load_data, clean_offense_data, save_cleaned_data

# KC Offensive table
kco_input_path = 'kc_offensive_game_stats.csv'
kco_output_path = 'nfl_package/datasets/kc_offensive_game_stats_cleaned.csv'

kco_df = load_data(kco_input_path)
kc_offense_cleaned_df = clean_offense_data(kco_df)
save_cleaned_data(kc_offense_cleaned_df, kco_output_path)

# KC OPP table
kc_opp_input_path = 'kc_opp_game_stats.csv'
kc_opp_output_path = 'nfl_package/datasets/kc_opp_game_stats_cleaned.csv'

kc_opp_df = load_data(kc_opp_input_path)
kc_opp_cleaned_df = clean_offense_data(kc_opp_df)
save_cleaned_data(kc_opp_cleaned_df, kc_opp_output_path)

# MIN Offensive table
mino_input_path = 'min_offensive_game_stats.csv'
mino_output_path = 'nfl_package/datasets/min_offensive_game_stats_cleaned.csv'

mino_df = load_data(mino_input_path)
mino_offense_cleaned_df = clean_offense_data(mino_df)
save_cleaned_data(mino_offense_cleaned_df, mino_output_path)

# MIN Opp table
min_opp_input_path = 'min_opp_game_stats.csv'
min_opp_output_path = 'nfl_package/datasets/min_opp_game_stats_cleaned.csv'

min_opp_df = load_data(min_opp_input_path)
min_opp_cleaned_df = clean_offense_data(min_opp_df)
save_cleaned_data(min_opp_cleaned_df, min_opp_output_path)