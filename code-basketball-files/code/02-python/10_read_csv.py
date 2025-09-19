

# normally imports like this would be at the top of the file
import os

os.cpu_count()


import pandas as pd
from os import path

print('hello')

print(pd.__version__)

## Debe de ser la raíz donde está el directorio donde no encontremos, en este caso fuera de "code"
PROJECT_PATH = "./code-basketball-files/"
DATA_DIR = "data/"

# normally imports like this would be at the top of the file
import os

os.cpu_count()

from os import path

ruta_fichero = path.join(PROJECT_PATH, DATA_DIR, "shot.csv")
print("Buscando en:", ruta_fichero)

with open(ruta_fichero, "r", encoding="utf-8") as f:
    contenido = f.read()
print(contenido)

