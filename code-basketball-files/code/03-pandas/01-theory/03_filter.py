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
# Añadimos ids que sabemos que corresponde a 3 jugadores de Los Ángeles Lakers
# Lebron James, Anthony Davis y Russel Westbrook
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

# Duplicados: Sirve para eliminar elementos duplicados

"""
drop_duplicates() sin argumento → elimina duplicados comparando toda la fila.

drop_duplicates('col') → elimina duplicados comparando solo esa(s) columna(s).

En ambos casos, se queda con la primera aparición a menos que indiques keep='last' o keep=False.
"""

# Elimina cuando las columnas de una fila, están duplicadas. En este caso, en el fichero no hay duplicados
dfp.drop_duplicates(inplace=True)


# Aquí elimina teniendo en cuenta el campo "pos"
"""
Quédate solo con un jugador por posición (pos).
Luego selecciona esas 4 columnas para mostrar.
"""
dfp_remove_pos_duplicates = dfp.drop_duplicates('pos')[['name', 'pos', 'height', 'weight']]
print('Al eliminar duplicados por "pos", coge los tres primeros de cada uno de esos puestos con los valores seleccionados como name, pos, height y weight')
print(dfp_remove_pos_duplicates)

print("Resultado si globalmente si se diera un duplicado (no hay en el global duplicados) - ")
print("Muestra True en el caso de que se vaya a borrar")
print(dfp.duplicated().head(10))

print("Eliminar duplicados por 'pos', nos dice que se eliminarán con 'True'")
print(dfp['pos'].duplicated().head())

print("Datos sin duplicados por 'pos', es decir, ya se ha borrado los duplicados por 'pos'")
print("En este caso tiene toda las columnas ya que no se ha seleccionado las que queremos")
print(dfp.drop_duplicates('pos'))
 
# Este es equivalente a "dfp.drop_duplicates('pos')"
dfp.loc[~dfp['pos'].duplicated()]

"""
df['pos'].duplicated(keep='first')  # default: marca duplicados menos la primera aparición
df['pos'].duplicated(keep='last')   # marca duplicados menos la última aparición
df['pos'].duplicated(keep=False)    # todas las ocurrencias de duplicados → True
"""

df = pd.DataFrame({"pos": ["PG","PG","SG","SG","PF"]})

print("duplicated (default first):")
print(df['pos'].duplicated())  # default keep='first'

print("\nduplicated (keep='last'):")
print(df['pos'].duplicated(keep='last'))

print("\nduplicated (keep=False):")
print(df['pos'].duplicated(keep=False))

# Confinando filtros con cambios en las columnas
# ================================
# 🔹 Clasificación de jugadores según el Draft
# ================================
# ================================================
# 📌 Uso de .loc en pandas
# Sintaxis: df.loc[condición_filas, columnas]
#
# 1. Antes de la coma → condición booleana para elegir filas.
# 2. Después de la coma → columnas que quiero leer o modificar.
# 3. = valor → asignación del nuevo contenido.
#
# Ejemplo:
# df.loc[df['age'] > 20, 'city'] = 'España'
#
# - Selecciona filas donde age > 20
# - En la columna "city"
# - Asigna el valor "España"
# ================================================

# Creamos una nueva columna vacía llamada 'draft_desc' en todo el DataFrame
dfp['draft_desc'] = ''

# Asignamos "first round" a todos los jugadores seleccionados en la primera ronda
dfp.loc[dfp['draft_round'] == 1, 'draft_desc'] = 'first round'

# Refinamos: si además fueron del pick 1 al 14, los marcamos como "lottery"
dfp.loc[(dfp['draft_round'] == 1) & (dfp['draft_number'] <= 14), 'draft_desc'] = 'lottery'

# Refinamos aún más: si fueron picks del 1 al 5, los marcamos como "top 5"
dfp.loc[(dfp['draft_round'] == 1) & (dfp['draft_number'] <= 5), 'draft_desc'] = 'top 5'

# Jugadores elegidos en segunda ronda → "second round"
dfp.loc[dfp['draft_round'] == 2, 'draft_desc'] = 'second round'

# Jugadores sin datos de draft (NaN en draft_round) → "undrafted"
dfp.loc[dfp['draft_round'].isnull(), 'draft_desc'] = 'undrafted'

# Mostramos una muestra aleatoria de 5 filas con las columnas relevantes
print(dfp[['name', 'school', 'draft_round', 'draft_number', 'draft_desc']].sample(5))

"""
import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "age": [19, 25, 30, 17],
    "group": ""
})

# A todos los mayores de 20 → poner "adult"
df.loc[df['age'] > 20, 'group'] = "adult"

# A todos los menores o iguales de 20 → poner "young"
df.loc[df['age'] <= 20, 'group'] = "young"

print(df)

  name  age  group
0    A   19   young
1    B   25   adult
2    C   30   adult
3    D   17   young
"""

# Query
# ================================================
# 📌 Uso de .query() en pandas
# Permite filtrar filas usando expresiones tipo SQL,
# más legibles que con .loc.
#



#
# ⚠️ Nota: A veces .query() con funciones como isnull()
# requiere especificar el motor de evaluación:
# dfp.query("draft_round.isnull()", engine='python')
#
# 👍 Ventaja: query es más legible que df.loc[condición]
# ================================================

# 🔹 Ejemplo 1: Filtrar por valor exacto
# dfp.query("school == 'North Carolina'")
#
print(dfp.query("school == 'North Carolina'").head())

# 🔹 Ejemplo 2: Crear columna booleana y filtrar con ella
# dfp['school_in_kentucky'] = dfp['school'] == 'Kentucky'
# dfp.query("school_in_kentucky")
dfp['school_in_kentucky'] = dfp['school'] == 'Kentucky'

dfp.query("school_in_kentucky").head()

# 🔹 Ejemplo 3: Filtrar valores nulos con isnull()
# dfp.query("draft_round.isnull()")[['name','school','draft_round','draft_number']]
dfp.query("draft_round.isnull()")[['name', 'school', 'draft_round', 'draft_number']].head()

# note: if getting an error on line above, try it with engine='python' like
# this
dfp.query("draft_round.isnull()", engine='python')[['name', 'school', 'draft_round', 'draft_number']].head()

# ============================================================
# 📌 Comparación entre .loc[] y .query() en pandas
#
# 🔹 Selección por valor exacto
#   con loc   → dfp.loc[dfp['school'] == 'North Carolina']
#   con query → dfp.query("school == 'North Carolina'")
#
# 🔹 Filtrar usando una columna booleana
#   dfp['school_in_kentucky'] = dfp['school'] == 'Kentucky'
#   con loc   → dfp.loc[dfp['school_in_kentucky']]
#   con query → dfp.query("school_in_kentucky")
#
# 🔹 Filtrar valores nulos
#   con loc   → dfp.loc[dfp['draft_round'].isnull(), ['name','school','draft_round','draft_number']]
#   con query → dfp.query("draft_round.isnull()")[['name','school','draft_round','draft_number']]
#
# ⚠️ Nota: Algunas funciones como isnull() pueden dar error en query,
# en ese caso usar → dfp.query("draft_round.isnull()", engine='python')
#
# ✅ Resumen:
# - .loc[] → más flexible, soporta cualquier condición Python.
# - .query() → más legible y corto, estilo SQL, ideal para filtros simples.
# ============================================================
