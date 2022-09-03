from cook import *

# 4.2

player_1 = input('player 1: ')
player_2 = input('player 2: ')
player_3 = input('player 3: ')

# 4.3

arr_1 = []
arr_2 = []
arr_3 = []

namenot = 0
for row in df_18.itertuples():
    if player_2 == row.player_name:
        namenot += 1
if namenot == 0:
    print('\nNBA player not in database.')
    quit()

for v in columns_norm:
    
    column = '{}_norm'.format(v)
    name = df_18.player_name

    x = df_18[column][name == player_1]
    x = x.values[0]
    arr_1.append(x)
    
    y = df_18[column][name == player_2]
    y = y.values[0]
    arr_2.append(y)
    
    z = df_18[column][name == player_3]
    z = z.values[0]
    arr_3.append(z)


d1 = distance_of(arr_1,arr_2)
d2 = distance_of(arr_1,arr_3)
d3 = distance_of(arr_2,arr_3)
d_min = min(d1,d2,d3)

if d_min == d1:
    print('\n{} and {} are more similar'.format(player_1, player_2))
elif d_min == d2:
    print('\n{} and {} are more similar'.format(player_2, player_3))
elif d_min == d3:
    print('\n{} and {} are more similar'.format(player_1, player_3))