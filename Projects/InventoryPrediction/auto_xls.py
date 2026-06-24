import pandas as pd
import numpy as np

# 120 dino ka data generate karna
dates = pd.date_range(start="2026-01-01", periods=120)

data = []
for i, dt in enumerate(dates):
    # Weekends (Sat/Sun) par demand high hoti hai
    is_weekend = dt.dayofweek in [5, 6]
    multiplier = 1.6 if is_weekend else 1.0
    
    # Logic setting based on columns
    discount = np.random.choice([0, 5, 10, 15, 20], p=[0.4, 0.3, 0.15, 0.1, 0.05])
    if is_weekend:
        discount = np.random.choice([10, 15, 20]) # Weekends par zyada discount
        
    items_sold = int((400 + (i * 2) + (discount * 5) + np.random.randint(-50, 50)) * multiplier)
    online_orders = int(items_sold * np.random.uniform(0.2, 0.35))
    
    # Spoilage/Kharab samaan tab zyada hota hai jab bikri bohot zyada ho ya stock bacha ho
    spoilage = int(items_sold * 0.06 + np.random.randint(-5, 10))
    if spoilage < 0: spoilage = 0

    data.append({
        "Date": dt.strftime('%Y-%m-%d'),
        "Items_Sold": items_sold,
        "Spoilage_Waste": spoilage,
        "Discount_Percent": discount,
        "Online_Orders": online_orders
    })

df = pd.DataFrame(data)
df.to_excel("grocery_stock_large.xlsx", index=False)
print("🎯 Naye Columns wala Excel 'grocery_stock_large.xlsx' generate ho gaya hai!")