# # This code has an intentional error. You can type it directly or
# # use it for reference to understand the error message below.
# def favorite_ice_cream():
#     ice_creams = [
#         'chocolate',
#         'vanilla',
#         'strawberry'
#     ]
#     print(ice_creams[3])
#
# favorite_ice_cream()
#
# # This code has an intentional error. Do not type it directly;
# # use it for reference to understand the error message below.
# def print_message(day):
#     messages = {
#         'monday': 'Hello, world!',
#         'tuesday': 'Today is Tuesday!',
#         'wednesday': 'It is the middle of the week.',
#         'thursday': 'Today is Donnerstag in German!',
#         'friday': 'Last day of the week!',
#         'saturday': 'Hooray for the weekend!',
#         'sunday': 'Aw, the weekend is almost over.'
#     }
#     print(messages[day])
#
# def print_friday_message():
#     print_message('Friday')
#
# print_friday_message()
#
# def another_function():
#     print('Syntax errors are annoying.')
#     print('But at least Python tells us about them!')
#     print('So they are usually not too hard to fix.')
#
# message = ""
# for number in range(10):
#     # use a if the number is a multiple of 3, otherwise use b
#     if (number % 3) == 0:
#         message = message + "a"
#     else:
#         message = message + 'b'
# print(message)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[-1])