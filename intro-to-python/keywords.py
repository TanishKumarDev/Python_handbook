# importing keyword module from standard library 'keyword.py'
# It contains a list of all Python keywords
# don't name your file as keyword.py -> it will throw error because instead of looking into stdlib, it will look into current directory 
import keyword 


# kwlist attribute to get a list of all keywords
kwlist = keyword.kwlist
print(kwlist)

# iskeyword() function to check if a string is a keyword
print(keyword.iskeyword("true"))  # False