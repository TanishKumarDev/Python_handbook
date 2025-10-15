import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom exception
class InvalidInputError(Exception):
    pass

# Function to process text
def process_user_input(user_input):
    try:
        # Check for empty input
        if not user_input.strip():
            raise InvalidInputError("Input cannot be empty!")
        
        # Check for non-string input (simulated by checking if all characters are digits)
        if user_input.isdigit():
            raise TypeError("Input must be text, not numbers!")
        
        # Process input
        words = user_input.split()
        word_count = len(words)
        
        # Log success
        logging.info(f"Processed input: '{user_input}' with {word_count} words")
        return word_count
    
    except InvalidInputError as e:
        logging.error(f"Invalid input error: {e}")
        return None
    except TypeError as e:
        logging.error(f"Type error: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None
    finally:
        logging.info("Processing attempt completed.")

# Test cases
test_inputs = [
    "Hello AI world",  # Valid input
    "",                # Empty input
    "12345",           # Invalid: numbers only
    "AI is cool"       # Valid input
]

# Process each input
for input_text in test_inputs:
    print(f"\nInput: '{input_text}'")
    result = process_user_input(input_text)
    if result is not None:
        print(f"Word count: {result}")