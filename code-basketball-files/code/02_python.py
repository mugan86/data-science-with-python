#######
# loops
#######
print("############## LOOPS ##############\n")

#################
# Looping over a list
#################

roster_list = ['kevin durant', 'james harden', 'kyrie irving']

# Crear una lista vacía para almacenar los nombres capitalizados
roster_list_upper = ['', '', '']

# Usando un bucle for con índice manual
i = 0
for player in roster_list:
    roster_list_upper[i] = player.title()  # Convierte cada nombre a Title Case, todas las palabras empiezan por mayúscula
    i += 1  # Incrementa el índice
print("Roster list capitalized:", roster_list_upper)

# Alternativa más pythonica usando list comprehension
roster_list_upper2 = [player.title() for player in roster_list]
print("Roster list capitalized (list comprehension):", roster_list_upper2)

#################
# Looping over a dictionary
#################

roster_dict = {
    'PF': 'kevin durant',
    'SG': 'kyrie irving',
    'PG': 'james harden',
    'C': 'deandre jordan'
}

# Iterar sobre las claves del diccionario
print("\nPositions only:")
for position in roster_dict:
    print(f"position: {position}")

# Iterar sobre las claves y acceder al valor manualmente
print("\nPositions and players (access via key):")
for position in roster_dict:
    print(f"position: {position}")
    print(f"player: {roster_dict[position]}")

# Iterar directamente sobre los pares clave-valor
print("\nPositions and players (using items()):")
for position, player in roster_dict.items():
    print(f"position: {position}")
    print(f"player: {player}")


#######
# loops - advanced
#######
print("############## LOOPS ADVANCED ##############\n")

#################
# Looping over a list with enumerate()
#################

roster_list = ['kevin durant', 'james harden', 'kyrie irving']

# enumerate devuelve índice y valor al mismo tiempo
print("Using enumerate():")
for i, player in enumerate(roster_list):
    print(f"Player {i+1}: {player.title()}")

#################
# Using break and continue
#################

print("\nUsing break and continue:")
for player in roster_list:
    if player == 'james harden':
        print("Found James Harden! Stopping loop.")
        break  # sale del loop al encontrar James Harden
    if player == 'kyrie irving':
        print("Skipping Kyrie Irving")
        continue  # salta esta iteración
    print("Processing player:", player.title())

#################
# Nested loops
#################

teams = [
    {'name': 'Team A', 'players': ['kevin durant', 'kyrie irving']},
    {'name': 'Team B', 'players': ['james harden', 'deandre jordan']}
]

print("\nNested loops over teams and their players:")
for team in teams:
    print(f"Team: {team['name']}")
    for player in team['players']:
        print(f"  Player: {player.title()}")

#################
# Looping over dictionary with conditions
#################

roster_dict = {
    'PF': 'kevin durant',
    'SG': 'kyrie irving',
    'PG': 'james harden',
    'C': 'deandre jordan'
}

print("\nLooping over dict with conditions:")
for position, player in roster_dict.items():
    if 'james' in player:
        print(f"Skipping {player.title()}")
        continue
    print(f"Position: {position}, Player: {player.title()}")

################
# comprehensions
################

print("############## COMPREHENSIONS ##############\n")

#################
# LIST COMPREHENSIONS
#################

roster_list = ['kevin durant', 'james harden', 'kyrie irving']

# Crear nueva lista con nombres capitalizados
roster_list_proper = [x.capitalize() for x in roster_list]
print("Roster capitalized:", roster_list_proper)

# Alternativa con otro nombre de variable en el for
roster_list_proper_alt = [y.title() for y in roster_list]
print("Roster capitalized (title):", roster_list_proper_alt)

# Tipo de una list comprehension
print("Type:", type([x.title() for x in roster_list]))

# Slice sobre el resultado de una comprehension
print("First two players capitalized:", [x.title() for x in roster_list][:2])

# Obtener solo los apellidos
roster_last_names = [full_name.split(' ')[1] for full_name in roster_list]
print("Last names:", roster_last_names)

# Ejemplo simple de split
full_name = 'kevin durant'
print("Full name split:", full_name.split(' '))
print("Last name only:", full_name.split(' ')[1])

# Filtrar solo jugadores cuyo nombre empieza con 'k'
roster_k_only = [x for x in roster_list if x.startswith('k')]
print("Players starting with 'k':", roster_k_only)

