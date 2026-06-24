import os
import PyInstaller.__main__
import customtkinter

# 1. CustomTkinter ke internal assets ka path nikalna (UI freezing fix)
ctk_path = os.path.dirname(customtkinter.__file__)

# 2. PyInstaller programmatically execute karna
PyInstaller.__main__.run([
    'run.py',                           # Main entry point file
    '--name=SmartShopAI_Predictor',      # .exe ka final name
    '--onedir',                          # Clean directory distribution format
    '--windowed',                        # Windows standard black console hide karne ke liye
    '--icon=assets/store.ico',           # Desktop shortcut logo icon
    
    # --- STRICT INCLUSIONS (Sirf zaroori folders add ho rahe hain) ---
    f'--add-data={os.path.join(ctk_path, "assets")}{os.path.pathsep}{os.path.join("customtkinter", "assets")}',
    f'--add-data=src{os.path.pathsep}src',
    f'--add-data=assets{os.path.pathsep}assets',
    
    # --- STRICT EXCLUSIONS (Fuzool files block karne ke liye) ---
    '--exclude-module=auto_xls',
    '--clean',                           # Clear previous cache before building
])

print("\n🚀 BUILD PROCESS COMPLETE!")
print("Aapki clean application 'dist/SmartShopAI_Predictor/' folder me taiyar hai.")