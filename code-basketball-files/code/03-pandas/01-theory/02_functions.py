import pandas as pd
from project.config import get_file_path, FileExtension, Project

# Ejecutamos con 
# python3 -m code-basketball-files.code.03-pandas.01-theory.02_functions

# Página 74 Ejercicio 1: Cargar los datos "games.csv". Esto lo usaremos para los siguientes puntos

# load player-game data

filePath = get_file_path("player_game", FileExtension.CSV, Project.BASKETBALL)
print("Find Path:", filePath)

pg = pd.read_csv(filePath)

## Convierte a string algunos datos
pg[['game_id', 'player_id', 'date']] = (
    pg[['game_id', 'player_id', 'date']].astype(str))

# book picks up here:
print('Media de los siguientes datos:')
print(pg[['fgm', 'fga', 'fg_pct', 'pts', 'fg3m', 'fg3a', 'fg3_pct']].mean())

## Devuelve el máximo de cada campo independientemente a quien corresponda
# Z. Willianson es último nombre el máximo por ejemplo, al ser un string coge de manera alfabética el último
print(pg[['name', 'fgm', 'fga', 'pts', 'fg3m', 'fg3a']].max())

# Muestra lo de todos los campos
print(pg.max())

# Axis
# axis = 0 => columnas / axis = 1 => filas. Por defecto = 0
# con esto haremos los cálculos por columnas (0 por defecto) o por filas (1)
# -----------------------------------------------
# axis en pandas:
# - axis=0 => operaciones por columnas (por defecto)
#   * Recorre hacia abajo, fila por fila
#   * Ejemplo: df.mean(axis=0) devuelve la media de cada columna
#     (media de todos los pts, media de todos los ast, etc.)
#
# - axis=1 => operaciones por filas
#   * Recorre hacia la derecha, columna por columna
#   * Ejemplo: df.mean(axis=1) devuelve la media de cada fila
#     (para un jugador, promedio de sus pts, ast, stl y reb)
#
# Ejemplo práctico con axis=1:
#   Si un jugador tiene:
#       pts = 18, ast = 8, stl = 1, reb = 10
#   Entonces:
#       (18 + 8 + 1 + 10) / 4 = 9.25
#   → el valor de esa fila en df.mean(axis=1) será 9.25
#
# En resumen:
# - axis=0 → un resultado por columna (estadísticas globales)
# - axis=1 → un resultado por fila (estadísticas de cada jugador)
# -----------------------------------------------
print('Estadísticas pts, ast, stl, reb columnas')
print(pg[['pts', 'ast', 'stl', 'reb']].mean(axis=0)) # No sería necesario poner axis = 0, por ser por defecto
print('Estadísticas pts, ast, stl, reb filas, en este caso, suma estos valores por jugador y / 4')
print(pg[['pts', 'ast', 'stl', 'reb']].mean(axis=1).head())


# ----------------------------------------------------------
# Operaciones lógicas y booleanas en pandas
#
# ----------------------------------------------------------
# 1) Crear columnas booleanas:
#    pg['cold_shooting'] = (pg['fga'] > 10) & (pg['pts'] < 5)
#    → True si un jugador tiró más de 10 veces y anotó < 5 puntos
pg['cold_shooting'] = (pg['fga'] > 10) & (pg['pts'] < 5)

#
# 2) mean() y sum() sobre booleanos:
#    - .mean() → porcentaje de True (ej: % jugadores con mal tiro, mostrado con valores de entre 0 y 1. Si queremos de 0 a 100 como % * 100)
#    - .sum()  → número total de True (ej: cuántos jugadores con mal tiro)
#
print('% jugadores con mal tiro (0 a 1): ', pg['cold_shooting'].mean())
print(f'% jugadores con mal tiro: {pg["cold_shooting"].mean()*100:.2f} %')
print('Número de jugadores con mal tiro: ', pg['cold_shooting'].sum())


# 3) any() y all():
#    - .any() → ¿existe al menos un True?
#       (pg['fg3a'] > 30).any() → ¿alguno intentó >30 triples?
#    - .all() → ¿todos son True?
#       (pg['min'] > 0).all() → ¿todos jugaron más de 0 min?
#   Aquí, como no se especifica el axis, hace el escaneo de arriba a abajo, en la columna seleccionada
#   que en este caso es 'fg3a'
#

print('¿Alguien ha intentado 30 triples en un partido?', (pg['fg3a'] > 30).any())
print('¿Alguien ha intentado 20 triples en un partido?', (pg['fg3a'] > 20).any())
print('¿Alguien ha intentado 10 triples en un partido?', (pg['fg3a'] > 10).any())


print('¿todos jugaron más de 0 min?', (pg['min'] > 0).all())

# 4) Comparaciones múltiples por filas:
#    (pg[['pts','ast','reb','stl','blk']] >= 10).any(axis=1)
#    → True si el jugador llegó a 10 en al menos una de esas categorías
#
pg['hit_10'] = (pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10).any(axis=1)

print('10 en puntos (pts), asistencias (ast), rebotes (reb), robos (stl) o tapones (blk)')
print(pg[['name', 'pts', 'ast', 'reb', 'stl', 'blk', 'hit_10']].head(15))