# Mismo filtro pero capitalizando nombres
roster_k_only_title = [x.title() for x in roster_list if x.startswith('k')]
print("Players starting with 'k' (capitalized):", roster_k_only_title)


#################
# DICT COMPREHENSIONS
#################

salary_per_player = {
    'kevin durant': 39058950,
    'kyrie irving': 33460350,
    'james harden': 41254920
}

# Crear diccionario con nombre en mayúsculas y salario en millones
salary_m_per_upper_player = {
    name.upper(): salary / 1_000_000
    for name, salary in salary_per_player.items()
}
print("Salary in millions per player (upper names):", salary_m_per_upper_player)

# Sumar valores simples con sum()
print("Sum of [1, 2, 3]:", sum([1, 2, 3]))

# Sumar salarios de todos los jugadores
total_salary = sum([salary for _, salary in salary_per_player.items()])
print("Total salary of roster:", total_salary)


###########
# functions
###########
len(['kevin durant', 'james harden', 'kyrie irving'])

pts_per_3 = len(['kevin durant', 'james harden', 'kyrie irving'])
pts_per_3

4 + len(['kevin durant', 'james harden', 'kyrie irving'])

def pts(fg2, fg3, ft):
    """
    multi line strings in python are between three double quotes

    it's not required, but the convention is to put what the fn does in one of these multi line strings (called "docstring") right away in function

    this function takes number of 2 point fgs, 3 point fgs, and free throws and
    returns total points scored
    """
    return fg2*2 + fg3*3 + ft*1


# this gives an error: fg2 is only defined inside pts
# print(fg2)

def pts_noisy(fg2, fg3, ft):
    """
    this function takes number of 2 point fgs, 3 point fgs, and free throws and
    returns total points scored

    it also prints out fg2
    """
    print(fg2)  # works here since we're inside fn
    return fg2*2 + fg3*3 + ft*1

pts_noisy(8, 4, 5)

# side effects
def is_player_on_team(player, team):
    """
    take a player string and team list and check whether the player is on team

    do this by adding the player to the team, then returning True if the player shows up 2 or more times
    """
    team.append(player)
    return team.count(player) >= 2

roster_list = ['kevin durant', 'james harden', 'kyrie irving']
is_player_on_team('jared dudley', roster_list)

roster_list
is_player_on_team('jared dudley', roster_list)

roster_list

# function arguments
## Positional vs Keyword Arguments

pts(8, 4, 5)
pts(8, 5, 4)  # order matters!

# pts?

pts(fg3=4, fg2=8, ft=5)  # keyword arguments
pts(8, 4, ft=5)

# error: keyword arguments can't come before positional arguments
# pts(ft=5, 8, 4)

## Default Values for Arguments

# error: leaving off a an argument
# pts(4, 2)

def pts_w_default(fg2, fg3, ft=0):
    """
    this function takes number of 2 point fgs, 3 point fgs, and free throws and
    returns total points scored
    """
    return fg2*2 + fg3*3 + ft*1

pts_w_default(8, 4)

# error: leaving out required argument
# pts_w_default(8)

# error: required arguments need to come first
# def pts_w_default_wrong(fg2=0, fg3, ft=0):
#     """
#     this function takes number of 2 point fgs, 3 point fgs, and free throws and
#     returns total points scored
#     """
#     return fg2*2 + fg3*3 + ft*1

#####################################
# functions that take other functions
#####################################

def do_to_list(working_list, working_fn, desc):
    """
    this function takes a list, a function that works on a list, and a
    description

    it applies the function to the list, then returns the result along with
    description as a string
    """

    value = working_fn(working_list)

    return f'{desc} {value}'

def last_elem_in_list(working_list):
    """
    returns the last element of a list.
    """
    return working_list[-1]

positions = ['C', 'PF', 'SF', 'SG', 'PG']

do_to_list(positions, last_elem_in_list, "last element in your list:")
do_to_list([1, 2, 4, 8], last_elem_in_list, "last element in your list:")

do_to_list(positions, len, "length of your list:")

do_to_list([2, 3, 7, 1.3, 5], lambda x: 3*x[0], "first element in your list times 3 is:")

# normally imports like this would be at the top of the file
import os

os.cpu_count()

from os import path

# change this to the location of your data
DATA_DIR = '/Users/nathan/nba-book/data'
path.join(DATA_DIR, 'shot.csv')
os.path.join(DATA_DIR, 'shot.csv')  # alt if we didn't want to import path
