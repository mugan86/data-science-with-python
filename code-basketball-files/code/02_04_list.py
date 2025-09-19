# Lists (listas)
print("############## LISTS ##############")

roster_list = ['kevin durant', 'kyrie irving', 'james harden']

print(f'Lista de jugadores: {roster_list}')

# Acceder al primer elemento (índice 0)
first_player = roster_list[0]
print("First player:", first_player)

# Acceder a un slice: los dos primeros elementos
first_two_players = roster_list[0:2]  # Toma índices 0 y 1 (el 2 no se incluye)
print("First two players:", first_two_players)

# Acceder a los últimos dos elementos usando índices negativos
last_two_players = roster_list[-2:]  # -2 es el penúltimo, ':' indica hasta el final
print("Last two players:", last_two_players)
