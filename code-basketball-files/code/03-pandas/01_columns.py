import pandas as pd
from project.config import get_file_path, FileExtension, Project

# Ejecutamos con 
# python3 -m code-basketball-files.code.03-pandas.01_columns

# Página 74 Ejercicio 1: Cargar los datos "games.csv". Esto lo usaremos para los siguientes puntos

# load player-game data

filePath = get_file_path("player_game", FileExtension.CSV, Project.BASKETBALL)
print("Find Path:", filePath)

pg = pd.read_csv(filePath)

# book picks up here:

# Página 76 - creating and modifying columns
print('Todos anotan 2 puntos')
pg['pts_per_shot'] = 2
print(pg[['game_id', 'player_id', 'pts_per_shot']].head(10))

print('Todos anotan 3 puntos')
pg['pts_per_shot'] = 3
print(pg[['game_id', 'player_id', 'pts_per_shot']].head(10))

# math and number columns
# fg3m = triples convertidos => puntos en triples 3*fg3m
# fgm = tiros de campo convertidos
# canasta de dos = fgm - fg3m => puntos de dos = (fgm - fg3m)*2
pg['pts_from_fgs'] = (pg['fg3m']*3 + (pg['fgm'] - pg['fg3m'])*2)

# Esto lo añado yo para mejorarlo
pg['fg2m'] = pg['fgm'] - pg['fg3m']

print("Puntos convertidos") # Añado yo fg2m y fg3m para mejorarlo
print(pg[['name', 'game_id', 'pts_from_fgs', 'fg2m', 'fg3m']].head())

# Página 77-78
import numpy as np  # note: normally you'd import this at the top of the file

pg['biggest_impact'] = np.abs(pg['plus_minus'])

pg['ln_pts'] = np.log(pg['pts'])

pg['court_length'] = 94

# 'sample' nos da una muestra aleatoria entre todos los registros
# 'head' da desde el registro 0 hasta 5 (por defecto) o el número que determinemos
print('Muestra aleatoria con "sample"')
print(pg[['name', 'game_id', 'court_length']].sample(5))

# string columns
print('Muestra aleatoria con "sample" mostrando los "name" en mayúsculas')
print(pg['name'].str.upper().sample(5))

print('Muestra aleatoria con "sample" mostrando los "name" donde sustituimos los "." por " "')
print(pg['name'].str.replace('.', ' ').sample(5))

print("Muestra aleatoria del nombre del jugador y su equipo")
print((pg['name'] + ', ' + pg['team']).sample(5))

print("Muestra aleatoria del nombre del jugador en minúsculas y sin '.'")
print(pg['name'].str.replace('.', ' ').str.lower().sample(5))

# boolean columns
pg['is_a_guard'] = (pg['pos'] == 'Guard')
print('Comprobar si son escoltas (Guard)')
print(pg[['name', 'pos', 'is_a_guard']].sample(5))

pg['is_a_forward_or_center'] = (pg['pos'] == 'Forward') | (pg['pos'] == 'Center')
pg['good_guard_game'] = (pg['pos'] == 'Guard') & (pg['pts'] >= 30)
pg['not_gt_10_pts_or_assists'] = ~((pg['pts'] > 10) | (pg['ast'] > 10))

print('Comprobar si son escoltas (Guard) o Pivots (Center)')
print(pg[['name', 'pos', 'is_a_forward_or_center']].sample(5))
print('Comprobar si son escoltas (Guard) con 30 ó + puntos')
print(pg[['name', 'pos', 'pts', 'good_guard_game']].sample(5))

print(pg[['name', 'pos', 'pts', 'ast', 'not_gt_10_pts_or_assists']].sample(5))

print('Más de 10 puntos y 10 asistencias ')
print((pg[['pts', 'ast']] > 10).sample(5))

# Operación vectorizada con nueva columna
pg["more_than_10_pts_ast"] = (pg["pts"] > 10) & (pg["ast"] > 10)

print('Más de 10 puntos y 10 asistencias ')
print(pg[['name', 'more_than_10_pts_ast', 'pts', 'ast']].sample(5))

# Applying functions to columns
def is_w_pac(team):
  """
  Takes some string named team ('MIL', 'LAL', 'CHI' etc) and checks
  whether it's in the Pacific Division.
  """
  return team in ['LAC', 'LAL', 'PHX', 'SAC', 'GSW']

pg['is_w_pac'] = pg['team'].apply(is_w_pac)

print("Equipos de División del Pacífico")
print(pg[['name', 'team', 'is_w_pac']].sample(5))

pg['is_w_pac_alternate'] = pg['team'].apply(
    lambda x: x in ['LAC', 'LAL', 'PHX', 'SAC', 'GSW'])

print("Equipos de División del Pacífico (con lambda)")
print(pg[['name', 'team', 'is_w_pac_alternate']].sample(5))

print('Columnas actuales:')
print(pg.columns)

# Página 80-81

# Dropping Columns
pg.drop('is_w_pac_alternate', axis=1, inplace=True)
pg.drop('is_w_pac', axis=1, inplace=True)


print('Columnas actuales:')
print(pg.columns)

# Renaming Columns
pg.columns = [x.upper() for x in pg.columns]

print('Columnas actuales después de convertir en mayúsculas:')
print(pg.columns)

print("Primeros 5 registros:", pg.head())

# Volver a ponerlas en minúsculas
pg.columns = [x.lower() for x in pg.columns]

print('Columnas actuales después de convertir en minúsculas:')
print(pg.columns)

# Renombrar columnas
print('Columnas actuales después de renombrar fgm por field_goals_made:')

pg.rename(columns={'fgm': 'field_goals_made'}, inplace=True)
print(pg.columns)

# missing data
pg['ft_pct'] = pg['ftm']/pg['fta']
pg[['name', 'team', 'ftm', 'fta', 'ft_pct']].head()

pg['ft_pct'].isnull().head()

pg['ft_pct'].notnull().head()

pg['ft_pct'].fillna(-99).head()

# Changing column types
pg['date'].sample(5)

date = '20191119'

year = date[0:4]
month = date[4:6]
day = date[6:8]

year
month
day

# pg['month'] = pg['date'].str[4:6]  # commented out since it gives an error

pg['month'] = pg['date'].astype(str).str[4:6]
pg[['name', 'team', 'month', 'date']].sample(5)

pg['month'].astype(int).sample(5)

pg.dtypes.head()
