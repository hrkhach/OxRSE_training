import time

import numpy
import numpy as np
from functools import reduce


####################################
## Side Effects
# y = [3, 2]
# x = [2]
# x = y
#
# print("x: ", x)
# print("y: ", y)
#
# def my_cool_function(x, y):
#     x[:] = y
#
#
# y = [3, 2]
# x = [2]
# my_cool_function(x, y)
#
# print("x: ", x)
# print("y: ", y)
#
# z = 3
# def my_cool_function(x, y):
#     global z
#     x = y
#     z = z + 1
#
#
# y = [3,2]
# x = [2]
# my_cool_function(x, y)
#
# print("x: ", x)
# print("y: ", y)
# print("z: ", z)
# x = np.zeros(1000) # do we have enough RAM available for this?
#
# myfile = open("example.txt", "w") # does this file exist? Do I have write permissions?
#
# line = myfile.readline()    # did I open this for reading?
# line = myfile.readline()    # Same call to readline, but result is different!

# result = 0
# for x in data:
#     result += expensive_computation(x)

# Pure functions

# # pure
# def add_one(x):
#     return x + 1
#
# x = 1
# add_one(x)
# print(x)
#
# # say_hello is not pure - printing text counts as a side effect,
# # even though it is the clear purpose of the function
# def say_hello(name):
#     print("Hello", name)
#
# name = "John"
# say_hello(name)
# print(name)
#
# # not pure
# def append_item_1(a_list, item):
#     a_list += [item]
#     return a_list
#
# a_list = [1, 2, 3]
# append_item_1(a_list, 1)
# print(a_list)
#
#
# # pure
# def append_item_2(a_list, item):
#     result = a_list + [item]
#     return result
#
# a_list = [1, 2, 3]
# append_item_2(a_list, 1)
# print(a_list)
#
# # Conway's Game of Life
# import numpy as np
#
#
# def step(grid):
#     rows, cols = grid.shape
#     resulted_grid = grid.copy()
#     for i in range(rows):
#         for j in range(cols):
#             neighbours = get_neighbours(grid, i, j)
#             count = sum(neighbours)
#             # cells are unaffected unless they:
#             # - die of under- or overpopulation, or
#             # - become alive if they have exactly three neighbours
#             if count < 2 or count > 3:
#                 resulted_grid[i, j] = 0
#             elif count == 3:
#                 resulted_grid[i, j] = 1
#     return resulted_grid
#
# def get_neighbours(grid, i, j):
#     rows, cols = grid.shape
#     indices = np.array([(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
#                         (i, j - 1),                 (i, j + 1),
#                         (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)])
#     valid_indices = ((indices[:,0] >= 0) & (indices[:,0] < rows) &
#                      (indices[:,1] >= 0) & (indices[:,1] < cols))
#     return grid[indices[valid_indices][:,0], indices[valid_indices][:,1]]
#
#
# # Test
# grid = np.array([[0, 0, 0, 0, 0],
#                  [0, 0, 1, 0, 0],
#                  [0, 1, 1, 1, 0],
#                  [0, 0, 1, 0, 0],
#                  [0, 0, 0, 0, 0]], dtype=np.int8)
#
# new_grid = step(grid)
# print(new_grid)
#
# # our grid should show a square pattern, but doesn't
# expected_grid = np.array([[0, 0, 0, 0, 0],
#                           [0, 1, 1, 1, 0],
#                           [0, 1, 0, 1, 0],
#                           [0, 1, 1, 1, 0],
#                           [0, 0, 0, 0, 0]], dtype=np.int8)
# assert np.array_equal(new_grid, expected_grid)
# print()
# print(step(new_grid))
#
#
#
# print()
#
# def add_two(x):
#     return add_one(add_one(x))
#
# print(add_two(2))

########################################################################
## Higher-Order Functions

# # First class functions
# def add_one(x):
#     return x + 1
#
# def apply_function(f, x):
#     return f(x)
#
# print(apply_function(add_one, 1))

