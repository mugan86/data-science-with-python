import pandas as pd

# Ejecutamos con 
# python3 -m 1

print('hello')

print(pd.__version__)

from project.config import get_file_path, FileExtension

filePath = get_file_path("shot", FileExtension.CSV)
print("Buscando en:", filePath)


df = pd.read_csv(filePath)
print(df.head(2))
