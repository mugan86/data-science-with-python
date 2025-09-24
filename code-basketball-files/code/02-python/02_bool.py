

#######
# bools
#######

# Puntos de cada equipo
team1_pts = 110
team2_pts = 120

# Comparaciones booleanas básicas
team1_won = team1_pts > team2_pts          # True si el equipo 1 ganó
team2_won = team1_pts < team2_pts          # True si el equipo 2 ganó
teams_tied = team1_pts == team2_pts        # True si los equipos empataron
teams_did_not_tie = team1_pts != team2_pts # True si NO empataron

# Verificar el tipo de dato (bool)
print("Tipo de team1_won:", type(team1_won))

# Mostrar resultado de teams_did_not_tie
print("Teams did not tie:", teams_did_not_tie)

# Error de sintaxis si usamos = en vez de == para comparar
# teams_tied = (team1_pts = team2_pts)

#######
# Condiciones más complejas con operadores lógicos
#######

# Ambos equipos anotaron más de 130 puntos
shootout = (team1_pts > 130) and (team2_pts > 130)
print("Shootout (both > 130):", shootout)

# Al menos un equipo anotó más de 120 puntos
at_least_one_good_team = (team1_pts > 120) or (team2_pts > 120)
print("At least one good team (>120):", at_least_one_good_team)

# Ninguno de los equipos anotó más de 100 puntos
you_guys_are_bad = not ((team1_pts > 100) or (team2_pts > 100))
print("You guys are bad (both <=100):", you_guys_are_bad)

# Combinación de todas las condiciones anteriores negada
meh = not (shootout or at_least_one_good_team or you_guys_are_bad)
print("Meh (negation of all previous conditions):", meh)
