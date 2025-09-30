import pandas as pd
from project.config import get_file_path, FileExtension, Project

# Ejecutamos con 
# python3 -m code-basketball-files.code.03-pandas.02-exercises.01_columns

# Página 86 Ejercicio 1: Cargar los datos "player_game.csv". Esto lo usaremos para los siguientes puntos

filePath = get_file_path("player_game", FileExtension.CSV, Project.BASKETBALL)
print("Find Path:", filePath)

##############
# Loading data
##############

print("========== LOADING DATA AND TAKE TYPE ==========")
player_game = pd.read_csv(filePath)
print(player_game.head(3))

## Página 86 Ejercicio 2: Añadir una nueva columna llamada "net_takeaways" cuyos valores se almacenan desde robos - perdidas (stl - tov)

player_game['net_takeaways'] = player_game['stl'] - player_game['tov']

print(player_game[['name', 'pts', 'stl', 'tov', 'net_takeaways']].head(4))

"""
          name  pts  stl  tov  net_takeaways
0     L. James   18    1    5             -4
1    D. Howard    3    0    0              0
2  L. Williams   21    1    2             -1
3    J. Dudley    6    0    0              0
"""

## Página 86 Ejercicio 3: Crear una columna llamada 'player_desc' donde añadimos una descripción del jugador.
## Por ejemplo player_desc = {name} is the {team} {pos}

player_game['player_desc'] = player_game['name'] + ' is the ' + player_game['team'] + ' ' + player_game['pos']

print(player_game[['player_desc']].sample(10))

"""
                          player_desc
1954    A. Johnson is the IND Forward
1043     J. Randle is the NYK Forward
130       A. Holiday is the IND Guard
394          B. Beal is the WAS Guard
373    M. Harkless is the LAC Forward
533   M. Frazier Jr. is the ORL Guard
787       D. Green is the GSW Forward
179       R. Gobert is the UTA Center
1851   D. Robinson is the MIA Forward
549   D. Jones Jr. is the MIA Forward
"""

## Página 86 Ejercicio 4: Añadir columna llamada 'bad_game' de tipo boolean indicando que se han tomado más de 20 tiros y menos de 15 puntos. 
## Con eso, se va a considerar que es un mal partido
player_game['bad_game'] = (player_game['fga'] > 20 ) & (player_game['pts'] < 15)

print(player_game[['name', 'pts', 'fga', 'bad_game']].tail(10))

## Extra Gran partido (valoración)

## Valoración=PTS+REB+AST+STL+BLK−(FGA−FGM)−(FTA−FTM)−TOV

player_game['eff'] = (
    player_game["pts"]
    + player_game["reb"]
    + player_game["ast"]
    + player_game["stl"]
    + player_game["blk"]
    - (player_game["fga"] - player_game["fgm"])
    - (player_game["fta"] - player_game["ftm"])
    - player_game["tov"]
)

print(player_game[['name', 'pts', 'fga', 'eff']].head(10))
"""
           name  pts  fga  eff
0      L. James   18   19    0
1     D. Howard    3    3    5
2   L. Williams   21   14    2
3     J. Dudley    6    2    2
4      J. McGee    4    3    2
5   P. Beverley    2    7    9
6      D. Green   28   14   12
7  P. Patterson    4    3    0
8    A. Bradley    8    7   -1
9    K. Leonard   30   19  -10
"""

## Aplicando columnas con función
def rating(eff):
    if eff <= 5:
        return "Malo"
    elif eff <= 15:
        return "Normal"
    elif eff <= 25:
        return "Bueno"
    elif eff <= 35:
        return "Excelente"
    elif eff <= 45:
        return "Estrella"
    else:
        return "Nivel MVP"

player_game["rating"] = player_game["eff"].apply(rating)


## Coger los 10 primeros desde el más eficiente
fields = ["name", "pts", "reb", "ast", "stl", "blk", "fga", "fgm", "fta", "ftm", "tov", "eff", "rating"]

