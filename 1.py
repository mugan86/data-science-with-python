import pandas as pd
from os import path

print('hello')

print(pd.__version__)

PROJECT_PATH = "/Users/anartz/Documents/GitHub/code-with-basketball/code-basketball-files/"
DATA_DIR = "data/"

df = pd.read_csv(path.join(PROJECT_PATH,DATA_DIR, "shot.csv"))
print(df.head(2))
