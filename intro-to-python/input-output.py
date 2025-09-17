# 1. Input in Python
name = input("Enter your name: ")
# 2. Printing Output
print("Hello, " + name + "!")

# Example – Printing Variables:

# single variable
age = 25
print("Age:", age)

# multiple variables
height = 5.9
weight = 70
print("Height:", height, "Weight:", weight)

# 3. Taking Multiple Inputs
num1, num2 = input("Enter two numbers value: ").split()
print("Number 1:", num1)
print("Number 2:", num2)

# 4. Changing Input Type
color = input("Enter fav color: ")
print("Fav color:", color)
color = input("Enter fav color! changed: ")
print("Fav color:", color)

# 5. Checking Data Type
a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for": 2, "Geeks": 3}

print(type(a))  # str
print(type(b))  # int
print(type(c))  # float
print(type(d))  # tuple
print(type(e))  # list
print(type(f))  # dict
