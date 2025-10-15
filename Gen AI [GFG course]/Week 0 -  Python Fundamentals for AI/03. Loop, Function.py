# Function to process text input
def process_text(sentences):
    # Initialize data structures
    word_list = []          # List to store all words
    word_freq = {}          # Dictionary for word frequencies
    unique_words = set()    # Set for unique words
    short_words = []        # List for words with length < 4

    # Loop through each sentence
    for sentence in sentences:
        words = sentence.lower().split()  # String: split into words
        word_list.extend(words)           # Add to list
        unique_words.update(words)        # Add to set (unique)

        # Count word frequencies
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        # Filter short words
        for word in words:
            if len(word) < 4 and word not in short_words:
                short_words.append(word)

    return {
        "total_words": len(word_list),
        "word_frequencies": word_freq,
        "unique_words": unique_words,
        "short_words": tuple(short_words)  # Tuple for fixed output
    }

# Example input
user_inputs = [
    "Hello world AI",
    "AI is awesome",
    "Hello AI world"
]

# Call function
results = process_text(user_inputs)

# Output results
print("Total words:", results["total_words"])
print("Word frequencies:", results["word_frequencies"])
print("Unique words:", results["unique_words"])
print("Short words (tuple):", results["short_words"])