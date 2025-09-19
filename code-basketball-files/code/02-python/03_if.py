# Puntos de cada equipo
team1_pts = 110
team2_pts = 120

# Comparaciones booleanas básicas
team1_won = team1_pts > team2_pts          # True si el equipo 1 ganó
team2_won = team1_pts < team2_pts          # True si el equipo 2 ganó

###############
# if statements
###############
print("############## IF STATEMENTS ##############")

if team1_won:
  message = "Nice job team 1!"
elif team2_won:
  message = "Way to go team 2!!"
else:
  message = "must have tied!"

print(f'if: {message}')