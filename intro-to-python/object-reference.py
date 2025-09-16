# 👉 Object Reference
# Step 1: Assign integer value to x
x = 5      # x --> 5
print("x:", x)  

# Step 2: Assign value of x to y
y = x      # y --> 5 (copy of value, not a reference in this case because int is immutable)
print("x:", x)  
print("y:", y)  

# Step 3: Change value of x to a string
x = "admin"   # x --> "admin"
print("x:", x)  
print("y:", y)   # y is still 5, since integers are immutable and assignment made a copy

# Step 4: Change value of y to another string
y = "anotherAdmin"   # y --> "anotherAdmin"
print("x:", x)  
print("y:", y)  

# 🔎 Explanation (References vs Values in Python)

# Integers, strings, and tuples are immutable. Assigning them creates a new object, so changing x doesn’t affect y.

# Lists, dicts, sets (mutable types) behave differently — if y = x and you modify x, y changes too (since both reference the same object).

# 🔎 Example
print("Case 1: Immutable types (int, str, tuple)")
# They don’t share references once reassigned.

# IMMUTABLE EXAMPLE
x = 5
y = x       # y gets a copy of 5

x = 10      # x now points to a NEW integer object
print("Immutable Example:")
print("x:", x)   # 10
print("y:", y)   # 5 (unchanged)

print("Case 2: Mutable types (list, dict, set)")
# They do share references unless you explicitly copy them.

# MUTABLE EXAMPLE
a = [1, 2, 3]
b = a       # b references the SAME list as a

a.append(4) # modify list through 'a'
print("\nMutable Example:")
print("a:", a)   # [1, 2, 3, 4]
print("b:", b)   # [1, 2, 3, 4] (changed too, because both point to same object)


print("Case 3: Breaking the reference (copy)")
# If you want independent copies, use .copy() or list().

# COPY EXAMPLE
p = [10, 20, 30]
q = p.copy()   # creates a NEW list

p.append(40)   # modify only 'p'
print("\nCopy Example:")
print("p:", p)   # [10, 20, 30, 40]
print("q:", q)   # [10, 20, 30] (unchanged, since it's a different object)

# 🔑 Summary:

# Immutable (int, str, tuple): reassignment makes a new object → no shared reference.

# Mutable (list, dict, set): assignment shares reference → both variables see changes.

# Use .copy() or copy.deepcopy() to break references.

