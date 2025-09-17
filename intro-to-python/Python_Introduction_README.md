# Python Introduction

## 1. What is Python?
- High-level programming language (close to English).
- Created in 1991 by Guido van Rossum.
- Known for readability and fewer lines of code.
- Works on Windows, Linux, MacOS.
- Has tons of libraries for web, ML, AI, automation, etc.
- Variable types are automatically detected (no need to declare int, string like C++/Java).
- Supports multiple paradigms:
  - Procedural (step by step)
  - Object-oriented (classes, objects)
  - Functional (functions, lambda expressions)

---

## 2. First Python Program – Hello World

### Code:
```python
# This is a single-line comment
print("Hello, World!")  # print() displays text
```

### Output:
```
Hello, World!
```

---

## 3. How It Works
- `print()` → Built-in Python function for output.
- `"Hello, World!"` → A string (text). Strings are enclosed in `'` or `"`. 
- `#` → Single-line comment, ignored by Python.
- Multi-line comment → Use triple quotes (`'''` or `"""`).

### Example:
```python
"""
This is a multi-line comment
Python will ignore everything here
"""
print("Learning Python")
```

---

## 4. Indentation in Python
Unlike C++/Java (which use { }), Python uses indentation (spaces or tabs) to define code blocks.

### Example – Wrong code:
```python
print("Line 1")
    print("Line 2")  # This will cause error
```

### Output:
```
IndentationError: unexpected indent
```

### Correct code:
```python
print("Line 1")
print("Line 2")  # Both at same indentation level
```

---

## 5. Famous Apps Built with Python
- YouTube – video streaming.
- Instagram – backend scaling.
- Spotify – ML-based music recommendation.
- Dropbox – file storage.
- Netflix – recommendation engine.
- Uber, Pinterest, Google – many services use Python.

---

## 6. Where Python is Used
- Web Dev – Django, Flask.
- Data Science/ML – NumPy, Pandas, TensorFlow, PyTorch.
- Automation – scripting repetitive tasks.
- Game Dev – Pygame.
- IoT – Raspberry Pi, MicroPython.
- DevOps/Cloud – automation tools.
- Cybersecurity – ethical hacking scripts.

---

## 7. Dry Run of Hello World
Let’s dry run the simple code:
```python
print("Hello, World!")
```

**Step-by-step:**
1. Interpreter sees `print("Hello, World!")`.
2. `"Hello, World!"` is a string literal.
3. `print()` function sends it to the console.
4. Screen shows → `Hello, World!`.

---

## 8. Internal Working of Python

### Step 1: You write Python code (.py file).
Example:
```python
print("Hello, World!")
```

### Step 2: Python Interpreter starts.
When you run `python file.py`, here’s what happens internally:

1. **Compilation (to Bytecode)**
   - Python first compiles your code into bytecode.
   - Bytecode is a low-level, platform-independent representation of your code.
   - This happens automatically — you don’t see .class files like in Java.
   - Python may store these in a `__pycache__` folder as `.pyc` files for faster execution next time.

2. **Interpretation (by Python Virtual Machine – PVM)**
   - The bytecode is then sent to the PVM (Python Virtual Machine).
   - PVM executes the bytecode line by line on your machine.
   - That’s why Python is called an interpreted language.

---

## 9. Flow Diagram
```
Your Code (.py) 
     ↓  (Compilation step)
Bytecode (.pyc in __pycache__) 
     ↓  (Interpretation step)
Python Virtual Machine (PVM) executes it
     ↓
Output
```

---

## 10. Key Points
- Python is both compiled and interpreted.
  - Compiled → into bytecode.
  - Interpreted → bytecode is run by PVM.
- Compilation is hidden from you (automatic).
- That’s why Python runs slower than C/C++ (which compiles directly to machine code).
- But Python is flexible and cross-platform because the bytecode can run anywhere with PVM.

---

## 11. Example with Hello World
1. `print("Hello, World!")` → compiled into bytecode.
2. Bytecode sent to PVM.
3. PVM executes `print` instruction.
4. Console displays:
```
Hello, World!
```
