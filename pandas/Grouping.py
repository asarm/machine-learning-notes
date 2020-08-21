import pandas as pd

games = pd.read_csv('HomeGames.csv')
df = pd.DataFrame(games)

print(games)
print()

year = df.groupby('year.key')
#print(f'{year.get_group(1878)}\n')

team = df.groupby('team.key')
print(f"{team.get_group('TOR').mean()}")
print(f"{team.get_group('TOR').sum()}")
#print(f"{team.get_group('BSN')}")

filt = df.filter(['games'])
print(filt)

team = df.groupby(['team.key','year.key'])
print(team.mean())