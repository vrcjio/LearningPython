
# 🎯 Core Data Structures: Python Sets

Jab humein kisi data mein se duplicates hatane hon ya mathematical calculations (jaise Union, Intersection) karni hon, tab hum **Sets** ka use karte hain. 

Set ek aisi collection hai jisme koi bhi item repeat nahi ho sakta aur inka koi fixed order (index) nahi hota.

---

## 1. Set Create Karna aur "No Duplicates" Rule 🚫
Sets ko curly braces `{}` ka use karke banaya jata hai. Iska sabse bada rule yahi hai ki ye kisi bhi duplicate value ko apne andar nahi rehne deta; use automatically hata deta hai.

```python
# Set create karna
student_ids = {101, 102, 103, 101, 104, 102}

# Print karne par duplicates automatically gayab ho jayenge!
print(student_ids)  # Output: {101, 102, 103, 104}
```
🚨 **Important Note:** Agar aapko ek khali (empty) set banana hai, toh aap `{}` nahi likh sakte (kyunki usse Dictionary ban jati hai). Aapko `set()` likhna hoga.
*(Example: `empty_set = set()`)*

---

## 2. Items Add aur Remove Karna 🛠️
Kyunki Sets mein index (0, 1, 2) nahi hote, isliye hum `.append()` ya `insert()` use nahi kar sakte. Iski jagah hum ye methods use karte hain:

* **`.add(item)`:** Set mein naya item dalne ke liye.
* **`.remove(item)`:** Item hatane ke liye (Agar item nahi mila toh Error aayega).
* **`.discard(item)`:** Item hatane ke liye (Agar item nahi mila toh Error **nahi** aayega - ye safe hai).

```python
colors = {"Red", "Blue"}

colors.add("Green")       # {'Red', 'Blue', 'Green'}
colors.discard("Yellow")  # Koi error nahi aayega, set waisa hi rahega
colors.remove("Red")      # 'Red' hat jayega
```

---

## 3. Mathematical Set Operations 🧮


[Image of Venn diagram showing union intersection difference]


Real-world mein Sets ka sabse zyada use groups ke beech data compare karne ke liye hota hai. Maan lijiye humare paas do groups hain:
* `cricket_team = {"Aman", "Rahul", "Priya"}`
* `football_team = {"Rahul", "Neha", "Aman", "Vikas"}`

### A. Union (`|`) - "Dono groups ko mila do"
Dono teams ke sabhi unique khiladiyon ki list banata hai.
```python
all_players = cricket_team | football_team
print(all_players) # {'Aman', 'Rahul', 'Priya', 'Neha', 'Vikas'}
```

### B. Intersection (`&`) - "Dono mein common kya hai?"
Sirf un logo ko nikalta hai jo dono teams mein hain.
```python
common_players = cricket_team & football_team
print(common_players) # {'Aman', 'Rahul'}
```

### C. Difference (`-`) - "Pehle mein hai, par dusre mein nahi"
Aise khiladi jo sirf Cricket khelte hain, Football nahi.
```python
only_cricket = cricket_team - football_team
print(only_cricket) # {'Priya'}
```

### D. Symmetric Difference (`^`) - "Common walo ko chhod kar baki sab"
Aise khiladi jo sirf ek hi game khelte hain (dono nahi).
```python
one_game_only = cricket_team ^ football_team
print(one_game_only) # {'Priya', 'Neha', 'Vikas'}
```

---

## 💻 Homework: Set Logic Building (Jupyter Notebook)

**Q1. The Duplicate Cleaner**
Aapke paas ek list hai jisme bahut saare duplicate phone numbers hain: 
`phone_list = [9876, 1234, 9876, 5555, 1234, 9999]`
* Is list ko Set mein convert karein taaki duplicates hat jayein.
* Phir us cleaned set ko wapas ek List mein convert karein aur print karein.

**Q2. Friend Recommendation System**
Aapka friend network: `my_friends = {"Aman", "Bhavna", "Chirag", "Deepak"}`
Aapke bhai ka network: `bro_friends = {"Chirag", "Deepak", "Esha", "Farhan"}`
* Intersection (`&`) ka use karke pata lagayein ki aap dono ke "Mutual Friends" kaun hain.
* Union (`|`) ka use karke aap dono ke saare friends ki ek combined unique party list banayein.

**Q3. The Discard vs Remove Test**
Ek set banaiye: `gadgets = {"Phone", "Laptop", "Tablet"}`
* `.remove("Smartwatch")` run karein aur error ko observe karein.
* Code ko theek karke wahan `.discard("Smartwatch")` lagayein aur check karein ki program bina crash hue chal raha hai ya nahi.
