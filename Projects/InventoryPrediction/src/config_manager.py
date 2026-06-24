import os
import json
import pandas as pd
import numpy as np

# Path definition globally managed
CONFIG_FILE = os.path.join("data", "config.json")

def initialize_config():
    """Ensure data directory and config.json exist on startup"""
    if not os.path.exists("data"):
        os.makedirs("data")
        
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            json.dump({"saved_file_path": ""}, f)

def get_valid_file_path():
    """
    Check if a path exists in JSON AND actually exists on the disk (os.path).
    Returns path string if valid, else returns empty string.
    """
    initialize_config()
    try:
        with open(CONFIG_FILE, "r") as f:
            config_data = json.load(f)
            path = config_data.get("saved_file_path", "")
            
            # Twist handling: File check via os.path
            if path and os.path.exists(path):
                return path
            else:
                # Agar file delete ya move ho gayi hai, toh save path ko reset karo
                save_file_path("")
                return ""
    except (json.JSONDecodeError, FileNotFoundError):
        return ""

def save_file_path(file_path):
    """Saves the selected valid file path permanently to JSON configuration"""
    initialize_config()
    with open(CONFIG_FILE, "w") as f:
        json.dump({"saved_file_path": file_path}, f)

def validate_and_load_data(file_path):
    """
    Validates if the file format is correct and checks for the mandatory 'Date' column.
    Returns (DataFrame, None) if successful, or (None, ErrorMessage) if failed.
    """
    if not os.path.exists(file_path):
        return None, "File does not exist or was deleted!"
        
    try:
        # Dynamic pandas execution based on extension
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file_path)
        else:
            return None, "Unsupported file format! Please upload CSV or Excel."
            
        # SMART UPDATE: Sirf 'Date' column compulsory hai time-series aur groups ke liye
        if "Date" not in df.columns:
            return None, "Missing 'Date' column! Please ensure your sheet has a column named 'Date'."
            
        # Date column ko safe parsing dena
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Date']) # Corrupt dates nikalna
        df = df.sort_values(by='Date') # Timeline format me maintain rakhna
        
        return df, None
        
    except Exception as e:
        return None, f"Error processing file: {str(e)}"

def get_ai_suggestions(df, target_column):
    """
    🧠 AI CORRELATION BRAIN:
    Check karta hai ki Target Column ke sath baaki numeric columns me se
    sabse best predictor (Highest Pearson Correlation) kaun sa hai.
    """
    try:
        # Sirf numeric columns filter karna (Date/String ko chhodkar)
        numeric_df = df.select_dtypes(include=[np.number])
        
        if target_column not in numeric_df.columns or len(numeric_df.columns) <= 1:
            return None, "Insufficient numeric columns for AI Analysis."
            
        # Target ke sath baaki columns ka correlation nikalna
        correlations = numeric_df.corr()[target_column].drop(target_column)
        
        if correlations.empty:
            return None, "No features found to correlate."
            
        # Sabse max impact dalne wala feature select karna
        best_feature = correlations.abs().idxmax()
        correlation_value = correlations[best_feature]
        
        suggestion_text = f"💡 AI Suggestion: '{best_feature}' column has the highest correlation with '{target_column}' (Score: {correlation_value:.2f}). We recommend using it for training."
        
        return best_feature, suggestion_text
    except Exception as e:
        return None, f"AI Suggestion Error: {str(e)}"