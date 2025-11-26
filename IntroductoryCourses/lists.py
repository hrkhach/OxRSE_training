odds = [1, 3, 5, 7]
print("odds are:", odds)

names = ["Curie", "Darwing", "Turing"]
print("names is originally:", names)
names[1] = "Darwin"
print("final value of names", names)

salsa = ["peppers", "onions", "cilantro", "tomatoes"]
my_salsa = salsa
salsa[0] = "hot peppers"
print("Ingredients in my salsa:", my_salsa)

salsa = ["peppers", "onions", "cilantro", "tomatoes"]
my_salsa = list(salsa)  # makes a *copy* of the list
salsa[0] = "hot peppers"
print("Ingredients in my salsa:", my_salsa)

# Nested lists
x = [['pepper', 'zucchini', 'onion'],
     ['cabbage', 'lettuce', 'garlic'],
     ['apple', 'pear', 'banana']]

odds.append(11)
print("odds after adding a value:", odds)
removed_element = odds.pop(0)
print("odds after removing the first element:", odds)
print("removed element:", removed_element)

odds.reverse()
print("odds after reversing:", odds)

odds = [1, 3, 5, 7]
primes = odds
primes.append(2)
print("primes:", primes)
print("odds:", odds)

binomial_name = "Drosophila melanogaster"
group = binomial_name[0:10]
print("group:", group)

species = binomial_name[11:23]
print("species:", species)

chromosomes = ['X', 'Y', '2', '3', '4']
autosomes = chromosomes[2:5]
print('autosomes:', autosomes)

last = chromosomes[-1]
print('last:', last)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = numbers[0:6:2]
print('odd numbers:', odd_numbers)

string_for_slicing = 'Observation date: 02-Feb-2013'
list_for_slicing = [['fluorine', 'F'],
                    ['chlorine', 'Cl'],
                    ['bromine', 'Br'],
                    ['iodine', 'I'],
                    ['astatine', 'At']]

print(string_for_slicing[-4:])
print(list_for_slicing[-4:])

counts = [2, 4, 6, 8, 10]
repeats = counts * 2
print(repeats)
