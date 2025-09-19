###########
# FUNCTIONS
###########

print("############## FUNCTIONS ##############\n")

#################
# Built-in functions
#################

print("Length of roster list:", len(['kevin durant', 'james harden', 'kyrie irving']))
pts_per_3 = len(['kevin durant', 'james harden', 'kyrie irving'])
print("Points per 3:", pts_per_3)

print("4 + len(roster):", 4 + len(['kevin durant', 'james harden', 'kyrie irving']))


#################
# Defining functions
#################

def pts(fg2, fg3, ft):
    """
    Calculate points scored based on:
    - fg2: 2-point field goals
    - fg3: 3-point field goals
    - ft: free throws

    Returns the total points scored.
    """
    return fg2 * 2 + fg3 * 3 + ft * 1

print("Total points:", pts(8, 4, 5))


def pts_noisy(fg2, fg3, ft):
    """
    Same as pts() but also prints the number of 2-point field goals.
    """
    print("fg2 inside function:", fg2)
    return fg2 * 2 + fg3 * 3 + ft * 1

print("Total points (noisy):", pts_noisy(8, 4, 5))


#################
# Side effects
#################

def is_player_on_team(player, team):
    """
    Check if a player is on the team by:
    1. Adding the player to the team list
    2. Returning True if the player appears 2 or more times
    """
    team.append(player)  # side effect: modifies the list!
    return team.count(player) >= 2

roster_list = ['kevin durant', 'james harden', 'kyrie irving']
print("Roster before check:", roster_list)
print("Is Jared Dudley on team?", is_player_on_team('jared dudley', roster_list))
print("Roster after check:", roster_list)


#################
# Function arguments
#################

print("Points with positional args:", pts(8, 4, 5))
print("Points with different order:", pts(8, 5, 4))  # order matters!
print("Points with keywords:", pts(fg3=4, fg2=8, ft=5))
print("Points mixed (positional + keyword):", pts(8, 4, ft=5))


#################
# Default values
#################

def pts_w_default(fg2, fg3, ft=0):
    """
    Same as pts(), but free throws default to 0 if not provided.
    """
    return fg2 * 2 + fg3 * 3 + ft * 1

print("Points with default free throws:", pts_w_default(8, 4))


#####################################
# Functions that take other functions
#####################################

def do_to_list(working_list, working_fn, desc):
    """
    Apply a function (working_fn) to a list (working_list),
    and return a string with the description + result.
    """
    value = working_fn(working_list)
    return f"{desc} {value}"

def last_elem_in_list(working_list):
    """
    Return the last element of a list.
    """
    return working_list[-1]

positions = ['C', 'PF', 'SF', 'SG', 'PG']

print(do_to_list(positions, last_elem_in_list, "Last element in your list:"))
print(do_to_list([1, 2, 4, 8], last_elem_in_list, "Last element in your list:"))
print(do_to_list(positions, len, "Length of your list:"))
print(do_to_list([2, 3, 7, 1.3, 5], lambda x: 3 * x[0], "First element times 3 is:"))
