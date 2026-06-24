import time
import schedule
import os
import json
import logging

# Internal modules import
import config_manager as cm
import ml_engine as mle

# Setup background logging mechanism taaki pata chale automation chal raha hai ya nahi
LOG_FILE = os.path.join("data", "scheduler_log.txt")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - [AI SCHEDULER] - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def auto_train_job():
    """🎯 BACKGROUND AUTOMATION JOB: Automatically updates model weights"""
    logging.info("Scheduled Auto-Training Job triggered successfully...")
    print("[Scheduler] Auto-Training Job Started...")
    
    # 1. Check if valid file path exists in system config
    file_path = cm.get_valid_file_path()
    if not file_path:
        logging.warning("Auto-Training cancelled: No valid file path found in configuration.")
        print("[Scheduler] Skip: No valid data file path found.")
        return
        
    # 2. Check last trained meta data to know what was the target column
    meta_path = os.path.join("models", "model_meta.json")
    if not os.path.exists(meta_path):
        logging.warning("Auto-Training cancelled: Missing model meta file. Run initial training from GUI first.")
        print("[Scheduler] Skip: Meta file missing. Run initial training from GUI first.")
        return
        
    try:
        with open(meta_path, "r") as f:
            meta_data = json.load(f)
        target_col = meta_data.get("target_column")
        
        # 3. Load fresh data from the saved disk path safely
        df, error = cm.validate_and_load_data(file_path)
        if error:
            logging.error(f"Data load error during auto-train: {error}")
            return
            
        # 4. Trigger Advanced Stacking Re-training Matrix
        success, message = mle.train_advanced_stacking_model(df, target_col)
        
        if success:
            logging.info(f"Auto-Train Success: {message}")
            print(f"[Scheduler] Success: {message}")
        else:
            logging.error(f"Auto-Train Failed in Engine: {message}")
            print(f"[Scheduler] Engine Error: {message}")
            
    except Exception as e:
        logging.error(f"Critical error in scheduler job loop: {str(e)}")
        print(f"[Scheduler] Critical Error: {str(e)}")

def start_scheduler_daemon():
    """Background loop scheduler initialization"""
    logging.info("Background AI Scheduler Service started successfully.")
    print("[Scheduler] Background Daemon Service Activated...")
    
    # Test/Demo ke liye har 10 minute me check karega ya aap custom interval set kar sakte hain:
    # Production standard: schedule.every().sunday.at("00:00").do(auto_train_job)
    schedule.every(10).minutes.do(auto_train_job)
    
    # Infinitesimal loop tracker running in a daemon state
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Is file ko standalone run karke background window ke roop me bhi rakh sakte hain
    start_scheduler_daemon()