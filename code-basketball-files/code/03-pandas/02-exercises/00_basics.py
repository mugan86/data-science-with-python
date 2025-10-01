import pandas as pd
from project.config import get_file_path, FileExtension, Project

# Ejecutamos con 
# python3 -m code-basketball-files.code.03-pandas.02-exercises.00_basics

# Página 74 Ejercicio 1: Cargar los datos "games.csv". Esto lo usaremos para los siguientes puntos

filePath = get_file_path("games", FileExtension.CSV, Project.BASKETBALL)
print("Find Path:", filePath)

##############
# Loading data
##############

print("========== LOADING DATA AND TAKE TYPE ==========")
games = pd.read_csv(filePath)

print(type(games))

print(games.head())

# Página 74 Ejercicio 2: cree un elemento DataFrame "games50" con los primeros 50 juegos ordenador por fecha

games50 = games.head(50).sort_values("date")

print(games50[['game_id','home','away','date']].head(50))

# Página 74 Ejercicio 3: Ordenar "games" mediante "home_pts" en ordenamiento descendente.

games.sort_values("home_pts", ascending=False, inplace=True)
print(games.head(30))

# Página 74 Ejercicio 4 - Que tipo es games.sort_values("home_pts")

print(type(games.sort_values("home_pts"))) ## <class 'pandas.core.frame.DataFrame'>

# Página 74 Ejercicio 5

# a ) Crea un nuevo DataFrame games_simple con las columnas 'date', 'home', 'away', 'home_pts' y 'away_pts'

games_simple = games[['date', 'home', 'away', 'home_pts', 'away_pts']]

print(games_simple)

"""
           date home away  home_pts  away_pts
281  2019-11-30  HOU  ATL       158       111
60   2019-10-30  WAS  HOU       158       159
686  2020-01-26  ATL  WAS       152       133
704  2020-01-28  MIL  WAS       151       131
291  2019-12-01  LAC  WAS       150       125
..          ...  ...  ...       ...       ...
673  2020-01-24  CHI  SAC        81        98
392  2019-12-15  GSW  SAC        79       100
918  2020-03-04  BKN  MEM        79       118
791  2020-02-10  DET  CHA        76        87
374  2019-12-13  CHI  CHA        73        83

[1059 rows x 5 columns]
"""

# b ) Modificar games_simple cambiando a 'home', 'away', 'date', 'home_pts', 'away_pts'

games_simple = games_simple[['home', 'away', 'date', 'home_pts', 'away_pts']]

print(games_simple)

"""
    home away        date  home_pts  away_pts
281  HOU  ATL  2019-11-30       158       111
60   WAS  HOU  2019-10-30       158       159
686  ATL  WAS  2020-01-26       152       133
704  MIL  WAS  2020-01-28       151       131
291  LAC  WAS  2019-12-01       150       125
..   ...  ...         ...       ...       ...
673  CHI  SAC  2020-01-24        81        98
392  GSW  SAC  2019-12-15        79       100
918  BKN  MEM  2020-03-04        79       118
791  DET  CHA  2020-02-10        76        87
374  CHI  CHA  2019-12-13        73        83

[1059 rows x 5 columns]
"""

# c) Asignar nueva columna 'game_id' en 'games_simple' cogiendo desde 'games'

games_simple['game_id'] = games['game_id']
print(games_simple.head())

"""
    home away        date  home_pts  away_pts   game_id
281  HOU  ATL  2019-11-30       158       111  21900282
60   WAS  HOU  2019-10-30       158       159  21900061
686  ATL  WAS  2020-01-26       152       133  21900687
704  MIL  WAS  2020-01-28       151       131  21900705
181  LAC  ATL  2019-11-16       150       101  21900182
"""

# d) Crear un fichero nuevo a partir de games_simple que se llamará games_simple.txt y se separará con '|' en vez de ','

games_simple.to_csv(get_file_path("games_simple", FileExtension.TXT, Project.BASKETBALL), sep='|')

# Genera fichero en code-with-basketball\code-basketball-files\data