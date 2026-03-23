# 🧵 The Ultimate Guide to Python Strings (`str`)

Python mein text data ko handle karne ke liye hum **Strings** ka use karte hain. Ek string characters ka ek sequence hota hai. Data Science, Web Development, ya AI—har jagah data cleaning aur processing ke liye strings par master hona sabse zaroori hai.

---

## 1. Creating Strings ✍️
Strings ko single (`' '`), double (`" "`), ya triple (`''' '''` ya `""" """`) quotes mein banaya ja sakta hai.

```python
name = 'Rahul'                 # Single quotes
message = "Learning Python"    # Double quotes
paragraph = """This is a
multi-line string
example."""                    # Triple quotes (Best for documentation/paragraphs)

## 1. Creating Strings ✍️
Strings ko single (`' '`), double (`" "`), ya triple (`''' '''` ya `""" """`) quotes mein banaya ja sakta hai.

```python
name = 'Rahul'                 # Single quotes
message = "Learning Python"    # Double quotes
paragraph = """This is a
multi-line string
example."""                    # Triple quotes (Best for documentation/paragraphs)
```

---

## 2. Escape Characters 🏃‍♂️
Jab humein string ke andar kuch special characters dalne hote hain (jaise nayi line ya quotes), toh hum Backslash `\` ka use karte hain.

* `\n` : New Line
* `\t` : Tab (Space)
* `\'` : Single Quote
* `\\` : Backslash

```python
print("Hello\nWorld")  # 'Hello' aur 'World' alag-alag line mein aayenge
print("He said, \"Python is great!\"") # Quotes ke andar quotes
```

---

## 3. String Indexing & Slicing ✂️
Python mein string ke har character ki ek position hoti hai jise **Index** kehte hain. 
* **Positive Indexing:** Left se Right (`0` se shuru hoti hai)
* **Negative Indexing:** Right se Left (`-1` se shuru hoti hai)

**Slicing Structure:** `string_name[start : stop : step]` (Stop index include nahi hota)

```python
text = "PYTHON"
# P  Y  T  H  O  N
# 0  1  2  3  4  5
#-6 -5 -4 -3 -2 -1

print(text[0])       # Output: P
print(text[-1])      # Output: N
print(text[0:4])     # Output: PYTH (Index 0 se 3 tak)
print(text[1:])      # Output: YTHON (1 se end tak)
print(text[::-1])    # Output: NOHTYP (String ko reverse karne ka best tarika)
```

---

## 4. String Operations & Formatting 🧮

### A. Operations
* **Concatenation (`+`):** Do strings ko jodna.
* **Repetition (`*`):** String ko repeat karna.
* **Membership (`in`, `not in`):** Check karna ki koi word string mein hai ya nahi.

```python
print("Data" + " " + "Science")   # Output: Data Science
print("Hi!" * 3)                  # Output: Hi!Hi!Hi!
print("a" in "apple")             # Output: True
```

### B. Formatting (f-strings) ✨
Python 3.6+ mein variables ko string ke andar daalne ka sabse fast aur padhne mein aasan tarika **f-strings** hai.

```python
user = "Aman"
score = 95
print(f"Congratulations {user}, you scored {score} marks!")
```

---

## 5. Comprehensive String Methods Library 📚
Strings *immutable* hoti hain. Iska matlab hai ki ye methods original string ko nahi badalti, balki ek **nayi string** return karti hain.

### 🔠 Case Manipulation Methods
| Method Structure | Kaam (Description) | Example | Output |
| :--- | :--- | :--- | :--- |
| `upper()` | Sabhi letters ko CAPITAL karta hai. | `"hello".upper()` | `"HELLO"` |
| `lower()` | Sabhi letters ko small karta hai. | `"HELLO".lower()` | `"hello"` |
| `title()` | Har word ka pehla letter Capital karta hai. | `"hello world".title()` | `"Hello World"` |
| `capitalize()` | Sirf puri string ka pehla letter Capital karta hai. | `"hello world".capitalize()` | `"Hello world"` |
| `swapcase()` | Capital ko small aur small ko Capital banata hai. | `"aBcD".swapcase()` | `"AbCd"` |

