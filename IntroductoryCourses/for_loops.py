for number in [2, 3, 5]:
    print(number)

primes = [2, 3, 5]
for p in primes:
    squared = p ** 2
    cubed = p ** 3
    print(p, squared, cubed)

# Sum the first 10 integers.
total = 0
for number in range(10):
    total += (number + 1)
print(total)

total = 0
for char in "tin":
    total += 1
    print(f"line {total}: char is {char}, total is {total}")

original = "tin"
result = ""
for char in original:
    result = char + result
print(result)

# Total length of the strings in the list: ["red", "green", "blue"] =12
total = 0
for word in ["red", "green", "blue"]:
    total = total + len(word)
print(total)

# List of word lengths: ["red", "green", "blue"] =[3, 5, 4]
lengths = []
for word in ["red", "green", "blue"]:
    lengths.append(len(word))
print(lengths)

# Concatenate all words: ["red", "green", "blue"] ="redgreenblue"
words = ["red", "green", "blue"]
result = ""
for word in words:
    result = result + word
print(result)

words = ["red", "green", "blue"]
acronym = ""
for word in words:
    acronym = acronym + word[0].upper()
print(acronym)

data = [1, 2, 2, 5]
cumulative = []
total = 0
for number in data:
    total += number
    cumulative.append(total)

print(cumulative)

message = ""
for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (number % 3) == 0:
        message = message + "a"
    else:
        message = message + "b"
print(message)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[-1])