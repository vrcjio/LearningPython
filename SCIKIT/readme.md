<div style="background-color: #E0F2F1; padding: 15px 20px; margin: 15px 0px; border-radius: 8px; border-left: 6px solid #008B8B;">
    <h2 style="color: #004D40; margin: 0; font-weight: bold; font-size: 24px;">
        💡 MACHINE LEARNING: MODEL SELECTION CHEAT-SHEET
    </h2>
    <p style="color: #00796B; margin: 5px 0 0 0; font-size: 14px;">
        Dataset ke hisab se sahi Machine Learning Model choose karne ki complete guide.
    </p>
</div>

### 📌 Sabse Bada Rule: Target Variable ko Samjhein
Machine Learning me model dataset ke naam se nahi, balki aapke **Target Variable (jo column predict karna hai)** ke type se decide hota hai. Apne aap se bas **1 sawaal** poochein: *"Mera target column kya hai?"*

---

### 🧮 Case 1: Target Variable ek Number (Continuous Value) hai
Agar aapko koi fix value ya price predict karni hai, toh use **Regression Problem** kehte hain.

*   **Examples:** Ghar ki keemat (Price), Car ka mileage, Kal ka temperature, Heere ki keemat.
*   **Popular Datasets:** California Housing (`sklearn`), Tips (`seaborn`), Diamonds (`seaborn`).
*   **Kaun se Models use karein?**
    1.  `LinearRegression` — *(Basics aur starting ke liye best)*
    2.  `DecisionTreeRegressor` — *(Non-linear data ke liye)*
    3.  `RandomForestRegressor` — *(High accuracy aur complex data ke liye)*

---

### 🏷️ Case 2: Target Variable ek Category (Class/Label) hai
Agar aapko data ko alag-alag groups ya categories me baantna hai, toh use **Classification Problem** kehte hain.

*   **Examples:** Email (Spam ya Not Spam), Phool ka type (Iris), Patient ko bimari hai ya nahi (Yes/No).
*   **Popular Datasets:** Titanic (`seaborn`), Iris (`seaborn` / `sklearn`), Wine (`sklearn`).
*   **Kaun se Models use karein?**
    1.  `LogisticRegression` — *(Binary/Do categories wale data ke liye best)*
    2.  `KNeighborsClassifier` (KNN) — *(Chote aur simple datasets ke liye)*
    3.  `RandomForestClassifier` — *(Zyadatar classification projects ke liye best accuracy)*

---

### 📋 Quick Practice Reference Table

Aap in popular datasets par direct in models ke sath kaam shuru kar sakte hain:


| Dataset Name           | Library | Target Column             | Problem Type       | Best Models to Practice                       |
| :--------------------- | :------ | :------------------------ | :----------------- | :-------------------------------------------- |
| **California Housing** | Sklearn | `MedHouseVal` (Price)     | **Regression**     | Linear Regression, Random Forest Regressor    |
| **Titanic**            | Seaborn | `survived` (0 ya 1)       | **Classification** | Logistic Regression, Decision Tree Classifier |
| **Iris**               | Seaborn | `species` (Phool ka type) | **Classification** | KNN, Logistic Regression, Random Forest       |
| **Tips**               | Seaborn | `tip` (Amount)            | **Regression**     | Linear Regression, Ridge Regression           |

---

### 🚀 Best Workflow For Practice (Sahi Tareeka)
Kisi bhi dataset par master karne ke liye hamesha yeh 3 steps follow karein:
1.  **Baseline Model:** Sabse pehle ek simple model (`Linear` ya `Logistic`) lagayein aur uska accuracy score check karein.
2.  **Advanced Model:** Phir usi data par ek complex model (`Random Forest` ya `Gradient Boosting`) lagayein.
3.  **Comparison:** Dono ke scores ko compare karein aur dekhein ki complex model ne accuracy kitni badhai.
   

------------------------------
## 📋 Machine Learning Hands-on Assignment (Easy to Advance)
## 🌸 1. Iris Flower Dataset (Warm-up / Easy)

**Goal**: Phoolon ki patti (Sepal & Petal) ka size dekhkar unki sahi species/category pehchanna.

* **Problem Type**: Multi-class Classification
* **Import Command**:` import seaborn as sns; df = sns.load_dataset('iris')`
* **Suggested Models**: `DecisionTreeClassifier` ya `RandomForestClassifier`
* **Key Challenge**: Pehla self-code test karna aur `accuracy_score` check karna.

------------------------------
## 🐧 2. Penguins Dataset (Easy)

**Goal**: Penguins ke body features (Flipper length, Bill depth) dekhkar unki sahi species (Adelie, Chinstrap, Gentoo) ko predict karna.

* **Problem Type**: Multi-class Classification
* **Import Command**: `import seaborn as sns; df = sns.load_dataset('penguins')`
* **Suggested Models**: `RandomForestClassifier` ya `KNeighborsClassifier`
* **Key Challenge**: Is dataset me kuch rows me missing values (NaN) hain. Pehle .dropna() ka use karke data ko handle karna seekhein.

------------------------------
## 🚗 3. MPG (Miles Per Gallon) Dataset (Medium)

