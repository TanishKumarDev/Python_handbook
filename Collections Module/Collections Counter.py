# Counters are a subclass of the dict class in Python collections module. They are used to count the occurrences of elements in an iterable or to count the frequency of items in a mapping. 

from collections import Counter

val = Counter(["Python","Java","Python","C","C++","Python"])
ctr = Counter(val)
print(ctr)
print(type(ctr))


# Creating a Counter

# Creating a Counter from a list
ctr1 = Counter([1, 2, 2, 3, 3, 3])

# Creating a Counter from a dictionary
ctr2 = Counter({1: 2, 2: 3, 3: 1})

# Creating a Counter from a string
ctr3 = Counter('hello')

print(ctr1)
print(ctr2)
print(ctr3)

# Accessing Counter Elements

print(ctr1[1]) # ctr1 = Counter([1, 2, 2, 3, 3, 3]) -> 1 occurs 1 time
print(ctr1[2]) # ctr1 = Counter([1, 2, 2, 3, 3, 3]) -> 2 occurs 2 times
print(ctr1[3]) # ctr1 = Counter([1, 2, 2, 3, 3, 3]) -> 3 occurs 3 times

# Updating counters
ctr = Counter([1, 2, 2])

# Adding new elements
ctr.update([2, 3, 3, 3])

print(ctr)

# Counter Methods - 1. elements()

ctr = Counter([1, 2, 2])
items = list(ctr.elements())
print(items)
# Counter Methods - 2. most_common()
ctr = Counter([1, 2, 2])
print(ctr.most_common())
# Counter Methods - 3. subtract()
ctr = Counter([1, 2, 2])
ctr.subtract([2, 3, 3, 3])
print(ctr)
# Counter Methods - 4. total()
ctr = Counter([1, 2, 2])
print(ctr.total())

# Arithmetic Operations on Counters
ctr1 = Counter([1, 2, 2])
ctr2 = Counter([2, 3, 3, 3])

print(ctr1 + ctr2)
print(ctr1 - ctr2)
# print(ctr1 * ctr2)
# print(ctr1 / ctr2)
