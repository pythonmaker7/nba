#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# hide warnings
pd.options.mode.chained_assignment = None  # default='warn'

df_stats = pd.read_csv('nba-stats-csv/player_general_traditional_per_game_data.csv')
df_names = pd.read_csv('nba-stats-csv/player_id_player_name.csv')
df_raw = pd.merge(df_names, df_stats, on='player_id', how='left')

# 1
# drop empty rows # deleted 2 rows
# new table NONULL

df_nonull = df_raw.dropna(axis=0, how='any')

# 2
# delete rows with few games/minutes
# new table NOSCRUBS

# 2.1 diagram 'gp'
bin_values = np.arange(start=0, stop=82, step=2)
plt.hist(x=df_nonull['gp'], bins = bin_values)
#plt.show()

# 2.3 
condition = (df_nonull['gp'] > 10) & (df_nonull['min'] > 20)
df_noscrubs = df_nonull[condition]

# 3
# keep only 2017-18 season
# new table 18

df_18 = df_noscrubs[df_noscrubs['season_id'] == '2017-18']

# 4
# for each column create norm version

# 4.1 do it for 1 column
# 4.2 use apply for many columns

columns_norm = ['pts','oreb','dreb','ast','stl','blk','tov','fta','ftm','fg3m','fg3a','fgm','fga']

#function that gets series
def norm(col):    
    col_norm = (col - mini) / (maxi - mini)
    return col_norm

for v in columns_norm:
    mini = df_18['{}'.format(v)].min()
    maxi = df_18['{}'.format(v)].max()
    df_18['{}_norm'.format(v)] = round(df_18['{}'.format(v)].apply(norm), 2)

# 5 calculate distance
# 5.1 euclidean takes arrays

def distance(u,v):
    u = np.array(u)
    v = np.array(v)
    d = np.sqrt(np.sum(u-v)**2)
    return d