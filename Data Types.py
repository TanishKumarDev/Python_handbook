# 1. Numeric Data Types in Python
# Integer
int_var = 10
print(type(int_var))

# Float
float_var = 3.14
print(type(float_var))

# Complex
complex_var = 2 + 3j
print(type(complex_var))

# 2. Sequence Data Types in Python
# String
string_var = "Hello"
print(type(string_var))

print(string_var[0]) # Accessing first character

# List
list_var = [1, 2, 3]
print(type(list_var))
print(list_var[0]) # Accessing first element

# Tuple
tuple_var = (1, 2, 3)
print(type(tuple_var))
print(tuple_var[0]) # Accessing first element

# Set
set_var = {1, 2, 3}
print(set_var) # Accessing elements in a set
print(type(set_var))

# 3. Boolean Data Type in Python
bool_var = True
print(type(bool_var))

print(type(True))
print(type(False))
print(type(True))

# 4. Set Data Type in Python

set_example = {1, 2, 3, 4, 5}
print(set_example) # Accessing elements in a set
print(type(set_example))

# Set using string
set_example_str = set("Hello")
print(set_example_str) # Accessing elements in a set
print(type(set_example_str))

# Set using list
set_example_list = set([1, 2, 3, 4, 5])
print(set_example_list) # Accessing elements in a set
print(type(set_example_list))

# 5. Dictionary Data Type
d = {}


d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

# Accessing Key-value in Dictionary
d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(3))