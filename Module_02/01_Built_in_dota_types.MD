# 🧱 Module 2: Python Language Basic Constructs (Part 1)

Welcome to Module 2! Is module mein hum Python ke core building blocks ko detail mein samjhenge. Aaj ka focus advanced **Built-in Data Types** aur **Strings** par hoga.

---

## 1. Built-in Data Types in Python 🗂️
Pichle module mein humne basic types (int, float, str, bool) dekhe the. Python mein har cheez ek 'Object' hoti hai. Aaiye kuch aur zaroori data types dekhte hain:

* **Numeric Types:** `int`, `float`, aur `complex` (jaise `3 + 4j`).
* **Sequence Types:** * `str` (String) - Text ke liye.
  * `list` - Multiple items ko ek variable mein store karne ke liye (e.g., `[1, 2, 3]`).
  * `tuple` - List jaisa hi, lekin iski values change nahi ki ja sakti (e.g., `(1, 2, 3)`).
* **Null Object (NoneType):** Python mein `None` ek special keyword hai jiska matlab hota hai "kuch nahi" (Null value).

```python
# Examples of different data **types**
empty_value = None          # NoneType
my_list = ["Apple", "Mac"]  # List
my_tuple = (10, 20, 30)     # Tuple

print(type(empty_value))    # Output: <class 'NoneType'>