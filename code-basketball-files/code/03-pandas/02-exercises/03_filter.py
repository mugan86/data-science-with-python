import pandas as pd
from project.config import get_file_path, FileExtension, Project

# Ejecutamos con 
# python3 -m code-basketball-files.code.03-pandas.02-exercises.03_filter

# Página 103 Ejercicio 1: Cargar los datos "team_games.csv". Esto lo usaremos para los siguientes puntos

# load team_games data

filePath = get_file_path("team_games", FileExtension.CSV, Project.BASKETBALL)
print("Find Path:", filePath)

dfp = pd.read_csv(filePath)

# Página 103 Ejercicio 2: Crear un pequeño DataFrame con los partidos de los Chicago Bulls (CHI) con las columnas 
# 'team', 'date', 'pts', 'fgm', 'fga'.
# Para ello usa:
# a) sintáxis 'loc' llamando al dataframe dft_chi1
# b) sintáxis 'query' llamando al dataframe dft_chi2

dft_chi1 = dfp.loc[dfp['team'] == 'CHI'][['team', 'date', 'pts', 'fgm', 'fga']]

print(dft_chi1.head(5))

"""
EXTRA para darle repaso a cosas estudiadas antes como modificar columnas
Los campos FGM y FGA (Field Goals Made/Attempted) incluyen todos los tiros de campo, es decir:
Tiros de 2 puntos (dobles).
Tiros de 3 puntos (triples).
Por eso tienes, además, las columnas FG3M y FG3A, que son un desglose solo de triples.
Si quieres calcular los tiros de 2 puntos:
Intentados de 2 pts = FGA - FG3A
Encestados de 2 pts = FGM - FG3M
% de 2 pts = (FGM - FG3M) / (FGA - FG3A)
👉 Ejemplo con tu primer partido (HOU vs. PHI):
FGA = 80
FG3A = 48
⇒ Tiros de 2 pts intentados = 80 - 48 = 32
FGM = 35
FG3M = 12
⇒ Tiros de 2 pts encestados = 35 - 12 = 23
% de 2 pts = 23 / 32 = 0.719 (71.9%)
"""
dft_chi1['fg3a'] = dfp['fg3a']
dft_chi1['fg2a'] = dft_chi1['fga'] - dft_chi1['fg3a']
dft_chi1['fg3m'] = dfp['fg3m']
dft_chi1['fg2m'] = dft_chi1['fgm'] - dft_chi1['fg3m']

print(dft_chi1.head(5))

# b) Haciendo uso de query
dft_chi2 = dfp.query("team == 'CHI'")[['team', 'date', 'pts', 'fgm', 'fga']]

print(dft_chi2.head(5))