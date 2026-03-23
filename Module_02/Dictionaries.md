# 📖 Core Data Structures: Python Dictionaries

Real-world data (jaise user profiles ya product details) hamesha ek simple list ki tarah nahi hota. Kabhi-kabhi humein data ko ek "Label" ya "Naam" dena padta hai taaki use aasani se dhoondha ja sake. Iske liye hum **Dictionaries** ka use karte hain.



---

## 1. The Key-Value Concept 🔑
Sochiye ek real-world Phonebook ke baare mein. Usme aap kisi ka **Naam** (Key) dhoondhte hain, aur aapko uska **Phone Number** (Value) mil jata hai. 

Python Dictionary bilkul aise hi kaam karti hai. Isme data hamesha `Key: Value` ke jode (pairs) mein store hota hai.

---

## 2. Creating and Accessing Data 🏗️
Dictionaries ko curly braces `{}` se banaya jata hai. Data nikalne ke liye hum Index (0, 1, 2) ka use nahi karte, balki **Key** ka use karte hain.

```python
# Ek student ki dictionary banana
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

# Data access karna (Key ka use karke)
print(student["name"])    # Output: Rahul

# .get() method ka use (Safe tarika)
# Agar key nahi milti, toh error nahi aayega, 'None' aayega
print(student.get("marks"))  # Output: None
```

---

## 3. Adding & Updating Data 🛠️
Dictionary mutable hoti hai. Aap isme nayi keys add kar sakte hain aur purani keys ki values ko update (badal) sakte hain.

```python
# Purani key ki value update karna
student["age"] = 21

# Nayi key aur value add karna
student["city"] = "Indore"

print(student) 
# Output: {'name': 'Rahul', 'age': 21, 'course': 'Python', 'city': 'Indore'}
```

---

## 4. Important Dictionary Methods 🧰
Jab dictionary bahut badi ho, toh uske data ko alag-alag nikalne ke liye hum in methods ka use karte hain:

| Method | Kaam (Description) | Example | Output |
| :--- | :--- | :--- | :--- |
| `.keys()` | Sirf saari Keys ki list deta hai. | `student.keys()` | `dict_keys(['name', 'age', 'course'])` |
| `.values()` | Sirf saari Values ki list deta hai. | `student.values()` | `dict_values(['Rahul', 20, 'Python'])` |
| `.items()` | Key aur Value dono ka ek pair (Tuple) deta hai. | `student.items()` | `dict_items([('name', 'Rahul'), ...])` |

---

## 5. Practical Application: Looping through a Dictionary 🔄
Real-world projects mein hum `.items()` ka sabse zyada use karte hain taaki `for` loop ki madad se Key aur Value dono ko ek sath print kar sakein.

```python
user_profile = {
    "username": "coder_aman",
    "email": "aman@test.com",
    "status": "Active"
}

# Key aur Value par ek sath loop chalana
for key, value in user_profile.items():
    print(f"{key.title()}: {value}")

# Output:
# Username: coder_aman
# Email: aman@test.com
# Status: Active
```

---

## 💻 Homework: Dictionary Logic Building (Jupyter Notebook)

**Q1. The Employee Database**
Ek dictionary banaiye: `employee = {"emp_id": 101, "name": "Neha", "department": "IT"}`
* Isme ek nayi key `"salary"` add karein jiski value `55000` ho.
* `"department"` ko update karke `"HR"` kar dein.
* Final dictionary ko print karein.

**Q2. The Safe Extractor**
Aapke paas ek dictionary hai: `config = {"theme": "dark", "language": "English"}`
* Bina program ko crash kiye (Error laye), `"font_size"` key ki value nikalne ki koshish karein. *(Hint: `.get()` method ka use karein).*
* Agar `"font_size"` nahi milta, toh default value `"12px"` print honi chahiye.

**Q3. The Bill Generator (`for` loop)**
Aapke paas ek restaurant ke bill ki dictionary hai jisme items aur unke prices hain:
`menu_prices = {"Pizza": 250, "Burger": 100, "Pasta": 150, "Coffee": 80}`
* Ek `for` loop aur `.values()` method ka use karke in sabhi prices ka Total Sum calculate karein aur print karein. *(Hint: Loop se pehle `total = 0` variable set karein).*
