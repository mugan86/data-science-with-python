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