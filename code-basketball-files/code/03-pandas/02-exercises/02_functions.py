import pandas as pd
from project.config import get_file_path, FileExtension, Project

# Ejecutamos con 
# python3 -m code-basketball-files.code.03-pandas.02-exercises.02_functions

# Página 94 Ejercicio 1: Cargar los datos "player_game.csv". Esto lo usaremos para los siguientes puntos

# load player-game data

filePath = get_file_path("player_game", FileExtension.CSV, Project.BASKETBALL)
print("Find Path:", filePath)

pg = pd.read_csv(filePath)

# Página 94 Ejercicio 2: Agrega a pg una columna que dé el número total de tiros (tiros de campo y tiros libres) 
# para cada partido de jugador.
# Hazlo de dos formas: una usando operaciones aritméticas básicas (suma con +) y otra usando una función incorporada de pandas 'sum()'.
# Llámalas 'total_shots1' y 'total_shots2'. Demuestra que son iguales.

pg['total_shots1'] = pg['fga'] + pg['fta']
pg['total_shots2'] = pg[['fga', 'fta']].sum(axis=1) # Importante que vaya cogiendo fila a fila y sumando los reusltados que hay por fila

print(pg['total_shots1'])
print(pg['total_shots2'])

# Comprobar que son iguales los resultados
print('¿Los dos valores iguales?', (pg['total_shots1'] == pg['total_shots2']).all())