print(player_game.sort_values("eff", ascending=False)[fields].head(30))
"""
                  name  pts  reb  ast  stl  blk  fga  fgm  fta  ftm  tov  eff     rating
1940         J. Harden   45   17    9    3    0   21   13   14   12    6   58  Nivel MVP
50            A. Davis   40   20    2    0    2   17    7   27   26    0   53  Nivel MVP
1566        D. Lillard   45    4   12    3    0   21   13   10    8    2   52  Nivel MVP
136         N. Vucevic   30   17    6    0    1   14   11    5    5    3   48  Nivel MVP
1987        D. Lillard   42    3   12    2    0   22   13    9    8    1   48  Nivel MVP
2008    J. Valanciunas   26   19   12    0    0   17   11    2    2    3   48  Nivel MVP
678           J. Tatum   41    6    4    3    0   22   16    3    3    0   48  Nivel MVP
1587         J. Harden   39    8   12    3    1   19   11   12   12   10   45   Estrella
1749        D. Lillard   51    3    7    2    0   28   16   16   15    6   44   Estrella
1255         T. Warren   34   11    4    3    4   26   14    5    5    0   44   Estrella
1229         L. Doncic   40    8   11    0    0   20   11   19   18    6   43   Estrella
1317          A. Davis   42   12    4    3    1   28   13   15   12    1   43   Estrella
629        A. Drummond   23   20    5    1    2   12    8    9    7    3   42   Estrella
359         B. Simmons   34    3    7    1    2   14   12   12    9    1   41   Estrella
329           A. Davis   39    9    2    2    3   21   12   15   13    3   41   Estrella
827           K. Lowry   32    8   10    2    0   21   12    5    5    3   40   Estrella
725          L. Doncic   25   15   17    0    0   18    8   10    9    6   40   Estrella
1147          K. Lowry   33   14    6    1    0   16    8   15   12    4   39   Estrella
943          A. Gordon   25   10    6    1    3   14    9    4    4    1   39   Estrella
956        A. Drummond   27   13    4    4    1   21   12    3    3    1   39   Estrella
1505      K. Middleton   33    6    8    0    0   14    9   10   10    3   39   Estrella
1505      K. Middleton   33    6    8    0    0   14    9   10   10    3   39   Estrella
302          A. Gordon   32    5    5    1    0   15   13    2    1    1   39   Estrella
302          A. Gordon   32    5    5    1    0   15   13    2    1    1   39   Estrella
1507  G. Antetokounmpo   33   12    4    0    1   17   13    9    7    6   38   Estrella
1507  G. Antetokounmpo   33   12    4    0    1   17   13    9    7    6   38   Estrella
669          E. Kanter   22   19    1    0    0   13   10    2    2    1   38   Estrella
2089           T. Mann   25   14    9    2    0   12    8   13    8    3   38   Estrella
1726        G. Hayward   31    9    5    0    1   18   12    6    5    1   38   Estrella
880          A. Gordon   25    9    9    1    1   15    8    6    6    1   37   Estrella
1138          D. Ayton   24   12    3    0    2   14   11    0    0    1   37   Estrella
669          E. Kanter   22   19    1    0    0   13   10    2    2    1   38   Estrella
2089           T. Mann   25   14    9    2    0   12    8   13    8    3   38   Estrella
1726        G. Hayward   31    9    5    0    1   18   12    6    5    1   38   Estrella
880          A. Gordon   25    9    9    1    1   15    8    6    6    1   37   Estrella
1138          D. Ayton   24   12    3    0    2   14   11    0    0    1   37   Estrella
891           R. Rubio   22    6   11    7    0   13    6    9    8    1   37   Estrella
2089           T. Mann   25   14    9    2    0   12    8   13    8    3   38   Estrella
1726        G. Hayward   31    9    5    0    1   18   12    6    5    1   38   Estrella
880          A. Gordon   25    9    9    1    1   15    8    6    6    1   37   Estrella
1138          D. Ayton   24   12    3    0    2   14   11    0    0    1   37   Estrella
891           R. Rubio   22    6   11    7    0   13    6    9    8    1   37   Estrella
1726        G. Hayward   31    9    5    0    1   18   12    6    5    1   38   Estrella
880          A. Gordon   25    9    9    1    1   15    8    6    6    1   37   Estrella
1138          D. Ayton   24   12    3    0    2   14   11    0    0    1   37   Estrella
891           R. Rubio   22    6   11    7    0   13    6    9    8    1   37   Estrella
880          A. Gordon   25    9    9    1    1   15    8    6    6    1   37   Estrella
1138          D. Ayton   24   12    3    0    2   14   11    0    0    1   37   Estrella
891           R. Rubio   22    6   11    7    0   13    6    9    8    1   37   Estrella
891           R. Rubio   22    6   11    7    0   13    6    9    8    1   37   Estrella
1177         J. Nurkic   30    9    5    2    1   20   12    5    5    2   37   Estrella
"""

## Página 86: Obtener la longitud del lastname en el nombre del jugador (len_last_name)

# player_game['len_last_name'] = len((player_game['name'].str.split(' '))[:-1])
player_game['len_last_name'] = (player_game["name"].apply(lambda x: x.split(" ")[-1])).apply(len)

print(player_game[['name', 'len_last_name']].head())

"""
          name  len_last_name
0     L. James              5
1    D. Howard              6
2  L. Williams              8
3    J. Dudley              6
4     J. McGee              5
"""

## Página 86 Ejercicio 6: Convertir game_id a string

player_game['game_id'] = player_game["game_id"].astype(str).replace("nan", "unknown")

print('Game id convertido a str')
print(player_game['game_id'].head(40))