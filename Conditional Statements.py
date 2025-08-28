# If Conditional Statement in Python
age = 20

if age >= 18:
    print("You are eligible to vote.")

# inshort
if age >= 18: print("You are eligible to vote.")

# If else Conditional Statements in Python
age = 15

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# inshort
marks = 4
res = "Pass" if marks >= 40 else "Fail"
print("Result:", res)

# elif Statement
age = 65

if age < 12:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 35:
    print("You are a young adult.")
else:
    print("You are an old old.")

# Nested if..else Conditional Statements in Python

# Ternary Conditional Statement in Python

age = 20
print("You are eligible to vote." if age >= 18 else "You are not eligible to vote.")

# Match-Case Statement in Python

num = 3

match num:

    case 1:
        print("Number is One")
    case 2:
        print("Number is Two")
    case 3:
        print("Number is Three")
    case _:
        print("Number is something else")