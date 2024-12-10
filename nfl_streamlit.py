import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('nfl_package/datasets/kc_offensive_game_stats_cleaned.csv')

# Scatterplot for Chiefs
st.title('Scatterplot of Points Scored vs Points Allowed')
years_selected = []
for year in range(2019, 2024):
    if st.checkbox(f'{year}', value=True):
        years_selected.append(year)

filtered_df = df[df['year'].isin(years_selected)]

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(filtered_df['pts_scored'], filtered_df['pts_allowed'], c=filtered_df['year'], cmap='viridis')
ax.set_xlabel('Points Scored')
ax.set_ylabel('Points Allowed')
ax.set_title('Points Scored vs Points Allowed')
cbar = plt.colorbar(ax.collections[0], ax=ax)
cbar.set_label('Year')
st.pyplot(fig)

# box plot of wins and losses and the time of possession for each team
