import pandas as pd
from project.config import get_file_path, FileExtension, Project

# Ejecutamos con 
# python3 -m code-basketball-files.code.03-pandas.01-theory.04_granularity

# load shots data

filePath = get_file_path("shots", FileExtension.CSV, Project.BASKETBALL)
print("Find Path:", filePath)

shots = pd.read_csv(filePath)

# extra
# Encontrar el tiro más lejano de cada partido
longest_shots = shots.loc[
    shots.groupby('game_id')['dist'].idxmax(),
    ['game_id', 'name', 'team', 'opp', 'dist', 'value', 'made', 'desc']
]

# Ordenar por distancia descendente
longest_shots = longest_shots.sort_values(by='dist', ascending=False).reset_index(drop=True)

# Crear una columna de texto indicando si fue encestado o no
longest_shots['result'] = longest_shots['made'].map({True: '✅', False: '❌'})
longest_shots['dist_m'] = longest_shots['dist'] * 0.3048

# Mostrar resultados
print(longest_shots[['game_id', 'name', 'team', 'opp', 'dist', 'dist_m', 'value', 'result', 'desc']])

# make attempt and made variables
shots['fg3m'] = (shots['value'] == 3) & shots['made']
shots['fg3a'] = (shots['value'] == 3)
shots['fga'] = 1
shots['fgm'] = shots['made']
shots['dist_m'] = shots['dist'] * 0.3048

# Datos de Curry

print(shots.query("name == 'S. Curry' & value == 3").sort_values(by='dist', ascending=False)[['name', 'dist_m', 'made']].head(20))


# Granularity
# Grouping
# Agrupa todos los tiros de un game_id concreto y
# luego ba sumando todos los valores de todos los registros
# Así podemos sacar resúmenes
print(shots.groupby('game_id').sum().head())  # book picks up here

fg_cols = ['fgm', 'fga', 'fg3m', 'fg3a']

# Lo anterior pero seleccionando las columnas que deseamos
print(shots.groupby('game_id').sum()[fg_cols].head())

"""
agg() sirve para resumir o combinar valores dentro de grupos, aplicando 
funciones como sum, mean (media aritmética), count, min, max, etc.
Puedes usar una función, varias funciones, o incluso funciones personalizadas.
"""
print(
shots.groupby('game_id').agg({
    'value': 'mean',    # Media aritmética del valor de anotación de los tiros (2 o 3pt)
    'fgm': 'sum',       # Tiros de campo totales convertidos
    'fga': 'sum',       # Tiros de campo totales intentandos
    'fg3m': 'sum',      # Triples anotados
    'fg3a': 'sum',      # Triples intentados
    }).head())

# Otra forma de agregar en formato direccionario los valores agrupados de game_id
# para los tiros
print(shots.groupby('game_id').agg(
    ave_value = ('value', 'mean'),
    ave_dist= ('dist', 'mean'),
    max_dist  = ('dist', 'max'),
    ave_dist_m= ('dist_m', 'mean'),
    max_dist_m  = ('dist_m', 'max'),
    fgm = ('fgm', 'sum'),
    fga = ('fga', 'sum'),
    fg3m = ('fg3m', 'sum'),
    fg3a = ('fg3a', 'sum')).head())

shots_per_pg = shots.groupby(['game_id', 'player_id']).agg(
    name = ('name', 'first'),
    fgm = ('fgm', 'sum'),
    fga = ('fga', 'sum'),
    fg3m = ('fg3m', 'sum'),
    fg3a = ('fg3a', 'sum'),
    ave_dist= ('dist', 'mean'),
    max_dist  = ('dist', 'max'),
    ave_dist_m= ('dist_m', 'mean'),
    max_dist_m  = ('dist_m', 'max'),
)

print(shots_per_pg.head())

# A note on multilevel indexing
shots_per_pg.loc[[(21900002, 2544), (21900008, 201143)]]

# Stacking and unstacking data
sv = (shots
      .groupby(['team', 'value'])['made']
      .sum()
      .reset_index())

sv.head()

sv_reshaped = sv.set_index(['team', 'value']).unstack()
sv_reshaped.head()

total_made = sv_reshaped.sum(axis=1)
total_made.head()

sv_reshaped.columns = [2, 3]
(sv_reshaped[3]/total_made).head()

sv_reshaped.stack().head()

