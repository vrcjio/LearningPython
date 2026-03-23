# 🔀 Master Guide to Control Flow & Loops in Python

Ab tak humara Python code line-by-line seedha chal raha tha. Par real-world softwares aise kaam nahi karte. Unhe decisions lene padte hain aur ek hi kaam ko baar-baar karna padta hai. [cite_start]Iske liye hum **Control Statements (if-else)** aur **Loops (for, while)** ka use karte hain[cite: 14].

---

## 1. Decision Making: `if`, `elif`, `else` ⚖️
Jab humein kisi condition (sahi ya galat) ke aadhar par faisla lena ho, toh hum in statements ka use karte hain. 



* **`if`**: Agar condition True hai, toh yeh block chalega.
* **`elif`** (Else-If): Agar pehli condition False hai, toh doosri condition check karo.
* **`else`**: Agar upar ki saari conditions False hain, toh aakhiri mein yeh chalega.

**Syntax & Indentation:** Python mein blocks ko alag karne ke liye `{}` nahi, balki space (Indentation) ka use hota hai.

```python
# Real-world Example: E-commerce Discount System
cart_value = 1500

if cart_value >= 2000:
    print("Aapko 20% discount mila hai!")
elif cart_value >= 1000:
    print("Aapko 10% discount mila hai!")
else:
    print("Koi discount nahi. Thodi aur shopping karein!")
```

---

## 2. The `for` Loop (Step-by-Step Iteration) 🔄
Jab aapko pehle se pata ho ki code ko kitni baar chalana hai, tab `for` loop ka use best hota hai. Yeh kisi sequence (jaise String, List, ya Range) ke har ek item par ek-ek karke jaata hai.



[Image of Python for loop flowchart]


### A. Looping through a Sequence (List/String)
```python
students = ["Aman", "Priya", "Rahul"]
for name in students:
    print(f"Welcome to the class, {name}!")
```

### B. The `range()` Function
`range(start, stop, step)` humein numbers ki ek list bana kar deta hai.
```python
# 1 se lekar 5 tak numbers print karna (6 include nahi hoga)
for i in range(1, 6):
    print(f"Counting: {i}")
```

---

## 3. The `while` Loop (Condition-Based Iteration) ⏳
`while` loop tab tak chalta hi rehta hai, jab tak uski di gayi condition `True` rehti hai. Isme dhyan rakhna padta hai ki condition kabhi na kabhi `False` ho, warna loop zindagi bhar chalta rahega (Infinite Loop!).



[Image of Python while loop flowchart]


```python
# Real-world Example: Battery draining process
battery = 100

while battery > 90:
    print(f"Battery at {battery}%. Playing game...")
    battery = battery - 2  # Battery kam ho rahi hai

print("Battery is 90% or below. Please plug in charger!")
```

---

## 4. Loop Control Statements (`break` & `continue`) 🛑
[cite_start]Kabhi-kabhi humein loop ke normal flow ko beech mein rokna ya skip karna padta hai[cite: 14].

### A. The `break` Statement
[cite_start]`break` ka kaam hai loop ko turant wahin tod dena aur code ko loop ke bahar nikal lena[cite: 14].

```python
# Hazaaron files mein se ek specific file dhoondhna
files = ["doc.txt", "image.png", "secret_code.py", "video.mp4"]

for file in files:
    print(f"Checking {file}...")
    if file == "secret_code.py":
        print("Mil gaya! Stopping search.")
        break  # Loop yahan ruk jayega
```

### B. The `continue` Statement
[cite_start]`continue` loop ko todta nahi hai, balki sirf us current round (iteration) ko skip karke seedha agle round par chala jaata hai[cite: 14].

```python
# 1 se 5 tak print karna hai, par 3 ko skip karna hai
for num in range(1, 6):
    if num == 3:
        continue  # 3 aate hi neeche ka code skip ho jayega
    print(num)
# Output: 1, 2, 4, 5
```

---

## 5. Pro-Tip: The `else` with Loops 🤯
[cite_start]Python mein ek bahut unique feature hai: aap `for` aur `while` loop ke sath bhi `else` laga sakte hain[cite: 14]. 
* Yeh `else` block tabhi chalta hai jab loop **bina `break` hue** naturally pura khatam ho jaye.

```python
# Check if a number is prime
search_num = 10
for i in range(1, 5):
    if i == search_num:
        print("Number found!")
        break
else:
    print("Pura loop chal gaya par number nahi mila.")
```

---

## 💻 Homework: Industry Level Logic Building (Jupyter Notebook)

Aapne ab tak variables, strings, operators aur loops seekh liye hain. Inhe mila kar in problems ko solve karein:

**Q1. The ATM Pin Validator (`while` loop & `break`)**
Aapke system mein sahi PIN `1234` hai. Ek `while` loop likhein jo user se PIN check kare. 
* Agar PIN galat hai, toh loop wapas chalna chahiye. 
* Agar PIN sahi hai, toh `"Access Granted"` print karein aur `break` kar dein.
*(Hint: Abhi ke liye aap ek list `attempts = [1111, 2222, 1234]` bana kar uspe loop chala sakte hain).*

**Q2. The Vowel Counter (`for` loop & `if`)**
Aapke paas ek string hai: `sentence = "Python is amazing and easy to learn"`
Ek code likhein jo is sentence mein iterate kare aur count kare ki total kitne vowels (a, e, i, o, u) hain. Total count print karein.

**Q3. The Skip-the-Evens Challenge (`for` loop & `continue`)**
`range(1, 21)` ka use karke 1 se 20 tak ka loop lagayein. 
* Agar number Even (sam) hai, toh use `continue` karke skip kar dein.
* Agar number Odd (visham) hai, toh use print karein.

**Q4. FizzBuzz (The Classic Interview Question)**
1 se 50 tak numbers print karein, lekin:
* Agar number 3 se divide hota hai, toh number ki jagah `"Fizz"` print karein.
* Agar number 5 se divide hota hai, toh `"Buzz"` print karein.
* Agar number 3 aur 5 **dono** se divide hota hai (jaise 15), toh `"FizzBuzz"` print karein.
* Baki numbers normal print honge.

---
*Logic building is the heart of software engineering. Keep practicing! 🚀*
