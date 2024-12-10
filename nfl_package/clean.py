import pandas as pd

def load_data(file_path):
    """Loads the dataset from the given file path."""
    return pd.read_csv(file_path, header = 1)

def clean_offense_data(df):
    """Cleans the dataset."""
    df['home_away'] = df['Unnamed: 6_level_1'].apply(lambda x: 'away' if x == '@' else 'home')
    df = df.drop(columns=['Unnamed: 3_level_1', 'Unnamed: 6_level_1'])
    df = df.dropna(subset=['Day'])
    df.columns = ['week', 'day', 'date', 'win_loss', 'OT', 'opp', 
                  'pts_scored', 'pts_allowed', 'passes_completed', 'passing_att',
                  'passing_yds', 'passing_tds', 'int_thrown', 
                  'times_sacked', 'yds_lost_from_sack', 'yds/pass_attempt', 
                  'netyds/pass_attempt', 'pass_completion_percent', 
                  'passer_rating', 'rushing_attempts', 'rushing_yds_gained', 
                  'rushing_yds/attempt', 'rushing_tds', 'fgm', 'fga', 'xpm', 
                  'xpa', 'times_punted', 'total_punt_yds', '3dconv', '3dattempt',
                   '4dconv', '4datt', 'off_top', 'year', 'home_or_away']
    df['off_top'] = [int(minutes) + (int(seconds) / 60) for minutes, seconds in (time.split(":") for time in df['off_top'])]
    return df

def save_cleaned_data(df, output_path):
    """Saves the cleaned dataset to the specified output path."""
    df.to_csv(output_path, index=False)