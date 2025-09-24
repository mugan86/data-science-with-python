
from project.config import get_file_path, FileExtension

# Ejecutamos con 
# python3 -m code-basketball-files.code.02-python.10_read_csv

filePath = get_file_path("shot", FileExtension.CSV)
print("Buscando en:", filePath)

with open(filePath, "r", encoding="utf-8") as f:
    contentData = f.read()
print(contentData)

