# **Tokenization**
---

## What is Tokenization?

**Tokenization** is the process of converting raw text into smaller meaningful units called **tokens**, which are then converted into numerical representations that AI models can understand.

Think of it like breaking a sentence into "building blocks" that the computer can process.

---

## Tokenization in Action: Real Example

Let's take this sentence and see how different tokenizers process it:
**"I don't like flying! ✈️ It makes me nervous."**

### Step-by-Step Process:

#### Step 1: Text Normalization
- Convert to lowercase: `"i don't like flying! ✈️ it makes me nervous."`
- Remove extra spaces
- Handle punctuation and emojis

#### Step 2: Tokenization Algorithm Applied
*This varies by method - we'll see examples below*

#### Step 3: Vocabulary Mapping
Each token gets mapped to a unique ID from the model's vocabulary.

#### Step 4: Model Processing
These IDs are what the transformer actually processes.

---

## Major Tokenization Algorithms Compared

### 1. **Word-Based Tokenization**
**Concept**: Split text into words using spaces and punctuation.

**Our Example**:
```
Tokens: ["i", "don't", "like", "flying", "!", "✈️", "it", "makes", "me", "nervous", "."]
Token IDs: [25, 134, 89, 2456, 15, 1001, 45, 234, 67, 1456, 14]
```

**Pros**:
- Simple and intuitive
- Preserves word meanings

**Cons**:
- Large vocabulary size
- Can't handle unknown words
- Poor with compound words and morphologically rich languages

**Used in**: Early NLP models, simple text processing

### 2. **Character-Based Tokenization**
**Concept**: Split text into individual characters.

**Our Example**:
```
Tokens: ["i", " ", "d", "o", "n", "'", "t", " ", "l", "i", "k", "e", " ", "f", "l", "y", "i", "n", "g", "!", " ", "✈", "️", " ", "i", "t", " ", "m", "a", "k", "e", "s", " ", "m", "e", " ", "n", "e", "r", "v", "o", "u", "s", "."]
```

**Pros**:
- Very small vocabulary (256 characters max)
- No unknown words
- Handles any text

**Cons**:
- Very long sequences
- Loses word-level meaning
- Computationally expensive

**Used in**: Character-level RNNs, some text generation tasks

### 3. **Subword Tokenization** (Most Popular for LLMs)

#### A. **Byte Pair Encoding (BPE) - Used by GPT models**
**Concept**: Start with characters and merge most frequent pairs iteratively.

**Training Process**:
1. Start with character vocabulary: `{a, b, c, ..., z, ...}`
2. Find most frequent adjacent pair: `"e" + "s" = "es"` (appears 125 times)
3. Merge them, add `"es"` to vocabulary
4. Repeat until target vocabulary size

**Our Example** (with trained BPE):
```
Tokens: ["i", " don", "'", "t", " like", " flying", "!", " ✈", "️", " it", " makes", " me", " nervous", "."]
Token IDs: [25, 148, 12, 23, 345, 1256, 15, 2001, 2002, 245, 567, 89, 1345, 14]
```

**Key Features**:
- **GPT-2/GPT-3/GPT-4** use this
- Handles unknown words by breaking into known subwords
- Good balance between vocabulary size and sequence length

#### B. **WordPiece - Used by BERT**
**Concept**: Similar to BPE but uses a different merging strategy based on likelihood.

**Merging Strategy**: Merge pairs that maximize the language model likelihood of the training data.

**Our Example**:
```
Tokens: ["i", "don", "##'", "##t", "like", "flying", "!", "✈️", "it", "makes", "me", "nervous", "."]
Token IDs: [25, 167, 210, 211, 345, 1256, 15, 2001, 245, 567, 89, 1345, 14]
```

**Key Features**:
- **BERT, DistilBERT** use this
- Uses `##` prefix for subword pieces
- Optimized for masked language modeling

#### C. **SentencePiece - Used by T5, Llama**
**Concept**: Language-agnostic tokenization that works on raw text without pre-tokenization.

**Our Example**:
```
Tokens: ["▁I", "▁don", "'", "t", "▁like", "▁flying", "!", "▁", "✈️", "▁It", "▁makes", "▁me", "▁nervous", "."]
Token IDs: [25, 167, 12, 23, 345, 1256, 15, 8, 2001, 245, 567, 89, 1345, 14]
```

**Key Features**:
- **T5, Llama, Gemma** use this
- Treats text as raw Unicode stream
- `▁` represents space character
- Works with any language without modification

---

## Detailed Comparison Table

