x = 5          # Integer
name = "Samantha"  # String

print(x)
print(name)

# valid
age = 21
_colour = "lilac"
total_score = 90


# dynamic typing
x = 10
x = "Now a string"  # Type changed dynamically

# 4. Type Casting

# int() → Convert to integer
# float() → Convert to float
# str() → Convert to string

s = "10"
n = int(s)       # string to int
cnt = 5
f = float(cnt)   # int to float
age = 25
s2 = str(age)    # int to string

print(n)   # 10
print(f)   # 5.0
print(s2)  # 25

# 5. Get Type of Variable
n = 42
f = 3.14
s = "Hello"
li = [1,2,3]
d = {'key':'value'}
flag = True

print(type(n))   # <class 'int'>
print(type(f))   # <class 'float'>
print(type(s))   # <class 'str'>
print(type(li))  # <class 'list'>
print(type(d))   # <class 'dict'>
print(type(flag))# <class 'bool'>

# 6. Object References
x = 5
y = x # y references the same object as x
print(y) # prints 5

x = 10 # x now references a new object
print(y) # y still references the old object, so prints 5

y = 15 # y references another object
print(y) # y now references the new object, so prints 15

# 7. Delete a Variable
z = 100
print(z)  # prints 100

del x # deletes variable x
try:
    print(x)  # raises an error since x is deleted
except NameError:
    print("x is not defined")


# 8. Practical Examples

# Swapping Two Variables:
a, b = 5, 10
a, b = b, a
print("a:", a)  # 10
print("b:", b)  # 5

# Counting Characters in a String:
word = "hello"
len_word = len(word)
print("Length of word:", len_word)  # 5