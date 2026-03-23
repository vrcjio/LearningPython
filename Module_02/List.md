
# 📋 Core Data Structures: Python Lists

Ab tak humne ek variable mein sirf ek hi value store ki thi. Par kya ho agar humein 100 students ke marks store karne hon? Yahan kaam aati hain **Lists**. 
List ek aisa container hai jisme hum ek sath bahut saari values store kar sakte hain.

---

## 1. Creating and Accessing Lists 🏗️
Lists ko square brackets `[]` ke andar likha jata hai. Isme hum kisi bhi type ka data (int, string, float, ya Boolean) ek sath rakh sakte hain.

```python
# Ek list banana
shopping_cart = ["Laptop", "Mouse", "Keyboard", "Monitor"]

# Indexing (Item nikalna - 0 se shuru hota hai)
print(shopping_cart[0])   # Output: Laptop
print(shopping_cart[-1])  # Output: Monitor (Last item)

# Slicing (List ka ek tukda nikalna)
print(shopping_cart[1:3]) # Output: ['Mouse', 'Keyboard']
```

---

## 2. Mutability (List ko Modify karna) 🛠️
Lists "Mutable" hoti hain. Iska matlab hai ki list banne ke baad hum uske items ko badal sakte hain, naye items jod sakte hain, ya purane hata sakte hain.

* **`append(item)`:** List ke sabse aakhiri mein naya item jodta hai.
* **`insert(index, item)`:** Kisi specific jagah (index) par naya item jodta hai.
* **`remove(item)`:** List se kisi specific item ko hatata hai (jo pehli baar mile).
* **`pop(index)`:** Kisi specific index wale item ko hatata hai. (Agar index na dein, toh aakhiri item hatata hai aur return karta hai).

```python
fruits = ["Apple", "Mango"]

fruits.append("Banana")        # ['Apple', 'Mango', 'Banana']
fruits.insert(1, "Orange")     # ['Apple', 'Orange', 'Mango', 'Banana']
fruits.remove("Mango")         # ['Apple', 'Orange', 'Banana']
removed_item = fruits.pop()    # 'Banana' hat jayega
print(fruits)                  # Output: ['Apple', 'Orange']
```

---

## 3. Important List Methods 🧮
* **`sort()`:** List ko A-Z ya 0-9 ascending order mein lagata hai.
* **`reverse()`:** List ko poora ulta kar deta hai.
* **`count(item)`:** Pata lagata hai ki ek item list mein kitni baar aaya hai.

```python
marks = [85, 90, 75, 90, 88]

print(marks.count(90))  # Output: 2

marks.sort()
print(marks)            # Output: [75, 85, 88, 90, 90]

marks.reverse()
print(marks)            # Output: [90, 90, 88, 85, 75]
```

---

## 4. Practical Application: Lists aur `for` Loop 🔄
Real-world programming mein hum sabse zyada Lists ke sath `for` loop ka use karte hain. Isse hum list ke har ek item par line-by-line aasani se kaam kar sakte hain.

```python
employees = ["Aman", "Priya", "Rahul"]

# List ke har item par loop chalana
for emp in employees:
    print(f"Sending official email to: {emp}@company.com")
```

---

## 💻 Homework: List Management (Jupyter Notebook)

**Q1. The Inventory Manager**
Aapke paas ek dukan ka saman hai: `inventory = ["Pen", "Notebook", "Eraser"]`
1. `append()` ka use karke `"Marker"` add karein.
2. `insert()` ka use karke index 1 par `"Stapler"` add karein.
3. Final inventory print karein.

**Q2. The Score Analyzer**
Ek cricket team ke pichle 5 matches ke score hain: `scores = [45, 120, 30, 85, 120]`
1. Check karein ki batsman ne `120` kitni baar banaya (`count` use karein).
2. Scores ko chote se bade kram (ascending) mein lagayein (`sort` use karein).

**Q3. The Dynamic To-Do List**
Ek khali list banaiye: `tasks = []`
* `append()` ka use karke isme 3 tasks add karein (jaise "Study", "Gym", "Code").
* Ek `for` loop lagayein jo har task ko is format mein print kare: `"Task to do: [task_name]"`