**Goal**: Car ke features (Cylinders, Horsepower, Weight) dekhkar car ka exact mileage (MPG) predict karna.

* **Problem Type**: Continuous Regression
* **Import Command**: `import seaborn as sns; df = sns.load_dataset('mpg')`
* **Suggested Models**: `LinearRegression` ya `RandomForestRegressor`
* **Key Challenge**: Yeh aapka pehla regression test hai. Isme accuracy score nahi, balki `mean_absolute_error` (MAE) aur `r2_score` calculate karna hai.

------------------------------
## 🩺 4. Pima Indians Diabetes Dataset (Medium)

**Goal**: Patient ke medical reports (Glucose, Blood Pressure, Insulin, Age) ko nikal kar yeh predict karna ki use diabetes hai ya nahi (0 = No, 1 = Yes).

* **Problem Type**: Binary Classification
* **Import Command**:
```python
import pandas as pdurl = "https://githubusercontent.com"
df = pd.read_csv(url, names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigree', 'Age', 'Outcome'])
```

* **Suggested Models**: `LogisticRegression` ya `RandomForestClassifier`
* **Key Challenge**: Data unbalanced hai (Healthy log zyada hain, bimar kam). Train-test-split karte waqt `stratify=y` lagana compulsory hai.

------------------------------
## 🍽️ 5. Restaurant Tips Dataset (Medium)

**Goal**: Total bill, table size, day, aur time ko dekhkar yeh predict karna ki customer lagbhag kitne dollar ki Tip ($ Value) dekar jayega.


* **Problem Type**: Continuous Regression
* **Import Command**: `import seaborn as sns; df = sns.load_dataset('tips')`
* **Suggested Models**: `RandomForestRegressor` ya `HistGradientBoostingRegressor`
* **Key Challenge**: Isme text columns hain (Sex: Male/Female, Smoker: Yes/No). Model me daalne se pehle unhe `pd.get_dummies()` se numeric me badalna seekhein.

------------------------------
## 🚢 6. Titanic: Machine Learning from Disaster (High)

**Goal**: Passenger ki personal details (Class, Age, Sex, Ticket Fare) dekhkar predict karna ki kya woh is samundari hadse me bach paya tha ya nahi (Survived: 0 ya 1).


* **Problem Type**: Binary Classification
* **Import Command**: `import seaborn as sns; df = sns.load_dataset('titanic')`
* **Suggested Models**: `DecisionTreeClassifier` ya `RandomForestClassifier`
* **Key Challenge**: Asli data cleaning challenge! Bohot saari missing values hain jise `.fillna()` se bharna padega aur categorical text data ko convert karna padega.

------------------------------
## 💎 7. Diamond Price Prediction Dataset (High)

**Goal**: Diamond ka weight (Carat), cut, color, aur dimensions dekhkar uski market price ($) predict karna.


* **Problem Type**: Advanced Regression
* **Import Command**: `import seaborn as sns; df = sns.load_dataset('diamonds')`
* **Suggested Models**: `HistGradientBoostingRegressor` ya `RandomForestRegressor`
* **Key Challenge**: Is dataset me 50,000 se zyada rows (Bada data) hain. RandomForest yahan bohot slow chalega, isliye student ko `HistGradientBoostingRegressor` ka real use-case samajh aayega.

------------------------------
## 🏠 8. California Housing Dataset (Expert / Final Challenge)

**Goal**: Kisi area ke logon ki median income, gharon ki age, aur location (Latitude/Longitude) dekhkar wahan ke gharon ki average cost predict karna.


* **Problem Type**: Advanced Regression with Feature Engineering
* **Import Command**:
```python
from sklearn.datasets import fetch_california_housing
import pandas as pd
raw = fetch_california_housing()
df = pd.DataFrame(raw.data, columns=raw.feature_names)
df['Price'] = raw.target
```
* **Suggested Models**: `HistGradientBoostingRegressor` aur model tuning parameters ke saath.
* **Key Challenge**: Purane models ki accuracy ek limit par ruk jayegi. Student ko 85%+ accuracy touch karne ke liye khud se naye columns (Feature Engineering jaise: Rooms per Person) banane honge.

-------
## Stacking Regression 
```python
from sklearn.ensemble import StackingRegressor, HistGradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import RidgeCV
from sklearn.metrics import r2_score

# Step 1: Apni 'Dabang Models' ki team banayein (Base Models)
base_models = [
    ('rf', RandomForestRegressor(n_estimators=50, random_state=42, n_jobs=-1)),
    ('hg', HistGradientBoostingRegressor(random_state=42))
]

# Step 2: Final decision lene wala commander set karein (Meta-Learner)
meta_model = RidgeCV()

# Step 3: Stacking Model taiyar karein
best_model = StackingRegressor(estimators=base_models, final_estimator=meta_model, n_jobs=-1)

# Step 4: Train aur Predict karein (Pehele ki tarah)
best_model.fit(X_train, y_train)
y_pred = best_model.predict(X_test)

# Result Check Karein
print(f"🎯 Stacking Model Ka R2 Score: {r2_score(y_test, y_pred) * 100:.2f}%")

```