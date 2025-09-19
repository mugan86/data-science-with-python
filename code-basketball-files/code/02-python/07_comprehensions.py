

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
    name.title(): round(salary / 1_000_000, 2)
    for name, salary in salary_per_player.items()
}
print("Salary in millions per player (upper names):", salary_m_per_upper_player)

# Sumar valores simples con sum()
print("Sum of [1, 2, 3]:", sum([1, 2, 3]))

# Sumar salarios de todos los jugadores
total_salary = sum([salary for _, salary in salary_per_player.items()])
print("Total salary of roster:", total_salary)