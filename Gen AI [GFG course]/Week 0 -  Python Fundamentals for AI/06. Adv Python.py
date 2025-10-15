import time
import logging
from contextlib import contextmanager

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Decorator to log function execution time
def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Generator to yield words one by one
def word_generator(sentences):
    for sentence in sentences:
        for word in sentence.lower().split():
            yield word

# Context manager for file handling
@contextmanager
def file_handler(filename, mode='r'):
    try:
        file = open(filename, mode)
        yield file
    except FileNotFoundError:
        logging.error(f"File {filename} not found!")
        yield None
    finally:
        if file:
            file.close()
            logging.info(f"File {filename} closed.")

# Function to process text with decorator
@log_time
def process_text(sentences, output_file):
    # Use generator to get words
    words = list(word_generator(sentences))
    
    # Use context manager to write results
    with file_handler(output_file, 'w') as f:
        if f:
            f.write(f"Processed words: {', '.join(words)}\n")
            f.write(f"Total words: {len(words)}\n")
    
    return len(words)

# Example input
sentences = ["AI is awesome", "Python for AI", "GenAI is cool"]
output_file = "output.txt"

# Process and write to file
word_count = process_text(sentences, output_file)
print(f"Total words processed: {word_count}")

# Read and display file content
with file_handler(output_file, 'r') as f:
    if f:
        print("\nFile content:")
        print(f.read())