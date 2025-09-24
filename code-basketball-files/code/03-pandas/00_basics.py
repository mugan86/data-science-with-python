from os import path
import pandas as pd
from project.config import get_file_path, FileExtension, Project

# Ejecutamos con 
# python3 -m code-basketball-files.code.03-pandas.00_basics

filePath = get_file_path("shot", FileExtension.CSV, Project.BASKETBALL)
print("Buscando en:", filePath)

##############
# Loading data
##############
shots = pd.read_csv(filePath)

print(type(shots))

##################################
# DataFrame methods and attributes
##################################
print(shots.head())

print(shots.columns)

print(f'Number rows and columns: {shots.shape}')

#################################
# Working with subsets of columns
#################################
# A single column (5 items for default from start)
print(shots['name'].head())

type(shots['name'])

shots['name'].to_frame().head()
type(shots['name'].to_frame().head())

# Multiple columns
shots[['name', 'dist', 'value', 'made']].head()

type(shots[['name', 'dist', 'value', 'made']].head())

# commented out because it throws an error
# shots['name', 'dist', 'value', 'made'].head() 

##########
# Indexing
##########
shots[['name', 'dist', 'value', 'made']].head()

shots.set_index('shot_id').head()

# Copies and the inplace argument
shots.head()  # note: player_id not the index, even though we just set it

shots.set_index('shot_id', inplace=True)
shots.head()  # now player_id is index

# alternate to using inplace, reassign adp
# reload shots with default 0, 1, ... index
shots = pd.read_csv(get_file_path("shots", FileExtension.CSV, Project.BASKETBALL))
shots = shots.set_index('shot_id')
shots.head()  # now shot_id is index

shots.reset_index().head()

#############################
# Indexes keep things aligned
#############################
shots_ot = shots.loc[shots['period'] > 4, ['name', 'dist', 'value']]
shots_ot.head()

shots_ot.sort_values('name', inplace=True)
shots_ot.head()

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

