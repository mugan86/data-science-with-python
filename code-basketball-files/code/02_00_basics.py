##############
# basic python
# v0.0.1
##############

##########################
# how to read this chapter
##########################
1 + 1

##########
# comments
##########

# print the result of 1 + 1
print("############## COMMENTS ##############")
print(1 + 1)

###########
# variables
###########
print("############## VARIABLES ##############")

three_pt_made = 4

print(f"3 point made: {three_pt_made}")

print(f"Total points with {three_pt_made} annotations in 3pt made: {3*three_pt_made}")

## New Three pt made
three_pt_made = three_pt_made + 1

print(f"Total points with {three_pt_made} annotations in 3pt made: {3*three_pt_made}")

sum_one_one = 1 + 1
sum_result = f"1+1= {sum_one_one}"
print(sum_result)

####################
# types of variables
####################

print("############## TYPES OF VARIABLES ##############")


over_under = 216  # int
fg_percentage = 0.48  # float

starting_c = 'Karl-Anthony Towns'
starting_pg = "D'Angelo Russell"

print(f"{starting_c} => {type(starting_c)}")

print(f"{over_under} => {type(over_under)}")

print("############## F STRINGS ##############")

starters = f'{starting_c}, {starting_pg}, etc.'
print(f"Starters: {starters}")