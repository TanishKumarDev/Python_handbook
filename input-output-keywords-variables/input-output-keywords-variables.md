# Python Basics: Input/Output, Variables, and Keywords

## 1. Input and Output in Python

### 1.1 Taking Input
- `input()` is used to take user input and returns it as a **string** by default.

#### Example:
```python
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")
```

#### Output:
```
Enter your name: GeeksforGeeks
Hello, GeeksforGeeks ! Welcome!
```

- The code prompts the user to input their name, stores it in the variable `name`, and prints a greeting.

#### Taking Multiple Inputs
```python
# Two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys:", x)
print("Number of girls:", y)

# Three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students:", x)
print("Number of boys:", y)
print("Number of girls:", z)
```

#### Output:
```
Enter two values: 5 10
Number of boys: 5
Number of girls: 10
Enter three values: 5 10 15
Total number of students: 5
Number of boys: 10
Number of girls: 15
```

#### Typecasting Input
```python
n = int(input("How many roses?: "))
price = float(input("Price of each rose?: "))
color = input("Color of rose?: ")
print(n, price, color)
```

#### Output:
```
How many roses?: 88
Price of each rose?: 50.30
Color of rose?: Red
88 50.3 Red
```

### 1.2 Printing Output
- `print()` displays text, variables, and expressions on the console.

#### Basic Usage:
```python
print("Hello, World!")
```

#### Output:
```
Hello, World!
```

#### Printing Variables:
```python
# Single variable
s = "Bob"
print(s)

# Multiple variables
s = "Alice"
age = 25
city = "New York"
print(s, age, city)
```

#### Output:
```
Bob
Alice 25 New York
```

#### Checking Variable Type:
```python
a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for": 2, "Geeks": 3}

print(type(a), type(b), type(c), type(d), type(e), type(f))
```

#### Output:
```
<class 'str'> <class 'int'> <class 'float'> <class 'tuple'> <class 'list'> <class 'dict'>
```

## 2. Python Variables

### 2.1 Overview
- Variables store data that can be referenced and manipulated.
- No explicit type declaration; type is inferred from the assigned value.

#### Example:
```python
x = 5
name = "Samantha"
print(x, name)
```

#### Output:
```
5 Samantha
```

### 2.2 Rules for Naming Variables
- Can contain letters, digits, and underscores (_).
- Cannot start with a digit.
- Case-sensitive (e.g., `myVar` and `myvar` are different).
- Cannot use Python keywords.

#### Valid Examples:
```python
age = 21
_colour = "lilac"
total_score = 90
```

#### Invalid Examples:
```python
1name = "Error"  # Starts with a digit
class = 10       # Keyword
user-name = "Doe" # Contains hyphen
```

### 2.3 Assigning Values
#### Basic Assignment:
```python
x = 5
y = 3.14
z = "Hi"
```

#### Multiple Assignments:
- Same value:
```python
a = b = c = 100
print(a, b, c)
```

#### Output:
```
100 100 100
```

- Different values:
```python
x, y, z = 1, 2.5, "Python"
print(x, y, z)
```

#### Output:
```
1 2.5 Python
```

### 2.4 Type Casting
- Converts data types using `int()`, `float()`, `str()`.

#### Example:
```python
s = "10"
n = int(s)
f = float(n)
s2 = str(n)
print(n, f, s2)
```

#### Output:
```
10 10.0 10
```

### 2.5 Object Reference
- Variables hold references to objects, not the objects themselves.

#### Example:
```python
x = 5
y = x
x = "Geeks"
y = "Computer"
# x references "Geeks", y references "Computer"
```

### 2.6 Deleting a Variable
- Use `del` to remove a variable.

#### Example:
```python
x = 10
print(x)
del x
# print(x)  # Raises NameError
```

### 2.7 Practical Examples
- Swapping Variables:
```python
a, b = 5, 10
a, b = b, a
print(a, b)
```

#### Output:
```
10 5
```

- Counting Characters:
```python
word = "Python"
length = len(word)
print("Length of the word:", length)
```

#### Output:
```
Length of the word: 6
```

## 3. Python Keywords

### 3.1 Overview
- Reserved words with special meanings; cannot be used as identifiers.

#### List of Keywords:
```python
import keyword
print("The list of keywords is: ")
print(keyword.kwlist)
```

#### Output:
```
The list of keywords is: 
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### 3.2 Categories
| Category           | Keywords                                      |
|--------------------|-----------------------------------------------|
| Value Keywords     | True, False, None                             |
| Operator Keywords  | and, or, not, is, in                          |
| Control Flow       | if, else, elif, for, while, break, continue, pass, try, except, finally, raise, assert |
| Function and Class | def, return, lambda, yield, class             |
| Context Management | with, as                                      |
| Import and Module  | import, from                                  |
| Scope and Namespace| global, nonlocal                              |
| Async Programming  | async, await                                  |

### 3.3 Using Keywords as Variables
- Raises `SyntaxError`.

#### Example:
```python
for = 10  # SyntaxError
```

### 3.4 Keywords vs Identifiers
- **Keywords**: Reserved, fixed (e.g., `if`, `else`).
- **Identifiers**: User-defined (e.g., `x`, `name`).

