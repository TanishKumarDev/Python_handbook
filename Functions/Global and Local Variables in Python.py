# In Python, global variables are declared outside any function and can be accessed anywhere in the program, including inside functions. On the other hand, local variables are created within a function and are only accessible during that function’s execution. This means local variables exist only inside the function where they are defined and cannot be used outside it.


# 👉 Python Local Variables : Local variables are created within a function and exist only during its execution. They're not accessible from outside the function.

# Example 1: In this example, we are creating and accessing a local variable inside a function.
def greet():
    message = "Hello, Local Variable!"
    print(message)
greet()  # Output: Hello, Local Variable!

# Example 2: Trying to access a local variable outside its function will result in an error.
def farewell():
    goodbye_message = "Goodbye, Local Variable!"
    print(goodbye_message)
farewell()  # Output: Goodbye, Local Variable!

# print(goodbye_message)  # Error: NameError: name 'goodbye_message' is not defined

# Error handling
try:
    print(goodbye_message)  # Error: NameError: name 'goodbye_message' is not defined
except NameError:
    print("Error: goodbye_message is not defined")
# 👉 Python Global Variables : Global variables are defined outside all functions. They can be accessed and used in any part of the program, including inside functions.

# Example 1: In this example, we are creating a global variable and then accessing it both inside and outside a function.

msg = "Hello, Global Variable!"

def display_message():
    print("Global Message:", msg)

display_message()  # Output: Hello, Global Variable!
print("Global Message:", msg)  # Output: Hello, Global Variable!

# Example 2: In this example, we're creating a global variable and then using it both inside and outside a function.

def say_farewell():
    print("Inside Function")

msg_farewell = "Goodbye, Global Variable!"

say_farewell()  # Output: Inside Function
print("Outside Function:", msg_farewell)  # Output: Outside Function: Goodbye, Global Variable!

# 👉 Why do we use Local and Global variables in Python?
# If a variable is defined both globally and locally with the same name, the local variable shadows the global variable inside the function. Changes to the local variable do not affect the global variable unless you explicitly declare the variable as global. Example:
def fun():
    s = "Hello, Local Variable!"
    print(s)

s = "Hello, Global Variable!"
fun()  # Output: Hello, Local Variable!
print(s)  # Output: Hello, Global Variable!

# Explanation: Inside fun(), s is a local variable set to "Hello, Local Variable!" and prints that value. Outside, the global s remains "Hello, Global Variable!", so printing s afterward shows the global value.

# 👉 What if We Try to Modify a Global Variable Inside a Function?
def fun_modify():
    s += 'GFG'  
    print("Inside Function", s)

s = "I love Geeksforgeeks"
fun()
# Attempting to change a global variable inside a function without declaring it as global will cause an error
# Explanation: fun() tries to modify s without declaring it global, so Python treats s as local but it’s used before assignment, causing an error. Declaring s as global inside fun() fixes this.

# 👉 Modifying Global Variables Inside a Function
def fun_modify_correct():
    global s  # Declare s as global to modify the global variable
    s += ' GFG'  
    print("Inside Function:", s)
    s = "I love Geeksforgeeks GFG"
    print("Inside Function after reassignment:", s)
s = "I love Geeksforgeeks Globally"

fun_modify_correct()  # Output: Inside Function: I love Geeksforgeeks GFG
print("Outside Function:", s)  # Output: Outside Function: I love Geeksforgeeks GFG

# Explanation: Inside fun(), the global keyword lets Python modify the global variable s directly. The function first appends ' GFG' to "Python is great!", then reassigns s to "Look for Geeksforgeeks Python Section".

# Example 2: This example demonstrates how Python handles global and local variables with the same name, and how the global keyword affects their behavior.

a = 1  # Global variable

def f():
    print('f():', a)  # Uses global a

def g():
    a = 2  # Local variable shadows global
    print('g():', a)

def h():
    global a
    a = 3  # Modifies global a
    print('h():', a)

print('global:', a)  
f()                  
print('global:', a) 
g()                 
print('global:', a)  
h()                  
print('global:', a)

# Explanation:

# f() prints the global a without changing it.
# g() creates a local a that shadows the global one, leaving the global a unchanged.
# h() uses global to modify the global a.
# Only h() changes the global variable, f() and g() do not.