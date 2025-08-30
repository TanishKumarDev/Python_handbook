# 👉 Pass statement in Python is a null operation or a placeholder. It is used when a statement is syntactically required but we don't want to execute any code. It does nothing but allows us to maintain the structure of our program.

# Example Use of Pass Keyword in a Function
# Pass keyword in a function is used when we define a function but don't want to implement its logic immediately. It allows the function to be syntactically valid, even though it doesn't perform any actions yet.

def my_function():
    pass
my_function()  # Calling the function does nothing

# 👉 Using pass in Conditional Statements
x = 10
if x > 0:
    pass  # Placeholder for future code
else:
    print("x is not positive")
# 👉 Using pass in Loops
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    else:
        print(i)
# 👉 Using pass in Classes
class EmptyClass:
    pass  # No methods or attributes yet

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        pass  # Placeholder for greet method

# Creating an instance of the class
p = Person("Anurag", 30)