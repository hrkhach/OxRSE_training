# # Identifying Syntax Errors
# def another_function():
#     print("Syntax errors are annoying.")
#     print("But at least python tells us about them!")
#     print("So they are usually not too hard to fix.")
#
#
# def report(pressure):
#     print('pressure is', pressure)
#
#
# print('calling', report, 22.5)
#
#
# # Order of Operations
# def print_time(hour, minute, second):
#     time_string = str(hour) + ':' + str(minute) + ':' + str(second)
#     print(time_string)
#
#
# result = print_time(11, 37, 59)
# print(result)
#
# # Encapsulation
# import pandas as pd
#
#
# def min_in_data(filename):
#     data = pd.read_csv(filename)
#     return data.min()
#
#
# def first_negative(values):
#     for v in values:
#         if v < 0:
#             return v
#     return None
#
# def print_date(year, month, day):
#     joined = str(year) + '/' + str(month) + '/' + str(day)
#     print(joined)
#
# import random
#
#
# def print_egg_label(mass):
#     # egg sizing machinery prints a label
#     if mass >= 85:
#         return "jumbo"
#     elif mass >= 70:
#         return "large"
#     elif mass < 70 and mass >= 55:
#         return "medium"
#     elif mass < 50:
#         return "too light, probably spoiled"
#     else:
#         return "small"
#
# for i in range(10):
#
#     # simulating the mass of a chicken egg
#     # the (random) mass will be 70 +/- 20 grams
#     mass = 70 + 20.0 * (2.0 * random.random() - 1.0)
#
#     print(mass, print_egg_label(mass))
import pandas as pd

df = pd.read_csv('data/gapminder_gdp_asia.csv', index_col=0)
japan = df.loc['Japan']
print(japan)
# year = 1983
# gdp_decade = 'gdpPercap_' + str(year // 10)
# avg = (japan.loc[gdp_decade + "2"] + japan.loc[gdp_decade + "7"]) / 2


def avg_gdp_in_decade(country, continent, year):
    df = pd.read_csv('data/gapminder_gdp_' + continent + '.csv', delimiter=',', index_col=0)
    country_df = df.loc[country]
    gdp_decade = 'gdpPercap_' + str(year // 10)
    avg = (country_df.loc[gdp_decade + "2"] + country_df.loc[gdp_decade + "7"]) / 2
    return avg

print(avg_gdp_in_decade('Japan', 'asia', 1983))