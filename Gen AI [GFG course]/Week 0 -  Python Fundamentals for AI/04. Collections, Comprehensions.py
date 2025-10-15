from collections import Counter, namedtuple
# Define a namedtuple for structured output
Result = namedtuple('Result', ['word_counts', 'filtered_words'])

# Class for text preprocessing
class TextProcessor:
    def __init__(self, min_length=3):
        self.min_length = min_length  # Attribute: minimum word length
        self.word_counts = Counter()  # Counter for word frequencies

    def process_sentences(self, sentences):
        # List comprehension: split sentences into words and filter by length
        all_words = [word.lower() for sentence in sentences for word in sentence.split()]
        filtered_words = [word for word in all_words if len(word) >= self.min_length]

        # Update word counts
        self.word_counts.update(all_words)

        # Return structured result
        return Result(word_counts=self.word_counts, filtered_words=filtered_words)

    def get_stats(self):
        # Dictionary comprehension: create stats
        stats = {word: count for word, count in self.word_counts.items() if count > 1}
        return stats

# Example input
sentences = ["AI is awesome", "AI and Python rock", "Python is cool"]

# Create object and process data
processor = TextProcessor(min_length=3)
result = processor.process_sentences(sentences)

# Output results
print("Word Counts:", result.word_counts)
print("Filtered Words (length >= 3):", result.filtered_words)
print("Words appearing more than once:", processor.get_stats())