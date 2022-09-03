#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# hide warnings
pd.options.mode.chained_assignment = None  # default='warn'

# 1.1

df_stats = pd.read_csv('nba-stats-csv/player_general_traditional_per_game_data.csv')
df_names = pd.read_csv('nba-stats-csv/player_id_player_name.csv')
df_raw = pd.merge(df_names, df_stats, on='player_id', how='left')

# 2.1

df_nonull = df_raw.dropna(axis=0, how='any')

# 2.2

bin_values = np.arange(start=0, stop=82, step=2)
plt.hist(x=df_nonull['gp'], bins = bin_values)
#plt.show()

condition = (df_nonull['gp'] > 10) & (df_nonull['min'] > 20)
df_noscrubs = df_nonull[condition]

# 2.3

df_18 = df_noscrubs[df_noscrubs['season_id'] == '2017-18']

# 3.1

columns_norm = ['pts','oreb','dreb','ast','stl','blk','tov','fta','ftm','fg3m','fg3a','fgm','fga']

def norm(col):    
    col_norm = (col - mini) / (maxi - mini)
    return col_norm

# 3.2

for v in columns_norm:
    mini = df_18['{}'.format(v)].min()
    maxi = df_18['{}'.format(v)].max()
    df_18['{}_norm'.format(v)] = round(df_18['{}'.format(v)].apply(norm), 2)

# 4.1

def distance_of(u,v):
    u = np.array(u)
    v = np.array(v)
    d = np.sqrt(np.sum(u-v)**2)
    return d