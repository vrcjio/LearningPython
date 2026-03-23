# 🧩 Module 2: Python Language Basic Constructs

Is section mein hum Python ke kuch unique aur advanced constructs dekhenge, jaise `Ellipsis`, `Modules`, aur apne code ki galtiyan (Bugs) theek karne ka tarika yani `Debugging`.

---

## 1. Classes aur Modules (Ek Jhalak) 🏗️
Inhe hum aage ke modules mein detail mein padhenge, lekin inka basic idea hona zaroori hai.

* **Classes:** Python mein har cheez ek object hai. `Class` us object ko banane ka naksha (blueprint) hota hai.
* **Modules:** Jab humara code bahut bada ho jata hai, toh hum use alag-alag files mein bant dete hain. Har Python file (`.py`) ek `Module` kehlati hai. Hum doosre modules ko `import` keyword ka use karke apne code mein la sakte hain (jaise `import math`).

---

## 2. Str (String) & Null Object (Quick Recap) 🧵
Humne pichle parts mein inhe detail mein padha hai:
* **Str (String):** Text ko represent karne ke liye (e.g., `"Hello"`).
* **Null Object (`None`):** Jab kisi variable mein koi value nahi hoti, tab hum use `None` assign karte hain. Ye "kuch nahi" ko darshata hai.

---

## 3. The Ellipsis Object (`...`) 🤫
Python mein ek bahut hi special aur unique object hota hai jise **Ellipsis** kehte hain. Ise likhne ke liye hum teen dots `...` ya `Ellipsis` keyword ka use karte hain.

**Iska Use Kahan Hota Hai?**
1. **Placeholder ki tarah:** Jab aap koi function ya loop bana rahe hain par uske andar ka code baad mein likhna chahte hain (jaise `pass` keyword).
2. **Advanced Slicing:** Data Science (NumPy) mein multi-dimensional arrays ko slice karne ke liye.

```python
# Placeholder example using Ellipsis
def calculate_salary():
    ...  # Code baad mein likhunga, abhi error mat dena

print(Ellipsis)  # Output: Ellipsis