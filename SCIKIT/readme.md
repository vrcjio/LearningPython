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
