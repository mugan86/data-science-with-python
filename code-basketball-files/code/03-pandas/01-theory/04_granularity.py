import pandas as pd
from project.config import get_file_path, FileExtension, Project

# Extraet todos los valores "desc" para analizarlo y sustituirlo en Español
## unique_desc = shots['desc'].drop_duplicates()
# print(unique_desc)
# Para traducir las descripciones al Español
desc_translation = {
    "Layup Shot": "Bandeja",
    "Pullup Jump shot": "Tiro en suspensión en movimiento",
    "Jump Shot": "Tiro en suspensión",
    "Step Back Jump shot": "Tiro en suspensión paso atrás",
    "Tip Layup Shot": "Bandeja tras rebote",
    "Turnaround Fadeaway shot": "Tiro en giro y paso atrás",
    "Dunk Shot": "Mate",
    "Driving Layup Shot": "Bandeja en penetración",
    "Cutting Dunk Shot": "Mate tras corte",
    "Turnaround Hook Shot": "Gancho en giro",
    "Cutting Layup Shot": "Bandeja tras corte",
    "Putback Dunk Shot": "Mate tras rebote ofensivo",
    "Running Pull-Up Jump Shot": "Tiro en suspensión en carrera",
    "Running Dunk Shot": "Mate en carrera",
    "Fadeaway Jump Shot": "Tiro en suspensión en retirada",
    "Floating Jump shot": "Tiro flotante",
    "Running Layup Shot": "Bandeja en carrera",
    "Driving Floating Jump Shot": "Tiro flotante en penetración",
    "Turnaround Jump Shot": "Tiro en suspensión tras giro",
    "Hook Bank Shot": "Gancho con tablero",
    "Turnaround Bank Hook Shot": "Gancho con tablero tras giro",
    "Tip Dunk Shot": "Mate tras toque",
    "Finger Roll Layup Shot": "Bandeja con efecto (finger roll)",
    "Reverse Layup Shot": "Bandeja invertida",
    "Putback Layup Shot": "Bandeja tras rebote ofensivo",
    "Driving Finger Roll Layup Shot": "Bandeja con efecto en penetración",
    "Alley Oop Layup shot": "Bandeja tipo alley-oop",
    "Running Finger Roll Layup Shot": "Bandeja con efecto en carrera",
    "Driving Reverse Layup Shot": "Bandeja invertida en penetración",
    "Alley Oop Dunk Shot": "Mate tipo alley-oop",
    "Hook Shot": "Gancho",
    "Driving Dunk Shot": "Mate en penetración",
    "Driving Floating Bank Jump Shot": "Tiro flotante con tablero en penetración",
    "Driving Hook Shot": "Gancho en penetración",
    "Running Alley Oop Dunk Shot": "Mate alley-oop en carrera",
    "Running Jump Shot": "Tiro en suspensión en carrera",
    "Driving Bank Hook Shot": "Gancho con tablero en penetración",
    "Reverse Dunk Shot": "Mate invertido",
    "Jump Bank Shot": "Tiro en suspensión con tablero",
    "Turnaround Fadeaway Bank Jump Shot": "Tiro en giro y retirada con tablero",
    "Running Reverse Layup Shot": "Bandeja invertida en carrera",
    "Cutting Finger Roll Layup Shot": "Bandeja con efecto tras corte",
    "Step Back Bank Jump Shot": "Tiro paso atrás con tablero",
    "Driving Reverse Dunk Shot": "Mate invertido en penetración",
    "Running Alley Oop Layup Shot": "Bandeja alley-oop en carrera"
}


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

# Ordenar por distancia descendente de más lejos a más cerca
longest_shots = longest_shots.sort_values(by='dist', ascending=False).reset_index(drop=True)

# Crear una columna de texto indicando si fue encestado o no
longest_shots['result'] = longest_shots['made'].map({True: '✅', False: '❌'})
longest_shots['dist_m'] = longest_shots['dist'] * 0.3048 # Convertir la distancia a metros

# Mostrar resultados
print(longest_shots[['game_id', 'name', 'team', 'opp', 'dist', 'dist_m', 'value', 'result', 'desc']])

# make attempt and made variables
shots['fg3m'] = (shots['value'] == 3) & shots['made'] # Triple anotado
shots['fg3a'] = (shots['value'] == 3) # Triple intentado (anote o no)
shots['fga'] = 1 # Representa un tiro intentado por registro:
shots['fgm'] = shots['made'] # Tiros de campo anotados
shots['dist_m'] = shots['dist'] * 0.3048 # Convertir la distancia a metros
shots['result'] = shots['made'].map({True: '✅', False: '❌'})
# Creamos una nueva columna con la descripción en español
shots['desc_es'] = shots['desc'].map(desc_translation)

# Datos de Curry
print("Stephen Curry stats 3 point")
print(shots.query("name == 'S. Curry' & value == 3").sort_values(by='dist', ascending=False)[['name', 'dist_m', 'result', 'desc_es']].head(20))


# Página 105 - Esto es lo del libro, lo anterior me lo he inventado por repasar
# Granularity
# Grouping
# Agrupa todos los tiros de un game_id concreto y
# luego ba sumando todos los valores de todos los registros
# Así podemos sacar resúmenes
print(shots.groupby('game_id').sum()[['name', 'dist_m', 'made']].head())  # book picks up here

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

# Calculamos porcentajes de los jugadores en un partido concreto
shots_per_pg['fg_percent'] = (shots_per_pg['fgm'] / shots_per_pg['fga'] * 100).round(1).fillna('---')
shots_per_pg['fg3_percent'] = (shots_per_pg['fg3m'] / shots_per_pg['fg3a'] * 100).round(1).fillna('---')

print(shots_per_pg.head(20))

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

