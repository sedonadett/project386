from nfl_package.analysis import make_corr_matrix, win_correlations, score_correlations, top_boxplot
import pandas as pd

print("Chiefs Correlations and Plots")
df1 = pd.read_csv("nfl_package\datasets\kc_offensive_game_stats_cleaned.csv") 
kc_mat = make_corr_matrix(df1)
win_correlations(kc_mat, df1)
score_correlations(kc_mat, df1)
top_boxplot(df1)

print("Vikings Correlations and Plots")
df2 = pd.read_csv("nfl_package\datasets\min_offensive_game_stats_cleaned.csv") 
min_mat = make_corr_matrix(df2)
win_correlations(min_mat, df2)
score_correlations(min_mat, df2)
top_boxplot(df2)

