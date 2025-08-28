# 👉 for loops

# Problem 1: Print each item in a shopping list
items = input("Enter items for your shopping list: ").split(',')

for item in items:
    print("Buy:", item.strip())

# Problem 2: Print squares of numbers from 1 to n
input_num = int(input("Enter a number: "))

for i in range(1, input_num + 1):
    print("Square of", i, "is", i**2)

# 👉 while loop

# Problem 1: Countdown timer

seconds = int(input("Enter seconds for countdown: "))

while seconds > 0:
    print("Countdown:", seconds)
    seconds -= 1
print("Time's up!")

# Problem 2: Sum until user enters 0

total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Total sum is:", total)

# 👉 Nested for Loops

# Problem 1: Print a multiplication table
multiplication_table = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(multiplication_table, "x", i, "=", multiplication_table * i)

# Problem 2: Print Identity Matrix Pattern

n = 4

for i in range(n):
    for j in range(n):

        if i == j:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

# 👉 Control Flow Statements in Loops

# 1. break
# Problem 1: Stop printing at a target item
shopping_list = ["apple", "banana", "cherry", "date"]

target_item = "cherry"

for item in shopping_list:
    if item == target_item:
        print("Found target item:", item)
        break
    print("Current item:", item)

# Problem 2: Find first even number

while True:
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:
        break
    if num % 2 == 0:
        print("First even number found:", num)
        break
    print("No even number found.")

# 2. continue

# Problem 1: Skip out-of-stock items
inventory = ["apple", "banana", "cherry", "date"]
out_of_stock = ["banana", "date"]

for item in inventory:
    if item in out_of_stock:
        continue
    print("In stock:", item)

# Problem 2: Skip even numbers
n = 10

for i in range(n):
    if i % 2 == 0:
        continue
    print("Odd number:", i)

# 3. pass

# Problem 1: Use pass for future implementation
tasks = ["task1", "task2", "task3"]

for task in tasks:
    if task == "task2":
        pass # Future implementation
    print("Processing", task)

# Problem 2: Pass in empty loop for now
for i in range(5):
    pass


# 👉 Understand Working of for loop

# Example with for loop
nums = [10, 20, 30]

for x in nums:
    print(x)

# Internal working (using iter + next + while)
nums = [10, 20, 30]

# Step 1: get an iterator
it = iter(nums)

# Step 2: keep fetching next item until StopIteration
while True:
    try:
        x = next(it)   # get next element
        print(x)
    except StopIteration:
        break   # no more items → exit loop
