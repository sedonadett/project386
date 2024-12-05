import pandas as pd

def get_offensive_game_stats_with_playoffs(base_url, years):
    all_data = []
    
    for year in years:
        url = base_url.format(year=year)
        tables = pd.read_html(url,  header=[0, 1])
        table_0 = tables[0]
        table_0['Year'] = year
        all_data.append(table_0)
        table_1 = tables[1]
        table_1['Year'] = year
        all_data.append(table_1)
    
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df


def get_offensive_game_stats_no_playoffs(base_url, years):
    all_data = []
    
    for year in years:
        url = base_url.format(year=year)
        tables = pd.read_html(url,  header=[0, 1])
        year_data = tables[0]
        year_data['Year'] = year
        all_data.append(year_data)
    
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df


def get_opp_game_stats_with_playoffs(base_url, years):
    all_data = []
    
    for year in years:
        url = base_url.format(year=year)
        tables = pd.read_html(url,  header=[0, 1])
        table_2 = tables[2]
        table_2['Year'] = year
        all_data.append(table_2)
        table_3 = tables[3]
        table_3['Year'] = year
        all_data.append(table_3)
    
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df


def get_opp_game_stats_no_playoffs(base_url, years):
    all_data = []
    
    for year in years:
        url = base_url.format(year=year)
        tables = pd.read_html(url,  header=[0, 1])
        year_data = tables[1]
        year_data['Year'] = year
        all_data.append(year_data)
    
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df