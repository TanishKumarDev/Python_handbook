basic_variables = "Python Variables"
print(basic_variables)

# Python variables are dynamically typed, meaning the same variable can hold different types of values during execution.
dynamic_typing = "Python is a dynamically typed language"
print(dynamic_typing)

# Multiple Assignments

a, b, c = 5, 10, 15
print("Values:", a, b, c)

# Type Casting a Variable
s = "25" # initial a string

int_value = int(s) # converting string to integer
converted_float = float(s) # converting string to float
string_value = str(25) # converting integer to string

print("Original string:", s)
print("Integer value:", int_value)
print("Float value:", converted_float)
print("String value:", string_value)

# Check data types
print("Data type of original string:", type(s))
print("Data type of integer value:", type(int_value))
print("Data type of float value:", type(converted_float))
print("Data type of string value:", type(string_value))

# Object Reference in Python
x = 5 # x refers to an integer object
y = x # y refers to the same integer object as x
z = 10 # z refers to a different integer object

print("Value of x:", x)
print("Value of y:", y)
print("Value of z:", z)

# Modifying the value of x
x = 20
print("After modifying x:")
print("Value of x:", x)
print("Value of y:", y)
print("Value of z:", z)

# Delete a Variable Using del Keyword
int_value = 10
print("Value of int_value before deletion:", int_value)

del int_value

try:
    print("Value of int_value after deletion:", int_value)
except NameError:
    print("int_value is deleted and no longer accessible.")

# Practical Examples
# 1. Swapping Two Variables
num1 = 5
num2 = 10
num1, num2 = num2, num1
print("Swapped Values: num1 =", num1, ", num2 =", num2)

# 2. Counting Characters in a String
word = "Hello"
char_count = len(word)
print("Number of characters in '", word, "':", char_count)

# Scope of a Variable