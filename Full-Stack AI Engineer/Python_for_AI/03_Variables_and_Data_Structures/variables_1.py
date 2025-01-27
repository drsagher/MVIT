# Variables and Data Structures in Python

# Numbers
integer_variable = 10
float_variable = 3.14
complex_variable = 2 + 3j

print("Integer:", integer_variable)
print("Float:", float_variable)
print("Complex:", complex_variable)

# Strings
string_variable = "Hello, world!"
print("String:", string_variable)


# Booleans
boolean_variable_true = True
boolean_variable_false = False
print("Boolean True:", boolean_variable_true)
print("Boolean False:", boolean_variable_false)

# Lists (Mutable, ordered sequence)
my_list = [1, 2, 3, "apple", 3.14]
my_list.append(4)  # Adding an element
my_list.remove(2) # Removing element by value
del my_list[0]  # Removing element by index

print("List:", my_list)

# Tuples (Immutable, ordered sequence)
my_tuple = (1, 2, 3, "banana", 4.5)

print("Tuple:", my_tuple)


# Sets (Unordered collection of unique elements)
my_set = {1, 2, 2, 3, 3, 3, "orange"}
print("Set:", my_set) #output will be unordered and without the duplicate values

my_set.add(4)
my_set.remove(2)  # Remove an element
print("Set after operations:", my_set)

# Dictionaries (Key-value pairs)
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
my_dict["occupation"] = "Engineer"  # Adding a new key-value pair
del my_dict["city"] # remove a key value pair

print("Dictionary:", my_dict)