# run.py
import sys
import os

# src folder ko system path me map karna imports resolution ke liye
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from app_gui import SmartShopApp

if __name__ == "__main__":
    print("[System Base] Initializing Object-Oriented GUI Thread Loop...")
    app = SmartShopApp()
    app.mainloop()