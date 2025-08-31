#----------Getting List of all Python Keywords----------
import keyword

print("Python Keywords:")
print(keyword.kwlist) # printing all keywords at once using "kwlist"

#----------What Happens if We Use Keywords as Variable Names----------
# Example (Uncommenting below line will cause SyntaxError)
# for = 5

#----------How to Identify Python Keywords----------
def is_keyword(word):
    # return word in keyword.kwlist
    return keyword.iskeyword(word) # programmatically checks if a name is a keyword, preventing errors.

print(is_keyword("def"))    # True
print(is_keyword("hello"))  #