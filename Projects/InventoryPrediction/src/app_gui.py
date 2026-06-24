import os
import pandas as pd
import customtkinter as ctk
from tkinter import filedialog, messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

# Internal imports
import config_manager as cm
import ml_engine as mle

# Theme and look configuration
ctk.set_appearance_mode("System")  # Automatically matches Windows dark/light mode
ctk.set_default_color_theme("blue")

class SmartShopApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window Settings
        self.title("Smart Shop Analytics & Future Predictor AI")
        self.geometry("1100x650")
        self.minsize(1000, 600)
        
        
        # State Variables
        self.db_path = ""
        self.df = None
        self.current_frame = None
        
        # Bootstrap App Flow
        self.check_initial_state()

    def check_initial_state(self):
        """os.path checks via config_manager to decide screen branching"""
        self.db_path = cm.get_valid_file_path()
        
        if self.db_path:
            # File exists safely, load data and jump to dashboard
            self.df, error = cm.validate_and_load_data(self.db_path)
            if error:
                messagebox.showerror("Initialization Error", error)
                self.show_upload_screen()
            else:
                self.show_dashboard_screen()
        else:
            # First time run or file was deleted by user
            self.show_upload_screen()

    def switch_frame(self, frame_class, *args, **kwargs):
        """Destroys current view and switches to new layout gracefully"""
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self, *args, **kwargs)
        self.current_frame.pack(fill="both", expand=True)

    def show_upload_screen(self):
        self.switch_frame(UploadScreen)

    def show_dashboard_screen(self):
        self.switch_frame(DashboardScreen)


