## - Variables

# print("hello world")
#
# six = 2 * 3
# print(six)
#
# one, two = 1, 2
#
# first, second = 1, 2
# third, fourth = second, first
# print(third, fourth)
#
# number = 1
# number = 2
#
# print(type(number))
#
# z = 3+1j
#
# print(dir(z))
# print(type(z))
# print(z.real)
# print(z.imag)
#
# given = 'Joe'
# middle = "Frederick"
# family = "'Bloggs'"
# full = given + " " + middle + " " + family
# print(full)
#
# nothing = None
# print(type(nothing))
#
# age, house_number = 30, "76"
# print(str(age), float(age), int(house_number), float(house_number))
#


######################################################################
## - Containers
# string_for_slicing = "Observation date: 02-Feb-2013"
# list_for_slicing = [["fluorine", "F"],
#                     ["chlorine", "Cl"],
#                     ["bromine", "Br"],
#                     ["iodine", "I"],
#                     ["astatine", "At"]]
#
# print(string_for_slicing)
# print(list_for_slicing)
#
# print(string_for_slicing[-4:])
# print(list_for_slicing[-4:])
#
# str = "This is a string"
# a_list = str.split()
# print(a_list)
#
# new_str = " ".join(a_list)
# print(new_str)
#
# good_match = {
#     ("lamb", "Mint"): True,
#     ("Bacon", "Chocolate"): False
# }
#
# illegal= {
#     ["lamb", "Mint"]: True,
#     ["Bacon", "Chocolate"]: False
# }
#
# x = [1, 2, 3]
# y = x
# y[1] = 20
# print(x, y)
#
# x = [1, 2, 3]
# y = x[:]
# y[1] = 20
# print(x, y)
#
# x = [["a", "b"], "c"]
# y = x
# z = x[:]
#
# x[0][1] = "d"
# z[1] = "e"
#
# print(x, y, z)
#############################################################
## - Functions
# char_count = len("Python")
# print(char_count)
#
# nums = [1, 2, 3]
# result = nums.append(4)
#
# print(nums)
# print(result)
#
#
# def add_one(value):
#     return value + 1
#
#
# two = add_one(1)
# print(two)
#
# def sey_hello(name):
#     return "Hello, " + name + "!"
#
# print(sey_hello("World"))

# def say_hello(name="World"):
#     return "Hello, " + name + "!"
#
#
# print(say_hello())
# print(say_hello("Python"))      # positional argument
# print(say_hello(name="Named Argument"))     # named argument
#
# def fence(original, wrapper):
#     return wrapper + original + wrapper
#
#
# print(fence("name", "*"))
#
#
# def say_hello(greeting="Hello", name="World"):
#     return greeting + ", " + name + "!"
#
# # No arguments - both default values
# print(say_hello())
#
# # One positional argument, one default value
# print(say_hello("Hello"))
#
# # Both positional arguments
# print(say_hello("Hi", "World"))
#
# # One Named argument
# print(say_hello(greeting="Hello"))
# print(say_hello(name="World"))
#
# # Both named arguments
# print(say_hello(greeting="Yo", name="Named"))
#
# # One positional argument, then one named argument
# print(say_hello("Hello", name= "Positional"))
#
#
# f = 0
# k = 0
#
# def multiply_by_10(f):
#     k = f * 10
#     return k
#
# multiply_by_10(2)
# multiply_by_10(8)
#
# print(k)
#
# def fahr_to_cels(fahr):
#     # Convert temperature in Fahrenheit to Celsius
#     return 5 * (fahr - 32) / 9
#
#
# def fahr_to_kelv(fahr):
#     # Convert temperature in Fahrenheit to Kelvin
#     return fahr_to_cels(fahr) + 273.15
#
#
# print(fahr_to_kelv(32))
# print(fahr_to_kelv(212))
#
# academics = [
#     {
#         "name": "Alice",
#         "papers": [
#             {
#                 "title": "My science paper",
#                 "date": 2015
#             },
#             {
#                 "title": "My other science paper",
#                 "date": 2017
#             }
#         ]
#     },
#     {
#         "name": "Bob",
#         "papers": [
#             {
#                 "title": "Bob writes about science",
#                 "date": 2018
#             }
#         ]
#     }
# ]
#
#
# def write_paper(academics, name, title, date):
#     paper = {
#         "title": title,
#         "date": date
#     }
#
#     for academic in academics:
#         if academic["name"] == name:
#             academic["papers"].append(paper)
#             break
#     else:
#         raise KeyError("Named academic does not exist")
#

