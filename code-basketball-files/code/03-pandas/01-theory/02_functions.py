import pandas as pd
from project.config import get_file_path, FileExtension, Project

# Ejecutamos con 
# python3 -m code-basketball-files.code.03-pandas.01-theory.02_functions

# Página 74 Ejercicio 1: Cargar los datos "games.csv". Esto lo usaremos para los siguientes puntos

# load player-game data

filePath = get_file_path("player_game", FileExtension.CSV, Project.BASKETBALL)
print("Find Path:", filePath)

pg = pd.read_csv(filePath)

## Convierte a string algunos datos
pg[['game_id', 'player_id', 'date']] = (
    pg[['game_id', 'player_id', 'date']].astype(str))

# book picks up here:
print('Media de los siguientes datos:')
print(pg[['fgm', 'fga', 'fg_pct', 'pts', 'fg3m', 'fg3a', 'fg3_pct']].mean())
print(pg[['name', 'fgm', 'fga', 'pts', 'fg3m', 'fg3a']].max())

pg.max()

# Axis
pg[['pts', 'ast', 'stl', 'reb']].mean(axis=0)
pg[['pts', 'ast', 'stl', 'reb']].mean(axis=1).head()

# Summary functions on boolean columns
pg['cold_shooting'] = (pg['fga'] > 10) & (pg['pts'] < 5)
pg['cold_shooting'].mean()

pg['cold_shooting'].sum()

(pg['fg3a'] > 30).any()
(pg['fg3a'] > 20).any()

(pg['min'] > 0).all()

(pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10).any(axis=1)

pg['triple_double'] = ((pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10)
                       .sum(axis=1) >= 3)

(pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10).head()
(pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10).sum(axis=1).head()
((pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10).sum(axis=1) >= 3).head()

pg['triple_double'].sum()

# Other misc built-in summary functions
pg['pos'].value_counts()

pg['pos'].value_counts(normalize=True)

pd.crosstab(pg['team'], pg['pos']).head()
