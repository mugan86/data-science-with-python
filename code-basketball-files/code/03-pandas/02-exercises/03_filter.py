import pandas as pd
from project.config import get_file_path, FileExtension, Project

# Ejecutamos con 
# python3 -m code-basketball-files.code.03-pandas.02-exercises.03_filter

# Página 103 Ejercicio 1: Cargar los datos "team_games.csv". Esto lo usaremos para los siguientes puntos

# load team_games data

filePath = get_file_path("team_games", FileExtension.CSV, Project.BASKETBALL)
print("Find Path:", filePath)