#
#
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, "equals", x, "*", n // x)
#             break
#     else:
#         # Loop fell through without finding a factor
#         print(n, "is a prime number")
#
#
# def append_to_list(l):
#     l.append("appended")
#     l = [1,2,3]
#     l.append("again")
#     return l
#
# a_list = ["this", "is", "a", "list"]
#
# print(append_to_list(a_list))
# print(a_list)
#
# def count_papers(academics_arg):
#     answer = 0
#     for academic in academics_arg:
#         answer += len(academic["papers"])
#     return answer
#
#
# print(count_papers(academics))
#
#
# def list_papers(academics_arg):
#     answer = []
#     for academic in academics_arg:
#         for paper in academic["papers"]:
#             answer.append(paper["title"])
#
#     return answer
#
#
# print(list_papers(academics))
#
#
# def list_papers1(academics_arg):
#     papers = []
#
#     for academic in academics_arg:
#         papers = papers + academic["papers"]
#
#     return papers
#
# print(list_papers1(academics))
###########################################################################
## -  Arrays
import numpy as np

# my_array = np.array(range(5))
# print(my_array)
#
# print(my_array[2])
#
# for element in my_array:
#     print("Hello" * element)
#
# print(my_array + 2)

import time
import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
# start_time = time.perf_counter()
#
# nested_list = [[0 for _ in range(10000)] for _ in range(10000)]
# nested_list = [[x+10 for x in column] for column in nested_list]
#
# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
#
# print(elapsed_time)
# logging.info(f"process executed in {elapsed_time: .4f} seconds")
#
# start_time = time.perf_counter()
#
# array = np.zeros((10000, 10000))
# array = array + 10
#
# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(elapsed_time)

data = np.loadtxt(
    fname="C:/Users/hrach/Desktop/Denovo Sciences/OxRSE_training/procedural/inflammation/inflammation/data/inflammation-01.csv",
    delimiter=",")
#
# print(data)
#
# print(type(data))
#
# print(data.dtype)
#
# print(data.shape)
#
# print(data[0,0])
#
# print(data[0:4,0:10])
#
# print(data[5:10,0:10])
#
# print(data[:3,36:])
#
# x = np.arange(5)
# y = x[:]
# y[2] = 0
# print(x)
#
# x = np.arange(5)
# y = np.copy(x)
# y[2] = 0
# print(x)
#
# doubledata = data * 2.0
#
# print("original:")
# print(data[:3,36:])
# print("doubledata:")
# print(doubledata[:3,36:])
#
# tripledata = doubledata + data
# print("tripledata:")
# print(tripledata[:3,36:])
#
# A = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print("A = ")
# print(A)
#
# B = np.hstack([A,A])
# print("B = ")
# print(B)
#
# C = np.vstack([A, A])
# print("C = ")
# print(C)
#
#
# first_row = data[:1]
# print(first_row)
#
# first_col = data[:, :1]
# last_col = data[:, -1:]
#
# stack = np.hstack([first_col, last_col])
# print("stack = ")
# print(stack)
#
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
#
# print(np.dot(a, b))
#
# print(np.mean(data))
#
# import time
# print(time.ctime())
#
# maxval, minval, stdval = np.max(data), np.min(data), np.std(data)
#
# print("max inflammation:", maxval)
# print("min inflammation:", minval)
# print("std deviation:", stdval)
#
# print(f"max inflammation of the first patient is {np.max(data[0,:])}")
#
# print(np.mean(data, axis=0))
#
# print(np.mean(data, axis=0).shape)
#
# print(data.shape)
#
# patients_average = np.mean(data, axis=1)
# print(patients_average)
# print(patients_average.shape)

# npdiff = np.array([0, 2, 5, 9, 14])
#
# print(np.diff(npdiff))
#
# print(np.diff(data, axis=1))
#
# print(np.diff(data, axis=1).shape)

# print(np.max(np.diff(data, axis=1), axis=1))
#
# print(np.max(np.diff(data, axis=1), axis=1).shape)
#
# print(np.max(np.absolute(np.diff(data, axis=1)), axis=1))

# works only if the lengths are the same
print(np.arange(5) * np.arange(5))

# works only if the lengths are the same
print(np.zeros([2,3]) * np.zeros([2,3]))
print()

subset = data[:10,:10]
print(subset)

multiplier = np.arange(1, 11)
print(multiplier)

print(subset * multiplier)