### 🔍 Searching & Finding Methods
| Method Structure | Kaam (Description) | Example | Output |
| :--- | :--- | :--- | :--- |
| `count(substring)` | Ek word/character kitni baar aaya hai. | `"banana".count("a")` | `3` |
| `find(substring)` | Pehli baar wo word kis index par mila (Nahi mila toh `-1` dega). | `"hello".find("l")` | `2` |
| `index(substring)` | `find` jaisa hi, par nahi milne par Error (ValueError) deta hai. | `"hello".index("l")` | `2` |
| `startswith(prefix)` | Kya string is word se shuru hoti hai? (True/False) | `"python".startswith("py")`| `True` |
| `endswith(suffix)` | Kya string is word par khatam hoti hai? (True/False) | `"file.pdf".endswith(".pdf")`| `True` |

### 🛠️ Modifying & Cleaning Methods
| Method Structure | Kaam (Description) | Example | Output |
| :--- | :--- | :--- | :--- |
| `strip([chars])` | Shuru aur aakhiri ke extra spaces (ya diye gaye characters) hatata hai. | `"  apple  ".strip()` | `"apple"` |
| `replace(old, new, [count])` | Purane word ko naye word se badalta hai. | `"I like Java".replace("Java", "Python")` | `"I like Python"` |
| `zfill(width)` | String ke aage `0` lagakar uski fixed lambaai banata hai. | `"42".zfill(5)` | `"00042"` |

### ✂️ Splitting & Joining Methods
| Method Structure | Kaam (Description) | Example | Output |
| :--- | :--- | :--- | :--- |
| `split(separator)` | String ko tod kar ek List (Array) banata hai. | `"A,B,C".split(",")` | `['A', 'B', 'C']` |
| `join(iterable)` | List ke elements ko string mein jodta hai. | `"-".join(["A", "B", "C"])` | `"A-B-C"` |
| `partition(separator)`| String ko 3 parts ke Tuple mein todta hai (before, sep, after). | `"a+b".partition("+")` | `('a', '+', 'b')` |

### ✅ Validation Methods (Checkers)
Ye sabhi methods `True` ya `False` return karti hain.
* `isalnum()`: Kya string mein sirf Alphabets aur Numbers hain? (Spaces allow nahi hain).
* `isalpha()`: Kya sirf Alphabets hain?
* `isdigit()`: Kya sirf Numbers hain?
* `islower()` / `isupper()`: Kya sabhi letters lower/upper case mein hain?
* `isspace()`: Kya string mein sirf white spaces hain?

---

## 💻 Homework: Real-World Industry Problems (Jupyter Notebook)

Data Science aur Software Development mein strings ko handle karne ke liye in problems ko solve karein:

**Q1. Database Name Formatter (Data Cleaning)**
Aapke paas user ka naam aaya hai jo bahut messy hai: 
`raw_name = "   jOhN dOe   "`
* String methods (`strip` aur `title`) ka use karke is naam ko clean karein taaki database mein ye ekdum sahi format mein save ho: `"John Doe"`.

**Q2. The URL Domain Extractor**
Aap ek web scraper bana rahe hain. Aapke paas ek URL hai: 
`url = "https://www.github.com/vrcjio/LearningPython"`
* String methods (`split` ya slicing) ka use karke sirf domain name nikaliye.
* **Expected Output:** `"github.com"`

**Q3. Indian Phone Number Validator**
Aapko check karna hai ki user ne phone number sahi dala hai ya nahi.
`phone = "+91-9876543210"`
1. Check karein ki kya string `+91-` se shuru hoti hai? (`startswith` use karein).
2. Number se `+91-` ko hatakar sirf 10-digit number print karein. (`replace` ya slicing use karein).
3. Check karein ki bacha hua 10-digit number sirf digits ka bana hai ya nahi. (`isdigit` use karein).

**Q4. The Secret File Renamer**
Aapke paas ek file ka naam hai jisme galti se spaces aa gaye hain:
`filename = "  my  secret  project document .pdf  "`
* `.strip()` se aage-peeche ke spaces hatayein.
* `.replace(" ", "_")` ka use karke beech ke saare spaces ko underscore se badlein.
* Ensure karein ki output ek valid filename ho: `"my__secret__project_document_.pdf"`

**Q5. The Word Counter**
Ek tweet ka text diya gaya hai:
`tweet = "Python is amazing. I love Python. Learning Python is fun!"`
* Find out karein ki is tweet mein `"Python"` word kitni baar use hua hai.

---
*Strings ko master karne ka matlab hai Data ko master karna. Happy Coding! 🚀*
```