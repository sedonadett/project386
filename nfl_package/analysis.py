import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def make_corr_matrix(df):
    """
    This function makes a correlation matrix.

    Parameters: 
    dataframe: the data you want to get correlations for.

    Returns:
    corr_matrix: the correlation matrix.
    
    """
    df['win_loss_binary'] = [1 if x == 'W' else 0 for x in df['win_loss']]
    columns_to_drop = ['week', 'day', 'date', 'win_loss', 'OT', 'opp', 'year', 'home_or_away']
    df_temp = df.drop(columns=columns_to_drop, axis=1)
    corr_matrix = df_temp.corr()
    return corr_matrix


def win_correlations(corr_matrix, df):
    """
    This function gets the top 5 variables correlated with wins and prints the descriptive statistics.

    Parameters:
    corr_matrix: the correlation matrix produced from make_corr_matrix.

    Returns:
    mat: the matrix of highly correlated variables with wins.
    """
    mat = corr_matrix['win_loss_binary'].sort_values(ascending=False)
    print("Correlation with Win/Loss (top 5):")
    print(mat[1:6])
    wins_descriptive_stats = df[mat[1:6].index].describe()
    print("\nDescriptive Statistics for Top 5 Variables correlated with wins:")
    print(wins_descriptive_stats)
    return mat


def score_correlations(corr_matrix, df):
    """
    This function gets the top 5 variables correlated with points scored and prints the descriptive statistics.

    Parameters:
    corr_matrix: the correlation matrix produced from make_corr_matrix.

    Returns:
    mat: the matrix of highly correlated variables with points scored.
    """
    mat = corr_matrix['pts_scored'].sort_values(ascending=False)
    print("Correlation with Points Scored (top 5):")
    print(mat[1:6])
    points_descriptive_stats = df[mat[1:6].index].describe()
    print("\nDescriptive Statistics for Top 5 Variables correlated with points scored:")
    print(points_descriptive_stats)
    return mat


def top_boxplot(df):
    """
    This function created boxplots of the distribution of total time of possession for each game and whether it was a win or loss.

    Parameters:
    df: the dataframe to be plotted.

    Returns:
    fig: the figure to be plotted.
    """
    df['win_loss_binary'] = [1 if x == 'W' else 0 for x in df['win_loss']]
    win_data = df[df['win_loss_binary'] == 1]['off_top']
    loss_data = df[df['win_loss_binary'] == 0]['off_top']
    data = [win_data, loss_data]
    
    fig, ax = plt.subplots(figsize =(10, 7))
    
    bp = ax.boxplot(data, patch_artist=True, labels=['Wins', 'Losses'])
    ax.set_title('Boxplot of Time of Possession for Wins and Losses')
    ax.set_ylabel('Time of Possession')
    ax.set_xlabel('Game Result')

    colors = ['blue', 'red']
    for box, color in zip(bp['boxes'], colors):
        box.set(facecolor=color, alpha=0.5) 

    positions = [1, 2]
    for pos, dataset, color in zip(positions, data, colors):
        jittered_x = np.random.normal(pos, 0.025, size=len(dataset))
        ax.scatter(jittered_x, dataset, alpha=0.6, color=color)

    return fig
