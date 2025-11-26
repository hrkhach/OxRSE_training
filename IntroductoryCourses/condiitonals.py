# mass = 3.54
# if mass > 3.0:
#     print(mass, "is large")
#
# mass = 2.07
# if mass > 3.0:
#     print(mass, "is large")
#
# masses = [3.54, 2.07, 9.22, 1.86, 1.71]
# for m in masses:
#     if m > 9.0:
#         print(m, "is huge")
#     elif m > 3.0:
#         print(m, "is large")
#     else:
#         print(m, "is small")
#
# grade = 85
# if grade >= 70:
#     print("grade is C")
# elif grade >= 80:
#     print("grade is B")
# elif grade >= 90:
#     print("grade is A")
#
# # Does not automatically go back and re-evaluate if values change.
# velocity = 10.0
# if velocity > 20.0:
#     print("moving too fast")
# else:
#     print("adjusting velocity")
#     velocity = 50.0
#
# velocity = 10.0
# for i in range(5):  # execute the loop 5 times
#     print(i, ":", velocity)
#     if velocity > 20.0:
#         print("moving too fast")
#         velocity = velocity - 5.0
#     else:
#         print("moving too slow")
#         velocity = velocity + 10.0
# print("final velocity:", velocity)
import pandas as pd

# mass = [3.54, 2.07, 9.22, 1.86, 1.71]
# velocity = [10.00, 20.00, 30.00, 25.00, 20.00]
#
# i = 0
# for i in range(5):
#     if mass[i] > 5 and velocity[i] > 20:
#         print("Fast heavy object.  Duck!")
#     elif mass[i] > 2 and mass[i] <= 5 and velocity[i] <= 20:
#         print("Normal traffic")
#     elif mass[i] <= 2 and velocity[i] <= 20:
#         print("Slow light object. Ignore it")
#     else:
#         print("Whoa!  Something is up with the data.  Check it!")
#
#
# original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
# result = []
# for value in original:
#     if value < 0.0:
#         result.append(0)
#     else:
#         result.append(1)
# print(result)
#
# import glob
# import pandas as pd
# for filename in glob.glob('data/*.csv'):
#     contents = pd.read_csv(filename)
#     if len(contents) < 50:
#         print(filename, len(contents))

values = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
smallest, largest = None, None
for v in values:
    if smallest is None and largest is None:
        smallest, largest = v, v
    else:
        smallest = min(smallest, v)
        largest = max(largest, v)
print(smallest, largest)

values = [-2, 1, 65, 78, -54, -24, 100]
smallest, largest = None, None
for v in values:
    if smallest is None or v < smallest:
        smallest = v
    if largest is None or v > largest:
        largest = v
print(smallest, largest)


def calculate_life_quartile(exp):
    if exp < 58.41:
        # This observation is in the first quartile
        return 1
    elif exp >= 58.41 and exp < 67.05:
        # This expression is in the second quartile
        return 2
    elif exp >= 67.05 and exp < 71.70:
        return 3
    elif exp >= 71.70:
        return 4
    else:
        return None


print(calculate_life_quartile(62.5))

# Using Pandas
data = pd.read_csv("data/gapminder_all.csv")
data["life_qrtl"] = data["lifeExp_1952"].apply(calculate_life_quartile)
print(data["life_qrtl"])