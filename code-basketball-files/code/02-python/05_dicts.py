print("############## DICTS ##############")



#################
# container types
#################



#################
# dicts
#################

# Diccionario de jugadores por posición
roster_dict = {
    'PF': 'kevin durant',   # Power Forward
    'SG': 'kyrie irving',   # Shooting Guard
    'PG': 'james harden'    # Point Guard
}

print("Roster inicial", roster_dict)

# Acceder a un valor mediante su clave
print("PF player:", roster_dict['PF'])

# Añadir un nuevo jugador a una posición nueva
print("Añadir como 'C' a 'deandre jordan'")
roster_dict['C'] = 'deandre jordan'  # Center
print("Updated roster:", roster_dict)

# Usar una variable como clave
pos = 'PF'
print(f"Player at position {pos}:", roster_dict[pos])

#################
# unpacking (desempaquetado)
#################

# Desempaquetado correcto de lista
sg, pg = ['kyrie irving', 'james harden']
print("Shooting Guard:", sg)
print("Point Guard:", pg)

# Otra forma explícita, asignando directamente
sg = 'kyrie irving'
pg = 'james harden'
print("Shooting Guard (direct):", sg)
print("Point Guard (direct):", pg)

# ❌ Ejemplo de error: número de variables no coincide con número de items en la lista
# sg, pg = ['kevin durant', 'kyrie irving', 'james harden']  # commented out w/ error
# Esto lanzaría: ValueError: too many values to unpack (expected 2)

#################
# unpacking avanzado con *
#################
# Podemos capturar el resto de los elementos con *
players = ['kevin durant', 'kyrie irving', 'james harden', 'deandre jordan']
first, *rest = players
print("\nFirst player:", first)
print("Rest of players:", rest)

# Desempaquetar al final
*first_players, last_player = players
print("All but last:", first_players)
print("Last player:", last_player)