# # Lambda Functions
# add_one = lambda x: x + 1   # NOQA E731
# # The # NOQA E731 comment is a flake8 directive to ignore the E731 error,
# # which is raised when a lambda function is assigned to a variable.
# print(add_one(1))
#
#
# # Higher-Order Functions
# def sum(data):
#     result = 0
#     for x in data:
#         result = result + x
#     return result
#
# def maximum(data):
#     result = 0
#     for x in data:
#         result = max(result, x)
#     return result
#
# def reduce(data, bin_op):
#     result = data[0]
#     for x in data[1:]:
#         result = bin_op(result, x)
#     return result
#
# data = [1, 2, 3, 4, -1]
# print(reduce(data, lambda a, b: a + b))
# print(reduce(data, lambda a, b: a * b))
# print(reduce(data, lambda a, b: max(a,b)))
# print(reduce(data, lambda a, b: min(a,b)))
#
# print(reduce(data, max))
# print(reduce(data, min))
#
# # Map, Filter, Reduce
# l = [1,2,3]
#
# def add_one(x):
#     return x + 1
#
# # Returns a <map object> so need to convert to list
# print(list(map(add_one, l)))
# print(list(map(lambda x: x + 1, l)))
#
#
#
# #
# # l = [1, 2, 3]
# #
# #
# # def add(a, b):
# #     return a + b
# #
# #
# # print(reduce(add, l))
# # print(reduce(lambda a, b: a + b, l))
#
# # Sum of Squares
# # def sum_of_squares(l):
# #     return reduce(lambda a, b: a + b, map(lambda x: x ** 2, l))
#
#
# # def sum_of_squares(l):
# #     integers = [int(x) if x[0] != "#" else 0 for x in l]
# #     squares = map(lambda x: x ** 2, integers)
# #     return reduce(lambda a, b: a + b, squares)
#
# def sum_of_squares(l):
#     not_comments = filter(lambda x: x[0] != "#", l)
#     squares = map(lambda x: int(x) ** 2, not_comments)
#     return reduce(lambda x, y: x + y, squares)
#
#
# # print(sum_of_squares([0]))
# # print(sum_of_squares([1]))
# # print(sum_of_squares([1, 2, 3]))
# # print(sum_of_squares([-1]))
# # print(sum_of_squares([-1, -2, -3]))
#
# print(sum_of_squares(['1', '2', '3']))
# print(sum_of_squares(['-1', '-2', '-3']))
#
# print(sum_of_squares(['1', '2', '3']))
# print(sum_of_squares(['-1', '-2', '-3']))
# print(sum_of_squares(['1', '2', '#100', '3']))
#
# ## Comprehensions
# # List Comprehensions
# print([i for i in range(5)])
# print([i * 2 for i in range(5)])
#
# print([i * 2 for i in range(5) if i % 2 == 0])
#
# # Set comprehension
# print({2 * i for i in range(5)})
#
# # Dictionary comprehension
# print({i: 2 * i for i in range(5)})
#
# ## Generators
# print((2 * i for i in range(5)))
#
# for i in (2 * i for i in range(5)):
#     print(i)
#
## Decorators
# def with_logging(func):
#     """A decorator which adds logging to a function."""
#
#     def inner(*args, **kwargs):
#         print("Before function call")
#         result = func(*args, **kwargs)
#         print("After function call")
#         return result
#
#     return inner
#
#
# def add_one(n):
#     print("Adding one")
#     return n + 1
#
#
# # Redefine function add_one by wrapping it within with_logging function
# add_one = with_logging(add_one)
#
#
# # Another way to redefine a function - using a decorator
# @with_logging
# def add_two(n):
#     print("Adding two")
#     return n + 2
#
#
# print(add_one(1))
# print(add_two(1))
#
#
# def with_timing(func):
#     """A decorator to measure the execution time of the decorated function."""
#
#     def inner(*args, **kwargs):
#         start = time.process_time_ns()
#         result = func(*args, **kwargs)
#         stop = time.process_time_ns()
#         print("Took {0} seconds".format((stop - start) / 1e9))
#         return result
#
#     return inner
#
#
# @with_timing
# def measure_me(n):
#     total = 0
#     for i in range(n):
#         total += i * i
#
#     return total
#
#
# print(measure_me(1000000))
#
###################################################################
### Recursion
def factorial(n):
    """Calculate the factorial of a given number.

    :param int n: The number to calculate
    :return: The resultant factorial
    """
    if n < 0:
        raise ValueError("Only use non-negative integers.")

    factorial = 1
    for i in range(1, n + 1):  # iterate from 1 to n
        # save intermediate value to use in the next iteration
        factorial *= i

    return factorial


def factorial_recursive(n):
    """Calculate the factorial of a given number.

    :param int n: The number to calculate
    :return: The resultant factorial"""
    if n < 0:
        raise ValueError("Only use non-negative integers.")

    if n == 1:
        return 1  # exit from recursion, prevents infinite loops
    return n * factorial_recursive(n - 1)  # recursive call to the same function


print(factorial_recursive(10))


# Recursion on trees
class Node(object):
    """Generic tree node."""

    def __init__(self, name="root", children=None):
        self.value = name
        self.children = children or []

    def __repr__(self):
        return f"Node({self.value},{self.children})"


#    +
#   / \
#  1  *
#    / \
#   2   3

t = Node("+", [Node("1"),
               Node("*", [Node("2"),
                          Node("3")])])


def count_nodes(tree):
    """Count the number of nodes in a tree.

    :param Node tree: The tree to count the nodes of
    :return: The number of nodes in the tree
    """
    if not tree.children:
        return 1
    else:
        return 1 + sum(count_nodes(child) for child in tree.children)


print(count_nodes(t))


def evaluate_tree(tree):
    if not tree.children:
        return tree.value
    else:
        return evaluate_tree(tree.children[0]) + tree.value + evaluate_tree(tree.children[1])


print(evaluate_tree(t))


def evaluate(tree):
    """Evaluate the result of a tree representing a mathematical expression.

    :param Node tree: The tree to evaluate
    :return: The result of the expression
    """
    if not tree.children:
        return int(tree.value)
    else:
        left = evaluate(tree.children[0])
        right = evaluate(tree.children[1])
        if tree.value == "+":
            return left + right
        elif tree.value == "-":
            return left - right
        elif tree.value == "*":
            return left * right
        elif tree.value == "/":
            return left / right
        else:
            raise ValueError(f"Unknown operator: {tree.value}")


print(f"{evaluate_tree(t)} = {evaluate(t)}")
