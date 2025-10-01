import pandas as pd
from project.config import get_file_path, FileExtension, Project

# Ejecutamos con 
# python3 -m code-basketball-files.code.03-pandas.01-theory.03_filter

# note: we're passing the index_col argument, which immediately setting the
# index to be the player_id column

filePath = get_file_path("players", FileExtension.CSV, Project.BASKETBALL)
print("Find Path:", filePath)

dfp = pd.read_csv(filePath, index_col='player_id')

# Filtering
lebron_id = 2544 ## ID de Lebron James
print(dfp.loc[lebron_id])

"""
Datos del filtrado con Lebron James
first                                         LeBron
last                                           James
name                                        L. James
birthdate                                   19841230
school                  St. Vincent-St. Mary HS (OH)
country                                          USA
last_affiliation    St. Vincent-St. Mary HS (OH)/USA
height                                           6-9
weight                                         250.0
season_exp                                        17
jersey                                          23.0
pos                                          Forward
rosterstatus                                  Active
from_year                                     2003.0
dleague_flag                                       N
draft_year                                      2003
draft_round                                      1.0
draft_number                                     1.0
team_id                                   1610612747
team_id2                                           0
team                                             LAL
team2                                            NaN
Name: 2544, dtype: object
"""

laker_ids = ([2544, 203076, 201566])

print('Obtener jugadores de los lakers con todas las columnas')
print(dfp.loc[laker_ids])
"""
Todos los datos filtrando los ids de jugadores de los lakers
             first       last          name  birthdate  ...     team_id team_id2 team team2
player_id                                               ...                                
2544        LeBron      James      L. James   19841230  ...  1610612747        0  LAL   NaN
203076     Anthony      Davis      A. Davis   19930311  ...  1610612747        0  LAL   NaN
201566     Russell  Westbrook  R. Westbrook   19881112  ...  1610612745        0  HOU   NaN
"""

print('Obtener jugadores de los lakers con "name", "school", "height" y "weight"')
print(dfp.loc[laker_ids, ['name', 'school', 'height', 'weight']])

"""
Resultado
                   name                        school height  weight
player_id                                                           
2544           L. James  St. Vincent-St. Mary HS (OH)    6-9   250.0
203076         A. Davis                      Kentucky   6-10   253.0
201566     R. Westbrook                          UCLA    6-3   200.0
"""

print('Obtener jugadores de los lakers con "name"')
print(dfp.loc[laker_ids, 'name'])
"""
RESULTADO
player_id
2544          L. James
203076        A. Davis
201566    R. Westbrook
"""

# Boolean Indexing

# Obtener los jugadores que proceden de North Carolina
school_in_nc = dfp['school'] == 'North Carolina'

print(school_in_nc.head())

# Extraer jugadores que vienen de North Carolina (coge los True)
players_nc = dfp.loc[school_in_nc]

print("Primeros 5 jugadores de la lista que proceden de North Carolina")
print(players_nc[['name', 'school', 'height', 'weight']].head())

# Ahora con la uni de Duke
players_duke = dfp.loc[dfp['school'] == 'Duke']

print("Primeros 5 jugadores de la lista que proceden de Duke")
print(players_duke[['name', 'school', 'height', 'weight']].head())

"""
RESULTADO
                 name school height  weight
player_id                                  
200755      J. Redick   Duke    6-3   200.0
202498      L. Thomas   Duke    6-8   225.0
203085      A. Rivers   Duke    6-4   200.0
203486     M. Plumlee   Duke   6-11   254.0
203552       S. Curry   Duke    6-2   185.0
"""

# Nacidos en USA
from_usa = dfp['country'] == 'USA'

# NO nacidos en usa, usando ~ dentro de loc[~condicion]
players_not_usa = dfp.loc[~from_usa]

print("Primeros 5 jugadores NO nacidos en USA")
print(players_not_usa[['name', 'country', 'height', 'weight']].head())

"""
RESULTADO
                   name             country height  weight
player_id                                                 
101133       I. Mahinmi              France   6-11   262.0
101141      E. Ilyasova              Turkey    6-9   235.0
200757     T. Sefolosha         Switzerland    6-6   215.0
200826         J. Barea         Puerto Rico   5-10   180.0
201143       A. Horford  Dominican Republic    6-9   240.0
"""

# Duplicates
dfp.drop_duplicates(inplace=True)

dfp.drop_duplicates('pos')[['name', 'pos', 'height', 'weight']]

dfp.duplicated().head()

dfp['pos'].duplicated().head()

dfp.drop_duplicates('pos')
dfp.loc[~dfp['pos'].duplicated()]

# Combining filtering with changing columns
dfp['draft_desc'] = ''
dfp.loc[dfp['draft_round'] == 1, 'draft_desc'] = 'first round'
dfp.loc[(dfp['draft_round'] == 1) & (dfp['draft_number'] <= 14), 'draft_desc'] = 'lottery'
dfp.loc[(dfp['draft_round'] == 1) & (dfp['draft_number'] <= 5), 'draft_desc'] = 'top 5'
dfp.loc[dfp['draft_round'] == 2, 'draft_desc'] = 'second round'
dfp.loc[dfp['draft_round'].isnull(), 'draft_desc'] = 'undrafted'

dfp[['name', 'school', 'draft_round', 'draft_number', 'draft_desc']].sample(5)

# Query
dfp.query("school == 'North Carolina'").head()

dfp['school_in_kentucky'] = dfp['school'] == 'Kentucky'

dfp.query("school_in_kentucky").head()

dfp.query("draft_round.isnull()")[['name', 'school', 'draft_round', 'draft_number']].head()

# note: if getting an error on line above, try it with engine='python' like
# this
dfp.query("draft_round.isnull()", engine='python')[['name', 'school', 'draft_round', 'draft_number']].head()
