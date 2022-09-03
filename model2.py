from model1 import *

player_1 = 'Stephen Curry'
player_2 = input('player 2: ')
arr_1 = []
arr_2 = []

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


d = distance(arr_1,arr_2)
d = round(d,3)

print('\nThe distance from {} is equal to {}'.format(player_1, d))