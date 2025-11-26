# ################################
# ## Variables and types
# # Using variable to store values
# age = 42
# first_name = "Ahmed"
#
# print(first_name, "is", age, "years old")
#
# atom_name = "sodium"
# print(atom_name[0:3])
#
# num_subjects = 600
# num_per_survey = 42
# num_surveys = (num_subjects - 1) // num_per_survey + 1
#
# print(f"{num_subjects} subjects, {num_per_survey} per servey: {num_surveys}")
# ###################################
# # ##Built-in Functions and Help
#
# help(round)
# ##################################
# # ## Libraries
# import math
#
# print("pi is", math.pi)
# print("cos(pi) is", math.cos(math.pi))
#
# help(math)
#
# from math import cos, pi
# print("cos(pi) is", cos(pi))
#
# import math as m
#
# from matplotlib import pyplot as plt
# Locating the right module
# import random
#
# bases = 'ACTTGCTTGAC'
#
# random_index = random.randrange(len(bases))
# print(bases[random_index])
#
# print(random.choice(bases))
#
# print(bases[random.randint(0, len(bases) - 1)])
#
# print(random.sample(bases, 1)[0])  # sample returns list of values
#
# # Importing with aliases
# import math as m
#
# angle = m.degrees(m.pi / 2)
# print(angle)
#
# import math
#
# angle = math.degrees(math.pi / 2)
# print(angle)
#
#
# from math import pi, degrees
# angle = degrees(pi / 2)
# print(angle)
#
# from math import log
# log(0)
