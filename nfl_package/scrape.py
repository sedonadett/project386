import pandas as pd

def get_game_stats(base_url, start_year, end_year):
    all_data = []
    
    for year in range(start_year, end_year + 1):
        url = base_url.format(year=year)
        tables = pd.read_html(url,  header=[0, 1])
        year_data = tables[1]
        year_data['Year'] = year
        all_data.append(year_data)
    
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df