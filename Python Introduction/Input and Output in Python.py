#----------Taking input in Python----------

name = input("Enter your name: ")
print("Hello, " + name + "!")

#----------Take Multiple Input in Python----------
x, y = input("Enter two numbers separated by space: ").split() # Taking multiple inputs
print("The sum is: ", int(x) + int(y))

#----------How to Change the Type of Input in Python---------
# Print Names in Python
color = input("Enter your favorite color: ") # By default, input is of string type

# Print Numbers in Python
int_num = int(input("Enter a number: ")) # Converting input to integer type
print("You entered:", int_num)

# Print Float/Decimal Number in Python
decimal_num = float(input("Enter a decimal number: ")) # Converting input to float type
print("You entered:", decimal_num)

##----------Find DataType of Input in Python----------
data = input("Enter something: ")

print("You entered:", data)
print("Data type:", type(data))

#----------Output Formatting----------
# Example 1: Using Format()
amount = 100
currency = "USD"
print("The total amount is {} {}".format(amount, currency))

# Example 2: Using sep and end parameter
print("Python", end="@") # end Parameter with '@'
print("is", "fun", sep="-") # sep Parameter with '-'

# Example 3: Using f-string
print(f"The total amount is {amount} {currency}")

# Extra Power of f-string (expressions bhi likh sakte ho):
num1 = 5
num2 = 10
print(f"Sum of {num1} and {num2} is {num1 + num2}")

# Example 4: Using % Operator
print("The total amount is %d %s" % (amount, currency))