| Algorithm | Used By | Vocabulary Size | Handles Unknown Words | Language Support | Key Feature |
|-----------|---------|-----------------|---------------------|------------------|-------------|
| **Word-Based** | Early models | Very Large (50K-200K) | ❌ No | Language-specific | Simple but limited |
| **Character-Based** | Char-RNNs | Very Small (~256) | ✅ Yes | Universal | Handles everything but inefficient |
| **BPE** | **GPT series** | Medium (10K-100K) | ✅ Yes | Good | Balance of efficiency & coverage |
| **WordPiece** | **BERT, DistilBERT** | Medium (10K-100K) | ✅ Yes | Good | Optimized for MLM |
| **SentencePiece** | **T5, Llama, Gemma** | Configurable | ✅ Yes | **Excellent** | Language-agnostic |

---

## Real-World Code Example

Let's see tokenization in action with different models:

```python
from transformers import AutoTokenizer

# Different models use different tokenizers
models = {
    "GPT-2 (BPE)": "gpt2",
    "BERT (WordPiece)": "bert-base-uncased", 
    "T5 (SentencePiece)": "t5-small",
    "Llama 2 (SentencePiece)": "meta-llama/Llama-2-7b-hf"
}

text = "I don't like flying! ✈️ It makes me nervous."

for name, model_name in models.items():
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokens = tokenizer.tokenize(text)
        token_ids = tokenizer.encode(text)
        
        print(f"\n{name}:")
        print(f"Tokens: {tokens}")
        print(f"Token IDs: {token_ids}")
        print(f"Number of tokens: {len(tokens)}")
        
    except Exception as e:
        print(f"\n{name}: Not available - {e}")
```

**Sample Output**:
```
GPT-2 (BPE):
Tokens: ['I', 'Ġdon', "'", 't', 'Ġlike', 'Ġflying', '!', 'Ġ', '✈', '️', 'ĠIt', 'Ġmakes', 'Ġme', 'Ġnervous', '.']
Number of tokens: 15

BERT (WordPiece):
Tokens: ['i', 'don', "'", 't', 'like', 'flying', '!', '[UNK]', 'it', 'makes', 'me', 'nervous', '.']
Number of tokens: 13

T5 (SentencePiece):
Tokens: ['▁I', '▁don', "'", 't', '▁like', '▁flying', '!', '▁', '✈', '️', '▁It', '▁makes', '▁me', '▁nervous', '.']
Number of tokens: 15
```

---

## Why Tokenization Matters for LLM Performance

### 1. **Vocabulary Efficiency**
- **Small vocabularies** → faster training, less memory
- **Large vocabularies** → shorter sequences, faster inference

### 2. **Handling Multiple Languages**
- **SentencePiece** excels here - same tokenizer works for any language
- **BPE/WordPiece** need language-specific training

### 3. **Special Tokens**
All modern tokenizers include special tokens:
- `[CLS]`, `[SEP]` - for BERT's classification tasks
- `<s>`, `</s>` - start/end of sentence
- `<pad>` - padding for equal length sequences
- `<unk>` - unknown tokens

### 4. **Impact on Model Understanding**
- Better tokenization = better understanding of word boundaries and morphology
- Poor tokenization = model struggles with rare words and compounds

---

## Advanced Tokenization Concepts

### 1. **Byte-level BPE** (GPT-4)
- Extends BPE to work at byte level
- Can represent any Unicode character
- Even more robust for multilingual text

### 2. **Unigram Language Model** (SentencePiece option)
- Starts with large vocabulary and removes less probable tokens
- Alternative approach to BPE

### 3. **Custom Tokenization**
You can train your own tokenizer for domain-specific text:

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

# Create and train a custom tokenizer
tokenizer = Tokenizer(BPE())
tokenizer.pre_tokenizer = Whitespace()

trainer = BpeTrainer(vocab_size=10000, special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])
tokenizer.train(files=["your_text_file.txt"], trainer=trainer)

# Save and use
tokenizer.save("custom-tokenizer.json")
```

---

## Key Takeaways

1. **Subword tokenization** (BPE/WordPiece/SentencePiece) dominates modern LLMs
2. **Choice affects performance**: Tokenization impacts model efficiency, multilingual capability, and handling of rare words
3. **Trade-offs exist**: Between vocabulary size, sequence length, and coverage
4. **Modern trend**: Towards byte-level and language-agnostic approaches
5. **Practical implication**: When choosing a model, consider if its tokenizer handles your specific use case (domain-specific terms, languages, etc.)

The tokenization strategy is a fundamental design choice that significantly influences how well an LLM understands and generates text!