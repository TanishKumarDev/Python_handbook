# Chatbot input classifier
user_input = input("Enter your message: ")  # str data type
input_length = len(user_input)              # int: length of input

# Conditional statements to classify input
if input_length < 5:
    response = "Short message, maybe a greeting!"
elif "question" in user_input.lower():
    response = "This seems like a question."
else:
    response = "Looks like a command or statement."

# Arithmetic operator: count words
word_count = len(user_input.split())  # Split string into words

print(f"Response: {response}")
print(f"Word count: {word_count}")