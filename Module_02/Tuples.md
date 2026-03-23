# 🔒 Core Data Structures: Python Tuples

Pichle section mein humne **Lists** dekhi, jo bahut flexible hoti hain. Lekin kabhi-kabhi hum chahte hain ki humara data "Lock" ho jaye aur use koi bhi galti se badal na sake. Yahan entry hoti hai **Tuples** ki.

Tuple bilkul List jaisa ek data structure hai, lekin iska sabse bada rule hai: **Ise ek baar banane ke baad badla nahi ja sakta.**

---

## 1. Creating and Accessing Tuples 🏗️
Lists mein hum square brackets `[]` lagate hain, jabki Tuples mein hum parentheses (gol brackets) `()` ka use karte hain. 

Data nikalne (Indexing aur Slicing) ka tarika bilkul List jaisa hi hota hai.

```python
# Ek Tuple banana
coordinates = (28.7041, 77.1025)  # Delhi ki Location (Latitude, Longitude)

# Indexing (Item nikalna)
print(coordinates[0])  # Output: 28.7041

# Mixed data bhi rakh sakte hain
student_info = ("Aarav", 22, True)
```
🚨 **Pro Tip:** Agar aapko sirf ek item ka tuple banana hai, toh item ke baad comma `,` lagana zaroori hai, warna Python use normal bracket samajh lega. *(Example: `single_tuple = ("Apple",)`)*

---

## 2. The Golden Rule: Immutability 🛑
List aur Tuple ke beech ka sabse bada difference yahi hai. 
* **List:** Mutable (Badli ja sakti hai)
* **Tuple:** Immutable (Nahi badli ja sakti)

Agar aap Tuple mein naya item add karne ki, purana hatane ki, ya value change karne ki koshish karenge, toh Python gussa ho jayega aur `TypeError` dega.

```python
vowels = ('a', 'e', 'i', 'o', 'u')

# vowels[0] = 'A'      # ❌ ERROR! Tuple object does not support item assignment
# vowels.append('x')   # ❌ ERROR! Tuple mein append nahi hota
```
Kyunki Tuples badle nahi ja sakte, inme `.append()`, `.remove()`, ya `.sort()` jaise methods nahi hote. Inme sirf `.count()` aur `.index()` methods kaam aate hain.

---

## 3. Tuple Packing and Unpacking 📦
Yeh Python ka ek bahut hi smart feature hai. 

* **Packing:** Jab hum bina brackets ke values ko comma laga kar likhte hain, toh Python automatically use Tuple bana (pack kar) deta hai.
* **Unpacking:** Hum ek hi line mein Tuple ke saare items ko alag-alag variables mein nikal (unpack kar) sakte hain.

```python
# 1. Tuple Packing
my_data = "Rahul", 25, "Delhi"
print(type(my_data))  # Output: <class 'tuple'>

# 2. Tuple Unpacking (Variables ki ginti Tuple ke items ke barabar honi chahiye)
name, age, city = my_data

print(name)  # Output: Rahul
print(age)   # Output: 25
```

---

## 4. Tuples ka Use Kahan aur Kyun Karein? 💡
Jab humare paas List hai, toh Tuple ki kya zaroorat hai?
1. **Data Safety (Read-Only):** Aisa data jo program chalne ke dauran badalna nahi chahiye (jaise hafte ke din, kisi jagah ke GPS coordinates, ya database ke passwords).
2. **Speed (Performance):** Tuples Lists ke mukable memory mein chote hote hain aur thode fast chalte hain.
3. **Dictionary Keys:** Aage chalkar hum padhenge ki Dictionaries mein hum List ko Key nahi bana sakte, par Tuple ko bana sakte hain kyunki wo immutable hote hain.

---

## 💻 Homework: Tuple Practice (Jupyter Notebook)

**Q1. The Unpacking Master**
Aapke paas ek employee ka data tuple mein hai: `emp_record = ("Emp_101", "Priya Sharma", "HR", 65000)`
* Is tuple ko 4 alag-alag variables (`emp_id`, `name`, `department`, `salary`) mein unpack karein.
* Ek **f-string** ka use karke print karein: *"Priya Sharma works in HR department."*

**Q2. The Immutability Test**
Ek tuple banaiye: `days = ("Monday", "Tuesday", "Wednesday")`
* Code likh kar `days[0]` ko `"Sunday"` karne ki koshish karein.
* Jo Error aayega, use comment `#` mein likhein aur samjhayein ki ye error kyun aaya.

**Q3. The Data Swapper**
Python mein Tuple unpacking ka use karke hum 2 variables ki value ek line mein swap (badal) sakte hain.
```python
a = 10
b = 20
# Yahan apna 1 line ka swapping code likhein (Hint: a, b = ...)
```
Code likhne ke baad dono variables ko print karke check karein.