"""
RESULTADO
---------
                name  pts  ast  reb  stl  blk  hit_10
0           L. James   18    8   10    1    1    True
1          D. Howard    3    1    6    0    1   False
2        L. Williams   21    7    5    1    0    True
3          J. Dudley    6    0    0    0    0   False
4           J. McGee    4    0    2    0    2   False
5        P. Beverley    2    6   10    0    1    True
6           D. Green   28    0    7    2    1    True
7       P. Patterson    4    0    3    0    0   False
8         A. Bradley    8    0    3    0    0   False
9         K. Leonard   30    5    6    2    1    True
10          A. Davis   25    5    9    1    2    True
11       M. Harkless   10    0    4    4    2    True
12          J. Green   12    0    6    0    0    True
13  K. Caldwell-Pope    0    3    3    0    0   False
14        T. Daniels    6    1    0    0    0   False
"""

# 5) Triple-doble:
#    pg['triple_double'] = ((pg[['pts','ast','reb','stl','blk']] >= 10)
#                            .sum(axis=1) >= 3)
#    → cuenta cuántas categorías tienen >=10
#    → si son 3 o más, marca True = triple-doble

pg['triple_double'] = ((pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10)
                       .sum(axis=1) >= 3)
pg['double_double'] = ((pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10)
                       .sum(axis=1) == 2)

print('Doble doble / Triple doble con puntos (pts), asistencias (ast), rebotes (reb), robos (stl) o tapones (blk)')
print(pg[['name', 'pts', 'ast', 'reb', 'stl', 'blk', 'double_double', 'triple_double']].head(30))

#
# 6) Ejemplo resumen:
#    (pg[['pts','ast','reb','stl','blk']] >= 10).head()
#       → muestra True/False por jugador y categoría
#    (pg[['pts','ast','reb','stl','blk']] >= 10).sum(axis=1).head()
#       → cuántas categorías con >=10 tiene cada jugador
#    ((pg[['pts','ast','reb','stl','blk']] >= 10).sum(axis=1) >= 3).head()
#       → True si ese jugador hizo triple-doble
#
print("10 o más en las categorías de 'pts', 'ast', 'reb', 'stl', 'blk'")
print((pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10).head())
# Comparación sobre las columnas numéricas
bool_df = (pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10)

# Agregar columna de nombres para mostrar
print(pd.concat([pg['name'], bool_df], axis=1).head())

## Indica en cuantos apartados hay 10 o más como valor (almacenar en "bool_sum_10_values_in_fields")
pg['bool_sum_10_values_in_fields'] = (pg[['pts', 'ast', 'reb', 'stl', 'blk']] >= 10).sum(axis=1)
print(pg[['name', 'bool_sum_10_values_in_fields']].head())
"""
RESULTADO
----
          name  bool_sum_10_values_in_fields
0     L. James                             2
1    D. Howard                             0
2  L. Williams                             1
3    J. Dudley                             0
4     J. McGee                             0
"""

print('Jugadores y saber si han hecho triple doble')
print(pg[['name', 'pts', 'ast', 'reb', 'stl', 'blk', 'triple_double']].head(25))

# 7) Contar triple-dobles totales:
#    pg['triple_double'].sum() → número de jugadores con triple-doble
print('Jugadores que han hecho triple doble: ', pg['triple_double'].sum())

# Otras funciones útiles
# ----------------------------------------------------------
# Resumen de conteos y proporciones en pandas
#
# 1) value_counts()
#    pg['pos'].value_counts()
#    → Cuenta cuántas veces aparece cada valor único en la columna 'pos'
#    Ejemplo:
#       Guard   800
#       Forward 700
#       Center  614
#
print('Mostrar apariciones de los puestos de manera única, para contabilizar total de jugadores en las posiciones')
print(pg['pos'].value_counts())

# 2) value_counts(normalize=True)
#    pg['pos'].value_counts(normalize=True)
#    → Devuelve proporciones en lugar de conteos
#    Ejemplo:
#       Guard    0.38  # 38% de los registros
#       Forward  0.33
#       Center   0.29
#
print('Mostrar apariciones (en proporciones) de los puestos de manera única, para contabilizar total de jugadores en las posiciones')

print((pg['pos'].value_counts(normalize=True))*100)

print('Comprobar que coge el muestre completo: ', ((pg['pos'].value_counts(normalize=True))*100).sum(), ' %')

# 3) pd.crosstab()
#    pd.crosstab(pg['team'], pg['pos']).head()
#    → Tabla de contingencia cruzando 'team' y 'pos'
#       Cada celda = número de registros con esa combinación
#    Ejemplo:
#       pos    Guard  Forward  Center
#       team
#       LAL      200      180     150
#       LAC      180      160     130
#
print(pd.crosstab(pg['team'], pg['pos']).head(30))

# 4) pd.crosstab() con normalize
#    - normalize=True      → proporción sobre total general
#    - normalize='index'   → proporción por fila (por equipo)
#    - normalize='columns' → proporción por columna (por posición)
#    Ejemplo interpretación:
#       normalize='index': porcentaje de posiciones dentro de cada equipo
#       normalize='columns': porcentaje de equipos dentro de cada posición
# ----------------------------------------------------------

print(pd.crosstab(pg['team'], pg['pos'], normalize=True))       # proporción total
print(pd.crosstab(pg['team'], pg['pos'], normalize='index') )    # proporción por fila (equipo)
print(pd.crosstab(pg['team'], pg['pos'], normalize='columns'))   # proporción por columna (posición)