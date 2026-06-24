import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, StackingRegressor
from sklearn.linear_model import Ridge
from xgboost import XGBRegressor
import joblib

# Paths setup
MODEL_DIR = "models"
MODEL_FILE = os.path.join(MODEL_DIR, "shop_model.pkl")
META_DATA_FILE = os.path.join(MODEL_DIR, "model_meta.json")

def create_time_features(df, target_col):
    """
    🧠 SMART FEATURE ENGINEERING ENGINE:
    Bina user se extra input liye, Date aur Target Column se 
    automatic X (Features) aur Y (Target) generate karna.
    """
    df = df.copy()
    
    # Sort data by date strictly
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('by=Date' if 'by=Date' in df.columns else 'Date')
    
    # 1. Calendar/Time Features (Model samajh payega kis din sales badhti hai)
    df['Day_of_Week'] = df['Date'].dt.dayofweek
    df['Is_Weekend'] = df['Date'].dt.dayofweek.isin([5, 6]).astype(int)
    df['Month'] = df['Date'].dt.month
    
    # 2. Lag Features (Purani sales ko hi naya input banana)
    # Lag 1: Pichle 1 din pehle ki sales
    df['Lag_1'] = df[target_col].shift(1)
    # Lag 2: Pichle 2 din pehle ki sales
    df['Lag_2'] = df[target_col].shift(2)
    # Lag 7: Pichle 1 hafte pehle ki sales (Weekly pattern pakadne ke liye)
    df['Lag_7'] = df[target_col].shift(7)
    
    # 3. Rolling Mean (Pichle 3 dino ka average trend)
    df['Rolling_Mean_3'] = df[target_col].shift(1).rolling(window=3).mean()
    
    # Drop rows jisme shifting ki wajah se NaN values aayi hain
    df_clean = df.dropna().copy()
    
    # Features aur Target list select karna
    feature_cols = ['Day_of_Week', 'Is_Weekend', 'Month', 'Lag_1', 'Lag_2', 'Lag_7', 'Rolling_Mean_3']
    
    X = df_clean[feature_cols].values
    y = df_clean[target_col].values
    
    return X, y, feature_cols, df_clean

def train_advanced_stacking_model(df, target_col):
    """
    Advanced Machine Learning Engine using Stacking Regressor 
    (Random Forest + XGBoost optimized with Ridge Meta-Learner)
    """
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)
        
    # Minimum rows data check
    if len(df) < 10:
        return False, ""Model training requires a minimum of 10 days of historical data!"
        
    try:
        # Prepare Features
        X, y, feature_cols, df_clean = create_time_features(df, target_col)
        
        if len(X) < 2:
            return False, "Insufficient data remaining after generating lag features. Please add more rows."

        # Base Models define karna
        base_estimators = [
            ('rf', RandomForestRegressor(n_estimators=100, max_depth=6, random_state=42)),
            ('xgb', XGBRegressor(n_estimators=100, max_depth=4, learning_rate=0.05, random_state=42))
        ]
        
        # Stacking Regressor setup (Dono models ko Ridge combine karega)
        stacking_pipeline = StackingRegressor(
            estimators=base_estimators,
            final_estimator=Ridge()
        )
        
        # Train the model
        stacking_pipeline.fit(X, y)
        
        # Model ko file me save karna (.pkl)
        joblib.dump(stacking_pipeline, MODEL_FILE)
        
        # Meta information save karna taaki Predictor ko pata rahe last data state kya tha
        import json
        meta_data = {
            "target_column": target_col,
            "feature_columns": feature_cols,
            "last_date": df_clean['Date'].max().strftime('%Y-%m-%d'),
            "last_sales_values": df_clean[target_col].tail(7).tolist() # Last 7 values for next lag injection
        }
        with open(META_DATA_FILE, "w") as f:
            json.dump(meta_data, f)
            
        return True, "AI Stacking Model successfully trained and updated!"
        
    except Exception as e:
        return False, f"Training Error: {str(e)}"

def predict_next_days(df, days_to_predict=1):
    """
    🔮 FUTURE FORECASTER:
    Bina user ke input diye, next timeline (Day/Week/Month) automatic forecast karna.
    """
    if not os.path.exists(MODEL_FILE) or not os.path.exists(META_DATA_FILE):
        return None, "Please train the AI model via the control panel first!"
        
    try:
        # Load Model aur Meta-Data
        model = joblib.load(MODEL_FILE)
        import json
        with open(META_DATA_FILE, "r") as f:
            meta = json.load(f)
            
        target_col = meta["target_column"]
        
        # Pure DataFrame se wapas fresh features generate karna till the last date
        _, _, _, df_clean = create_time_features(df, target_col)
        
        predictions = []
        future_dates = []
        
        # Humari pipeline ka dynamic rolling dataset creation
        current_data = df_clean.copy()
        
        for i in range(days_to_predict):
            # 1. Agle din ki date calculate karna
            last_date = pd.to_datetime(current_data['Date'].iloc[-1])
            next_date = last_date + pd.Timedelta(days=1)
            future_dates.append(next_date)
            
            # 2. Next day ke liye automatic testX row generate karna
            day_of_week = next_date.dayofweek
            is_weekend = 1 if day_of_week in [5, 6] else 0
            month = next_date.month
            
            # Lags uthana dynamic history se
            lag_1 = current_data[target_col].iloc[-1]
            lag_2 = current_data[target_col].iloc[-2]
            lag_7 = current_data[target_col].iloc[-7] if len(current_data) >= 7 else lag_2
            rolling_3 = current_data[target_col].iloc[-3:].mean()
            
            # Ek testX single row structure banana
            testX = np.array([[day_of_week, is_weekend, month, lag_1, lag_2, lag_7, rolling_3]])
            
            # Predict next step
            pred_val = model.predict(testX)[0]
            if pred_val < 0: pred_val = 0 # Sales ya target negative nahi ho sakta
            predictions.append(pred_val)
            
            # 3. Dynamic Append: Is predicted value ko temporary dataset me daalna 
            # taaki iske agle din (Day 2) ke prediction me ye khud Lag bankar kaam aaye!
            new_row = pd.DataFrame([{
                'Date': next_date,
                target_col: pred_val,
                'Day_of_Week': day_of_week,
                'Is_Weekend': is_weekend,
                'Month': month,
                'Lag_1': lag_1, 'Lag_2': lag_2, 'Lag_7': lag_7, 'Rolling_Mean_3': rolling_3
            }])
            current_data = pd.concat([current_data, new_row], ignore_index=True)
            
        # Clear DataFrame return karna graphs ke liye
        result_df = pd.DataFrame({
            'Date': future_dates,
            f'Predicted_{target_col}': predictions
        })
        
        return result_df, None
        
    except Exception as e:
        return None, f"Prediction Engine Error: {str(e)}"