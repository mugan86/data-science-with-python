## Debe de ser la raíz donde está el directorio donde no encontremos, en este caso fuera de "code"
PROJECT_PATH = "./code-basketball-files/"
DATA_DIR = "data/"

from os import path

filePath = path.join(PROJECT_PATH, DATA_DIR, "shot.csv")
print("Buscando en:", filePath)

with open(filePath, "r", encoding="utf-8") as f:
    contentData = f.read()
print(contentData)

