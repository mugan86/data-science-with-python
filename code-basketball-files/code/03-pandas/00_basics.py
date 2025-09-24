from os import path
import pandas as pd
from project.config import get_file_path, FileExtension, Project

# Ejecutamos con 
# python3 -m code-basketball-files.code.03-pandas.00_basics

filePath = get_file_path("shots", FileExtension.CSV, Project.BASKETBALL)
print("Find Path:", filePath)

##############
# Loading data
##############

print("========== LOADING DATA AND TAKE TYPE ==========")
shots = pd.read_csv(filePath)

print(type(shots))

##################################
# DataFrame methods and attributes
##################################

print("========== DATAFRAME METHODS AND ATTRIBUTES ==========")
print(shots.head())

print(shots.columns)

print(f'Number rows and columns: {shots.shape}')

#################################
# Working with subsets of columns
#################################
print("========== SUBSETS OF COLUMNS ==========")
# A single column (5 items for default from start)
print("----One Column----")
print(shots['name'].head())

print(type(shots['name']))

print(shots['name'].to_frame().head())
print(type(shots['name'].to_frame().head()))

# Multiple columns
print("----Multiple Column----")
shots[['name', 'dist', 'value', 'made']].head()

type(shots[['name', 'dist', 'value', 'made']].head())

# commented out because it throws an error
# shots['name', 'dist', 'value', 'made'].head() 

##########
# Indexing
##########
print("========== INDEXING ==========")

print(shots[['name', 'dist', 'value', 'made']].head(3))

print("--- Asigna como ID 'shot_id' ---")
print("Todas las columnas")
print(shots.set_index('shot_id').head()) # Muestra como Index el shot_id
print("Columnas", 'name', 'dist', 'value', 'made')
print(shots.set_index('shot_id')[['name', 'dist', 'value', 'made']].head()) # Muestra como Index el shot_id

# Copies and the inplace argument
## Muestra los 5 primeros elementos
print("---Usando inplace---")
print('Sin cambiarlo, tenemos el index normal')
print(shots.head())  # note: id not the index, even though we just set it

shots.set_index('shot_id', inplace=True) # inplace fija como id principal shot_id
print('Asignando "shot_id" como index')

print(shots.head())  # now player_id is index

# En vez de usar Inplace, ahora recargamos y volvemos al index normal
# reload shots with default 0, 1, ... index
shots = pd.read_csv(get_file_path("shots", FileExtension.CSV, Project.BASKETBALL))
shots = shots.set_index('shot_id')
shots.head()  # now shot_id is index

## Resetea el index shot_id por el index que viene por defecto con 0,1,2,...
print(shots.reset_index().head())


#############################
# Indexes keep things aligned
#############################
## Lanzamientos en prorroga
"""
#### 🔹 **Filtrar con `.loc[]`**

El método `.loc[]` permite acceder a filas basadas en condiciones:

```python
df_filtered = df.loc[df["Age"] > 28, ["Name", "Salary"]]
print(df_filtered)
```
"""
shots_ot = shots.loc[shots['period'] > 4, ['name', 'dist', 'value']]
print(shots_ot.head())

shots_ot.sort_values('name', inplace=True)
print(shots_ot.head())

# assigning a new column
shots_ot['made'] = shots['made']
shots_ot.head()

# has the same index as shots['made'] and shots['made']
shots['made'].head()

#################
# Outputting data
#################
shots_ot.to_csv(get_file_path("shots_ot", FileExtension.CSV, Project.BASKETBALL))

shots_ot.to_csv(get_file_path("shots_ot_no_index", FileExtension.CSV, Project.BASKETBALL), index=False)

