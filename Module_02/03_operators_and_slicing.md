
# 🧮 The Master Guide to Python Operators & Slicing

Programming mein variables aur data ke sath khelne ke liye humein **Operators** ki zaroorat padti hai. Is file mein hum Python ke sabhi zaroori operators aur sequence data ko kaatne (Slicing) ke tarike ko detail mein samjhenge.

---

## 1. Arithmetic Operators (Maths wale) ➕
Ye operators numbers ke beech mathematical calculation karne ke kaam aate hain.

| Operator | Name | Example (`a=10`, `b=3`) | Result |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `a + b` | `13` |
| `-` | Subtraction | `a - b` | `7` |
| `*` | Multiplication| `a * b` | `30` |
| `/` | True Division | `a / b` | `3.333...` (Hamesha Float deta hai) |
| `//`| Floor Division| `a // b` | `3` (Decimal wala hissa hata deta hai) |
| `%` | Modulus | `a % b` | `1` (Remainder ya Sheshfal batata hai) |
| `**`| Exponentiation| `a ** b` | `1000` ($10^3$) |

```python
# Real-world example: Calculating a total bill
price = 500
tax = 50
total = price + tax
print(f"Total Bill: {total}")
```

---

## 2. Comparison (Relational) Operators ⚖️
Ye do values ko compare karte hain aur hamesha **Boolean** (`True` ya `False`) return karte hain. Inka sabse zyada use `if-else` conditions mein hota hai.

| Operator | Meaning | Example (`x=5`, `y=8`) | Result |
| :--- | :--- | :--- | :--- |
| `==` | Equal to | `x == y` | `False` |
| `!=` | Not equal to | `x != y` | `True` |
| `>` | Greater than | `x > y` | `False` |
| `<` | Less than | `x < y` | `True` |
| `>=` | Greater or equal | `x >= 5` | `True` |
| `<=` | Less or equal | `y <= 5` | `False` |

---

## 3. Logical Operators 🧠
Jab humein ek se zyada conditions ko ek sath check karna ho, tab Logical operators ka use hota hai.

* **`and`**: Dono conditions `True` honi chahiye.
* **`or`**: Koi ek condition bhi `True` ho, toh kaam chal jayega.
* **`not`**: Answer ko ulta kar deta hai (`True` ko `False`, `False` ko `True`).

```python
age = 25
has_license = True

# 'and' ka example
if age >= 18 and has_license:
    print("Aap gaadi chala sakte hain.")

# 'or' ka example
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("Aaj chhutti hai!")
```

---

## 4. Bitwise Operators (Binary Level) 🤖
Ye operators data ko normal numbers ki tarah nahi, balki unke **Binary Format (0s aur 1s)** mein badal kar operate karte hain. Ye thode advanced hain aur mostly hardware programming ya fast mathematical computations mein use hote hain.

Maan lijiye: `a = 10` (Binary: `1010`) aur `b = 4` (Binary: `0100`)

| Operator | Name | Kaam kaise karta hai? | Example (`a & b`) |
| :--- | :--- | :--- | :--- |
| `&` | Bitwise AND | Dono bits 1 hongi tabhi 1 dega. | `1010 & 0100` $\rightarrow$ `0000` (0) |
| `\|` | Bitwise OR | Ek bhi bit 1 hui toh 1 dega. | `1010 \| 0100` $\rightarrow$ `1110` (14)|
| `^` | Bitwise XOR | Dono bits alag hongi tabhi 1 dega. | `1010 ^ 0100` $\rightarrow$ `1110` (14)|
| `~` | Bitwise NOT | Saare 0 ko 1 aur 1 ko 0 kar deta hai. | `~a` $\rightarrow$ `-11` |
| `<<` | Left Shift | Bits ko left khiskata hai (Multiply by 2).| `10 << 1` $\rightarrow$ `20` |
| `>>` | Right Shift | Bits ko right khiskata hai (Divide by 2).| `10 >> 1` $\rightarrow$ `5` |

---

## 5. The Slicing Operator (`[:]`) ✂️
Python mein jab hum kisi String, List, ya Tuple ka ek tukda (slice) nikalna chahte hain, toh hum Slicing ka use karte hain.

**Formula:** `variable_name[start : stop : step]`
* **`start`**: Kahan se shuru karna hai (Default: 0).
* **`stop`**: Kahan rukna hai (Ye index include nahi hota).
* **`step`**: Kitne kadam aage badhna hai (Default: 1).

### Slicing in Action:
```python
text = "PYTHON PROGRAMMING"

# 1. Basic Slicing
print(text[0:6])    # Output: PYTHON (Index 0 se 5 tak)

# 2. Start ya Stop miss karna
print(text[:6])     # Output: PYTHON (Shuru se le kar 5 tak)
print(text[7:])     # Output: PROGRAMMING (7 se aakhiri tak)

# 3. Using Steps (Skip characters)
print(text[0:18:2]) # Output: PTO RGAMN (Har doosra character lega)

# 4. The Magic Reverse
print(text[::-1])   # Output: GNIMMARGORP NOHTYP (String ulti ho gayi!)
```

---

## 💻 Homework / Practice (Jupyter Notebook)

In real-world problems ko solve karke apne logic ko sharp karein:

**Q1. The Even/Odd Shortcut (Arithmetic & Comparison)**
User se ek number lijiye. Modulus operator (`%`) ka use karke check karein ki number Even hai ya Odd.
*(Hint: Agar `number % 2 == 0`, toh Even)*

**Q2. Discount Eligibility (Logical Operators)**
Aap ek e-commerce site bana rahe hain. Ek user ko 20% discount tab milega jab:
- Uska total bill `1000` se zyada ho **AUR** wo ek `premium_member` ho.
- **YA PHIR** uske paas ek `coupon_code` ho.
Variables set karein aur `and`, `or` ka use karke `True` ya `False` mein answer nikalein.

**Q3. File Extension Extractor (Slicing)**
Aapke paas ek file ka naam hai: `filename = "assignment_document.pdf"`
Slicing ka use karke sirf `".pdf"` extract karein aur print karein. *(Hint: Negative indexing ka use karein).*

**Q4. Word Reverser (Slicing)**
Ek variable `word = "DEVELOPER"` banaiye. Slicing ke step operator ka use karke is word ko ulta (reverse) print karein.