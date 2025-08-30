# 👉 Basic Functions
def fun():
    print("Hello, World!")
fun() 
# 👉 Function Arguments
def evenOdd(x : int) -> None: # Also can without type_hints like def evenOdd(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")
evenOdd(10)
evenOdd(5)

# 👉 Type of function arguments
# Default argument : A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument. 
def myFun(x, y = 50):
    print("x:", x)
    print("y:", y)

    # print("z:", z) # This will raise an error
myFun(10) # x: 10, y: 50

# Keyword arguments (named arguments) : The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.
def myFun2(x, y):
    print("x:", x)
    print("y:", y)
myFun2(y=60, x=70) # x: 70, y: 60

# Positional arguments : Positional arguments are the arguments that need to be passed in the same order as the function parameters.
def nameAge(name, age):
    print("Name:", name)
    print("Age:", age)

print("Case 1:")
nameAge("Alice", 30) # Name: Alice, Age: 30
print("Case 2:")
nameAge(30, "Alice") # Name: 30, Age: Alice
# Note: In Case 2, the order of arguments is changed, which may lead to incorrect results.
# We used the Position argument during the function call so that the first argument (or value) is assigned to name and the second argument (or value) is assigned to age. By changing the position, or if you forget the order of the positions, the values can be used in the wrong places, as shown in the Case-2 example below, where 27 is assigned to the name and Suraj is assigned to the age.

# Arbitrary arguments (variable-length arguments *args and **kwargs) : These allow you to pass a variable number of arguments to a function.
def myFun4(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
myFun4(10, 20, 30, x=40, y=50)

# 👉 Docstring : The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function. The use of docstring in functions is optional but it is considered a good practice.
def myFun5():
    """
    This is a docstring for myFun5 function.
    """
    print("Hello from myFun5")
print(myFun5.__doc__)

# 👉 Function within Functions
def outerFunction():
    print("Hello from OuterFunction")
    def innerFunction():
        print("Hello from innerFunction")
    innerFunction()

outerFunction()


# 👉 Anonymous Functions : means that a function is without a name., def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.
def myFun6(x, y):
    return (lambda a, b: a + b)(x, y)

print(myFun6(10, 20))

# 👉 Return Statement in Function
def myFun7(x, y):
    return x + y

(myFun7(10, 20))
print("Result:", myFun7(10, 20))
# 👉 Pass by Reference and Pass by Value : Python every variable name is a reference. When we pass a variable to a function Python, a new reference to the object is created. Parameter passing in Python is the same as reference passing in Java.

# In Python, everything is an object, and variables are just references (names) pointing to those objects.
# So technically, Python uses pass-by-object-reference (or pass-by-assignment).
    # If the object is immutable (like int, str, tuple): function cannot modify it.
    # If the object is mutable (like list, dict, set): function can modify it.

# Example: Immutable (like pass by value)
def change_number(x):
    x = 20
    print("Inside change_number:", x)

num = 10
change_number(num)
print("Outside change_number:", num)

# ✅ Original num not changed → behaves like pass by value.

# Example: Mutable (like pass by reference)
def change_list(lst):
    lst.append(4)
    print("Inside change_list:", lst)

lst = [10, 30, 40]
change_list(lst)
print("Outside change_list:", lst)

# ✅ Original list changed → behaves like pass by reference.

# ✅ Takeaway
# Python is NOT strictly pass by value or pass by reference.
# It passes a reference to the object.
# If the object is immutable → looks like value.
# If the object is mutable → looks like reference.

# 👉 Recursive Functions : Recursion in Python refers to when a function calls itself. 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5:", factorial(5))