# ==========================================
# SCREEN 1: FILE UPLOAD & PREVIEW INTERFACE
# ==========================================
class UploadScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        # UI Layout setup
        self.grid_columnconfigure(0, weight=1)
        
        # Title Header
        self.title_lbl = ctk.CTkLabel(self, text="📊 Welcome to AI Shop Forecasting Suite", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_lbl.pack(pady=(40, 10))
        
        self.sub_lbl = ctk.CTkLabel(self, text="Please select your shop's sales transaction Excel or CSV ledger to begin.", font=ctk.CTkFont(size=14))
        self.sub_lbl.pack(pady=10)
        
        # Main Upload Box Card
        self.upload_card = ctk.CTkFrame(self, width=500, height=180)
        self.upload_card.pack(pady=20, padx=40, fill="x")
        self.upload_card.pack_propagate(False)
        
        self.browse_btn = ctk.CTkButton(self.upload_card, text="📂 Browse Excel / CSV File", font=ctk.CTkFont(size=14, weight="bold"), command=self.browse_file, width=220, height=45)
        self.browse_btn.place(relx=0.5, rely=0.4, anchor="center")
        
        self.path_lbl = ctk.CTkLabel(self.upload_card, text="No file selected (Mandatory Column: 'Date')", text_color="gray", font=ctk.CTkFont(slant="italic"))
        self.path_lbl.place(relx=0.5, rely=0.75, anchor="center")
        
        # Preview Table Container (Treeview)
        self.preview_lbl = ctk.CTkLabel(self, text="📋 Sheet Preview (Top 5 Rows - pd.head()):", font=ctk.CTkFont(size=14, weight="bold"))
        
        self.table_frame = ctk.CTkFrame(self)
        self.tree = None
        
        # Bottom Navigation
        self.next_btn = ctk.CTkButton(self, text="Proceed to Analytics ➔", state="disabled", fg_color="gray", font=ctk.CTkFont(size=15, weight="bold"), command=self.proceed, width=200, height=45)
        self.next_btn.pack(side="bottom", pady=30)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel or CSV Files", "*.xlsx *.xls *.csv")])
        if not file_path:
            return
            
        # Validate data structure through config manager
        df, error = cm.validate_and_load_data(file_path)
        if error:
            messagebox.showerror("Invalid File Structure", error)
            return
            
        # If success, update state
        self.parent.df = df
        self.parent.db_path = file_path
        self.path_lbl.configure(text=os.path.basename(file_path), text_color="#2ecc71")
        
        # Render Treeview Dynamic Columns and Data (pd.head())
        self.render_preview_table(df.head(5))
        
        # Activate final validation step button
        self.next_btn.configure(state="normal", fg_color="#1f538d")

    def render_preview_table(self, preview_df):
        # Pack frames now that data exists
        self.preview_lbl.pack(pady=(10, 5), anchor="w", padx=40)
        self.table_frame.pack(pady=5, padx=40, fill="both", expand=True)
        
        # Clear existing treeview if any
        if self.tree:
            self.tree.destroy()
            
        # Setup modern looking Tkinter Treeview inside frame
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#2a2d2e", fieldbackground="#2a2d2e", foreground="white", rowheight=25)
        style.map("Treeview", background=[('selected', '#1f538d')])
        
        # Convert columns string format for mapping
        cols = list(preview_df.columns)
        cols_str = [str(c) for c in cols]
        
        self.tree = ttk.Treeview(self.table_frame, columns=cols_str, show="headings")
        
        for col in cols:
            # Convert date display safely
            display_name = col if col != 'Date' else 'Date (Parsed)'
            self.tree.heading(str(col), text=display_name)
            self.tree.column(str(col), anchor="center", width=120)
            
        for _, row in preview_df.iterrows():
            row_vals = []
            for col in cols:
                val = row[col]
                if isinstance(val, pd.Timestamp):
                    row_vals.append(val.strftime('%Y-%m-%d'))
                else:
                    row_vals.append(str(val))
            self.tree.insert("", "end", values=row_vals)
            
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

    def proceed(self):
        # Save validated path permanently to file
        cm.save_file_path(self.parent.db_path)
        self.parent.show_dashboard_screen()


# ==========================================
# SCREEN 2: MAIN DASHBOARD & FORECASTING FRAME
# ==========================================
class DashboardScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.df = parent.df
        
        # Main Dashboard Layout Grid splits into Sidebar and Workspace
        self.grid_columnconfigure(0, weight=1) # Sidebar weight
        self.grid_columnconfigure(1, weight=5) # Workspace weight
        self.grid_rowconfigure(0, weight=1)
        
        # --- LEFT SIDEBAR PANEL ---
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        
        self.logo_lbl = ctk.CTkLabel(self.sidebar, text="🏪 ShopAI Engine", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_lbl.pack(pady=30, padx=20)
        
        # Menu Tabs Navigation Buttons
        self.tab1_btn = ctk.CTkButton(self.sidebar, text="📈 Historical Analytics", fg_color="#1f538d", height=40, command=lambda: self.select_tab("analytics"))
        self.tab1_btn.pack(pady=10, padx=20, fill="x")
        
        self.tab2_btn = ctk.CTkButton(self.sidebar, text="🔮 AI Forecasting", fg_color="transparent", height=40, command=lambda: self.select_tab("forecasting"))
        self.tab2_btn.pack(pady=10, padx=20, fill="x")
        
        self.reset_btn = ctk.CTkButton(self.sidebar, text="🔄 Change Source File", fg_color="#c0392b", hover_color="#962d22", height=35, command=self.reset_source_file)
        self.reset_btn.pack(side="bottom", pady=30, padx=20, fill="x")
        
        # --- RIGHT WORKSPACE MAIN AREA ---
        self.workspace = ctk.CTkFrame(self, fg_color="transparent")
        self.workspace.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        # Initialize Tab Screens
        self.active_tab = None
        self.select_tab("analytics")

    def select_tab(self, tab_name):
        """Switches active sub-tab view styling and frames inside workspace"""
        if self.active_tab == tab_name: return
        
        # Button styling toggle
        if tab_name == "analytics":
            self.tab1_btn.configure(fg_color="#1f538d")
            self.tab2_btn.configure(fg_color="transparent")
            self.render_analytics_tab()
        else:
            self.tab1_btn.configure(fg_color="transparent")
            self.tab2_btn.configure(fg_color="#1f538d")
            self.render_forecasting_tab()
            
        self.active_tab = tab_name

    def clear_workspace(self):
        for widget in self.workspace.winfo_children():
            widget.destroy()

    # --- SUB TAB 1: SEABORN HISTORICAL PLOTS ---
    # --- SUB TAB 1: SEABORN HISTORICAL PLOTS WITH DATE FILTER ---
    def render_analytics_tab(self):
        self.clear_workspace()
        
        # Header controls inside workspace (Thoda bada kiya panel taaki filters aa sakein)
        ctrl_panel = ctk.CTkFrame(self.workspace, height=80)
        ctrl_panel.pack(fill="x", pady=(0, 15))
        
        # 1. Metric Dropdown Selector
        ctk.CTkLabel(ctrl_panel, text="Metric: ", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=(15, 2), pady=15)
        numeric_cols = list(self.df.select_dtypes(include=['number']).columns)
        self.plot_var = ctk.StringVar(value=numeric_cols[0] if numeric_cols else "")
        self.menu_dropdown = ctk.CTkOptionMenu(ctrl_panel, width=140, values=numeric_cols, variable=self.plot_var, command=lambda _: self.update_seaborn_graph())
        self.menu_dropdown.pack(side="left", padx=5, pady=15)
        
        # Global dates nikalna string format me drop-downs ke liye
        all_dates = self.df['Date'].dt.strftime('%Y-%m-%d').tolist()
        
        # 2. FROM DATE FILTER (Default: Aaj se 30 records pehle ya start date)
        ctk.CTkLabel(ctrl_panel, text=" From: ", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=(20, 2), pady=15)
        default_from = all_dates[-30] if len(all_dates) >= 30 else all_dates[0]
        self.from_date_var = ctk.StringVar(value=default_from)
        self.from_dropdown = ctk.CTkOptionMenu(ctrl_panel, width=120, values=all_dates, variable=self.from_date_var, command=lambda _: self.update_seaborn_graph())
        self.from_dropdown.pack(side="left", padx=5, pady=15)
        
        # 3. TO DATE FILTER (Default: Last Date of the dataset)
        ctk.CTkLabel(ctrl_panel, text=" To: ", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=(10, 2), pady=15)
        default_to = all_dates[-1]
        self.to_date_var = ctk.StringVar(value=default_to)
        self.to_dropdown = ctk.CTkOptionMenu(ctrl_panel, width=120, values=all_dates, variable=self.to_date_var, command=lambda _: self.update_seaborn_graph())
        self.to_dropdown.pack(side="left", padx=5, pady=15)
        
        # Graph Canvas Container
        self.graph_frame = ctk.CTkFrame(self.workspace)
        self.graph_frame.pack(fill="both", expand=True)
        
        # Initial Plot Execution
        self.update_seaborn_graph()

    def update_seaborn_graph(self):
        selected_metric = self.plot_var.get()
        if not selected_metric: return
        
        # Fetch current date bounds from UI
        start_date = pd.to_datetime(self.from_date_var.get())
        end_date = pd.to_datetime(self.to_date_var.get())
        
        # Validation: Agar user ne ulti date select kar li (From > To)
        if start_date > end_date:
            messagebox.showwarning("Filter Boundary Conflict", "'From Date' humesha 'To Date' se pehle ki honi chahiye!")
            return
            
        # SMART WINDOWING: DataFrame ko user ke select kiye range ke hisab se filter karna
        filtered_df = self.df[(self.df['Date'] >= start_date) & (self.df['Date'] <= end_date)]
        
        if filtered_df.empty:
            return
            
        # Clear previous canvas elements safely
        for widget in self.graph_frame.winfo_children(): 
            widget.destroy()
        
        plt.clf() 
        
        sns.set_theme(style="darkgrid")
        fig, ax = plt.subplots(figsize=(7, 3.8), dpi=100)
        fig.patch.set_facecolor('#2b2b2b') 
        ax.set_facecolor('#242424')
        
        # Sliced Dataset Line Plot
        sns.lineplot(
            data=filtered_df, # 👈 Pure dataset ke bajay sirf filtered data jayega
            x='Date', 
            y=selected_metric, 
            ax=ax, 
            color="#3498db", 
            linewidth=2.5, 
            marker='o'
        )
        
        ax.set_title(f"Historical Trend Analysis: {selected_metric} (Custom Range)", color="white", fontsize=12, pad=10)
        ax.tick_params(colors='white', labelsize=8)
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        
        plt.xticks(rotation=20)
        plt.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)
        
    # --- SUB TAB 2: AI RECURSIVE FORECASTER PANEL ---
    def render_forecasting_tab(self):
        self.clear_workspace()
        
        # Configurations Row Splitter (Left settings card, Right dynamic prediction graph card)
        self.workspace.grid_columnconfigure(0, weight=2)
        self.workspace.grid_columnconfigure(1, weight=3)
        self.workspace.grid_rowconfigure(0, weight=1)
        
        left_panel = ctk.CTkFrame(self.workspace)
        left_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        right_panel = ctk.CTkFrame(self.workspace)
        right_panel.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        
        # --- LEFT PANEL SETTINGS CONTROLS ---
        ctk.CTkLabel(left_panel, text="🤖 AI Model Control Panel", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=15, padx=15, anchor="w")
        
        # Target Selection Dropdown Setup
        ctk.CTkLabel(left_panel, text="1. Select Column to Predict (Target):", font=ctk.CTkFont(weight="bold")).pack(pady=(5,2), padx=15, anchor="w")
        numeric_cols = list(self.df.select_dtypes(include=['number']).columns)
        self.target_var = ctk.StringVar(value=numeric_cols[0] if numeric_cols else "")
        self.target_dropdown = ctk.CTkOptionMenu(left_panel, values=numeric_cols, variable=self.target_var, command=self.handle_target_change)
        self.target_dropdown.pack(pady=5, padx=15, fill="x")
        
        # AI Suggestion Prompt box live binding
        self.ai_suggest_lbl = ctk.CTkLabel(left_panel, text="", text_color="#2ecc71", font=ctk.CTkFont(size=11, weight="bold"), wraplength=320, justify="left")
        self.ai_suggest_lbl.pack(pady=5, padx=15, anchor="w")
        
        # Train Button trigger
        self.train_btn = ctk.CTkButton(left_panel, text="⚙️ Train Advanced Stacking Model", fg_color="#27ae60", hover_color="#219150", font=ctk.CTkFont(weight="bold"), command=self.trigger_model_training)
        self.train_btn.pack(pady=15, padx=15, fill="x")
        
        # Timeline Horizon Dropdown Setup
        ctk.CTkLabel(left_panel, text="2. Forecasting Horizon Period:", font=ctk.CTkFont(weight="bold")).pack(pady=(15,2), padx=15, anchor="w")
        self.horizon_var = ctk.StringVar(value="Next Day (1 Day)")
        self.horizon_dropdown = ctk.CTkOptionMenu(left_panel, values=["Next Day (1 Day)", "Next Week (7 Days)", "Next Month (30 Days)"], variable=self.horizon_var)
        self.horizon_dropdown.pack(pady=5, padx=15, fill="x")
        
        # Predict Button Trigger
        self.predict_btn = ctk.CTkButton(left_panel, text="🔮 Execute Future Forecast", font=ctk.CTkFont(size=13, weight="bold"), command=self.trigger_future_forecasting)
        self.predict_btn.pack(pady=20, padx=15, fill="x")
        
        # Trigger default initial suggestion string loop on boot
        self.handle_target_change(self.target_var.get())
        
        # --- RIGHT PANEL FORECAST VISUALIZATION WINDOW ---
        self.forecast_window = right_panel
        self.no_data_msg = ctk.CTkLabel(self.forecast_window, text="📊 Forecast trends table & charts will render here\nafter executing the AI model engine pipeline.", text_color="gray", font=ctk.CTkFont(slant="italic"))
        self.no_data_msg.place(relx=0.5, rely=0.5, anchor="center")

    def handle_target_change(self, val):
        """Trigger dynamic Pearson correlation checks instantly when target dropdown updates"""
        _, suggestion_text = cm.get_ai_suggestions(self.df, val)
        self.ai_suggest_lbl.configure(text=suggestion_text)

    def trigger_model_training(self):
        target = self.target_var.get()
        self.train_btn.configure(text="⚡ Training Stacking Pipeline...", state="disabled")
        self.update() # Refresh GUI UI thread loop
        
        success, message = mle.train_advanced_stacking_model(self.df, target)
        
        if success:
            messagebox.showinfo("AI System Core", message)
        else:
            messagebox.showerror("AI Pipeline Failure", message)
            
        self.train_btn.configure(text="⚙️ Train Advanced Stacking Model", state="normal")

    def trigger_future_forecasting(self):
        horizon_string = self.horizon_var.get()
        days_mapping = {"Next Day (1 Day)": 1, "Next Week (7 Days)": 7, "Next Month (30 Days)": 30}
        days = days_mapping.get(horizon_string, 1)
        
        result_df, error = mle.predict_next_days(self.df, days_to_predict=days)
        
        if error:
            messagebox.showerror("Forecaster Matrix Error", error)
            return
            
        for widget in self.forecast_window.winfo_children(): 
            widget.destroy()
        
        # Matplotlib global figure state clear karna (Center squeeze fix)
        plt.clf()
        
        chart_sub = ctk.CTkFrame(self.forecast_window, fg_color="transparent")
        chart_sub.pack(fill="both", expand=True, pady=(10,5))
        
        table_sub = ctk.CTkFrame(self.forecast_window, height=140)
        table_sub.pack(fill="x", padx=15, pady=(5,15))
        
        # Fresh Plot configuration
        fig, ax = plt.subplots(figsize=(5, 3), dpi=100)
        fig.patch.set_facecolor('#2b2b2b')
        ax.set_facecolor('#242424')
        ax.grid(True, color="#444444", linestyle="--", alpha=0.5) # Background Grid lines
        
        pred_col = result_df.columns[1]
        
        # Stretched Line Plot
        ax.plot(
            result_df['Date'], 
            result_df[pred_col], 
            color="#2ecc71", 
            linestyle="-",      # Continuous line style
            marker="o", 
            linewidth=2, 
            label="AI Forecast"
        )
        
        ax.set_title(f"AI Prediction Horizon Result ({len(result_df)} Days)", color="white", fontsize=11)
        ax.tick_params(colors='white', labelsize=8)
        
        # X-Axis limits formatting taaki labels center me na phasein
        plt.xticks(rotation=20)
        ax.legend(facecolor='#2b2b2b', edgecolor='none', labelcolor='white')
        plt.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, master=chart_sub)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)
        
        # --- Niche ka table view as it is rahega ---
        tree = ttk.Treeview(table_sub, columns=["Date", "Val"], show="headings", height=4)
        tree.heading("Date", text="Future Forecast Date")
        tree.heading("Val", text="Predicted Smart Value")
        tree.column("Date", anchor="center", width=140)
        tree.column("Val", anchor="center", width=140)
        
        for _, row in result_df.iterrows():
            tree.insert("", "end", values=(row['Date'].strftime('%Y-%m-%d'), f"{row[pred_col]:.2f}"))
            
        tree.pack(fill="both", expand=True, padx=5, pady=5)
        
    def reset_source_file(self):
        """Resets dynamic path, flushes configuration parameters and restarts GUI cycle"""
        if messagebox.askyesno("Change File Source", "Kya aap sach me dataset source path change karna chahte hain?"):
            cm.save_file_path("") # Flush global system JSON configuration
            self.parent.df = None
            self.parent.db_path = ""
            self.parent.show_upload_screen()