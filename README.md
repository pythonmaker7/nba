# Compare 2 players' similitude

We ask a user to write down 3 nba players.
We tell the user which pair out of these 3 players played more similarly during the season 2018-19.

A few examples
{Stephen Curry, Kyrie Irving, Steven Adams}     ->    {Stephen Curry, Kyrie Irving}
{Joel Embiid, Rudy Gay, Damian Lillard}         ->    {Joel Embiid, Damian Lillard}

1.    find data
2.    clean data
3.    normalize stats
4.    calculate distance

1.1   read per_game stats

2.1   drop rows with empty cells

2.2   drop scrubs with few games/minutes

2.3   only keep 2017-18 season

3.1   define normalization

3.2   create 1 new normalized column for each stat

4.1   define distance

4.2   ask user for players

4.3   calculate distance
