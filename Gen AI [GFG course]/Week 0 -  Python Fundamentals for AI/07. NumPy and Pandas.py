import numpy as np
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to create mock embeddings with NumPy
def create_embeddings(words):
    try:
        # Generate random embeddings (3D vectors for simplicity)
        embeddings = np.random.rand(len(words), 3)
        logging.info("Generated embeddings successfully.")
        return embeddings
    except Exception as e:
        logging.error(f"Error generating embeddings: {e}")
        return None

# Function to process dataset with Pandas
def process_dataset(queries):
    try:
        # Create DataFrame
        df = pd.DataFrame({
            'query': queries,
            'length': [len(q.split()) for q in queries],
            'category': ['question' if '?' in q else 'statement' for q in queries]
        })

        # Clean: Remove queries with length < 2
        df_cleaned = df[df['length'] >= 2].copy()
        
        # Handle missing values (if any)
        df_cleaned = df_cleaned.fillna('unknown')
        
        # Group by category and count
        summary = df_cleaned.groupby('category').agg({'length': ['mean', 'count']})
        
        logging.info("Dataset processed successfully.")
        return df_cleaned, summary
    except Exception as e:
        logging.error(f"Error processing dataset: {e}")
        return None, None

# Example input
queries = [
    "What is AI?",
    "Hello world",
    "How to code?",
    "AI rocks",
    ""
]

# Create embeddings for words
words = ["ai", "world", "code"]
embeddings = create_embeddings(words)

# Process dataset
df, summary = process_dataset(queries)

# Output results
if embeddings is not None:
    print("Mock Embeddings (NumPy):")
    print(embeddings)

if df is not None:
    print("\nCleaned Dataset (Pandas DataFrame):")
    print(df)
    print("\nDataset Summary:")
    print(summary)