from enum import Enum
from os import path

class Project(Enum):
    BASKETBALL = "./code-basketball-files/"
    FOUNDATIONS = "./data-analysis-foundations-with-python/"

class FileExtension(Enum):
    CSV = ".csv"
    JSON = ".json"
    TXT = ".txt"

# Nombre fijo de la subcarpeta de datos
DATA_DIR = "data/"

def get_file_path(
    filename: str,
    extension: FileExtension,
    project: Project = Project.BASKETBALL
) -> str:
    """
    Construye la ruta completa de un fichero dentro de la carpeta 'data'
    de un proyecto dado.
    """
    return path.join(project.value, DATA_DIR, filename + extension.value)
