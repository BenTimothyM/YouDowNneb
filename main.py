# ===================================================
# Credit By Ben Timothy
# Project Name: Youdownneb
# Developed By: Ben Timothy
# Description: Custom YouTube Downloader (MP4/MP3)
# ===================================================

import os
import sys
import threading
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import yt_dlp

class YoudownnebApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouDowNneb")
        
        # Dimensions adjusted to fit all layout widgets comfortably
        self.window_width = 620
        self.window_height = 530
        self.center_window(self.window_width, self.window_height)
        self.root.resizable(False, False)
        
        # Color Palette - Modern Dark Slate (Catppuccin Mocha Theme)
        self.bg_color = "#1E1E2E"        # Deep blue-gray slate background
        self.card_color = "#252538"      # Panels/cards container color
        self.accent_color = "#89B4FA"    # Soft pastel blue highlight
        self.accent_hover = "#A6E3A1"    # Soft pastel green on hover
        self.fg_color = "#CDD6F4"        # Standard bright text
        self.muted_color = "#A6ADC8"     # Muted grey text
        
        self.root.configure(bg=self.bg_color)
        
        # State Tracking
        self.is_downloading = False
        
        # Dynamic Options variables
        self.url_var = tk.StringVar()
        self.format_var = tk.StringVar(value="MP4 (Video)")
        self.quality_var = tk.StringVar()
        self.dir_var = tk.StringVar(value=os.path.join(os.path.expanduser('~'), 'Downloads'))
        
        # Initialize UI Components
        self.setup_styles()
        self.build_gui()
        
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Style standard Comboboxes
        style.configure("TCombobox", 
                        fieldbackground=self.card_color, 
                        background=self.accent_color, 
                        foreground=self.fg_color,
                        bordercolor=self.bg_color,
                        lightcolor=self.bg_color,
                        darkcolor=self.bg_color)
        
        # Custom Styled Progress Bar
        style.configure("Custom.Horizontal.TProgressbar", 
                        thickness=14, 
                        troughcolor=self.card_color, 
                        background=self.accent_color,
                        bordercolor=self.bg_color,
                        lightcolor=self.bg_color,
                        darkcolor=self.bg_color)

    def build_gui(self):
        # 1. Header Frame
        header_frame = tk.Frame(self.root, bg=self.bg_color)
        header_frame.pack(fill="x", pady=(25, 10), padx=30)
        
        title_label = tk.Label(header_frame, text="YouDowNneb", font=("Segoe UI", 28, "bold"), fg=self.accent_color, bg=self.bg_color)
        title_label.pack(anchor="w")
        
        credit_label = tk.Label(header_frame, text="Developed By Ben Timothy", font=("Segoe UI", 9, "italic"), fg=self.muted_color, bg=self.bg_color)
        credit_label.pack(anchor="w", pady=(2, 0))
        
        # Line separating header and content
        divider = tk.Frame(self.root, height=1, bg="#2D2D3E")
        divider.pack(fill="x", padx=30, pady=(0, 20))
        
        # 2. Main Input Card Container (Adjusted without expand=True to preserve button spacing)
        form_frame = tk.Frame(self.root, bg=self.card_color, bd=0)
        form_frame.pack(fill="x", padx=30, pady=(0, 15))
        
        inner_frame = tk.Frame(form_frame, bg=self.card_color)
        inner_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # A. URL Input
        url_label = tk.Label(inner_frame, text="YouTube URL:", font=("Segoe UI", 10, "bold"), fg=self.fg_color, bg=self.card_color)
        url_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 5))
        
        url_border = tk.Frame(inner_frame, bg="#3E3E56", bd=1)
        url_border.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        
        self.url_entry = tk.Entry(url_border, textvariable=self.url_var, font=("Segoe UI", 11), bg=self.bg_color, fg=self.fg_color, insertbackground=self.fg_color, bd=0, relief="flat")
        self.url_entry.pack(fill="x", ipady=6, padx=8)
        
        # B. Form Formats Options (Two Columns)
        options_frame = tk.Frame(inner_frame, bg=self.card_color)
        options_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        
        # Format Select
        fmt_label = tk.Label(options_frame, text="Format:", font=("Segoe UI", 10, "bold"), fg=self.fg_color, bg=self.card_color)
        fmt_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        self.fmt_combobox = ttk.Combobox(options_frame, textvariable=self.format_var, state="readonly", values=["MP4 (Video)", "MP3 (Audio)"], width=18, font=("Segoe UI", 10))
        self.fmt_combobox.grid(row=1, column=0, sticky="w", padx=(0, 15))
        self.fmt_combobox.bind("<<ComboboxSelected>>", self.on_format_change)
        
        # Quality Select
        qual_label = tk.Label(options_frame, text="Quality / Resolution:", font=("Segoe UI", 10, "bold"), fg=self.fg_color, bg=self.card_color)
        qual_label.grid(row=0, column=1, sticky="w", pady=(0, 5))
        
        self.quality_combobox = ttk.Combobox(options_frame, textvariable=self.quality_var, state="readonly", width=18, font=("Segoe UI", 10))
        self.quality_combobox.grid(row=1, column=1, sticky="w")
        
        # Run Format configuration to populate current quality selection lists
        self.on_format_change()
        
        # C. Output Location Selection
        dest_label = tk.Label(inner_frame, text="Save Destination Folder:", font=("Segoe UI", 10, "bold"), fg=self.fg_color, bg=self.card_color)
        dest_label.grid(row=3, column=0, columnspan=2, sticky="w", pady=(0, 5))
        
        dest_action_frame = tk.Frame(inner_frame, bg=self.card_color)
        dest_action_frame.grid(row=4, column=0, columnspan=2, sticky="ew")
        
        dest_border = tk.Frame(dest_action_frame, bg="#3E3E56", bd=1)
        dest_border.pack(side="left", fill="x", expand=True)
        
        self.dest_entry = tk.Entry(dest_border, textvariable=self.dir_var, font=("Segoe UI", 9), bg=self.bg_color, fg=self.muted_color, bd=0, relief="flat", state="readonly")
        self.dest_entry.pack(fill="x", ipady=5, padx=8)
        
        self.browse_btn = tk.Button(dest_action_frame, text="Browse", font=("Segoe UI", 9, "bold"), bg="#3E3E56", fg=self.fg_color, activebackground="#4E4E6E", activeforeground=self.fg_color, bd=0, relief="flat", command=self.browse_directory, cursor="hand2")
        self.browse_btn.pack(side="right", padx=(10, 0), ipady=4, ipadx=15)
        
        # Grid Configuration Weights
        inner_frame.columnconfigure(0, weight=1)
        inner_frame.columnconfigure(1, weight=1)
        options_frame.columnconfigure(0, weight=1)
        options_frame.columnconfigure(1, weight=1)
        
        # 3. Status Labels
        self.progress_frame = tk.Frame(self.root, bg=self.bg_color)
        self.progress_frame.pack(fill="x", padx=30, pady=(10, 5))
        
        self.status_label = tk.Label(self.progress_frame, text="Status: Ready", font=("Segoe UI", 9, "bold"), fg=self.muted_color, bg=self.bg_color)
        self.status_label.pack(side="left")
        
        self.percentage_label = tk.Label(self.progress_frame, text="0.0%", font=("Segoe UI", 9, "bold"), fg=self.accent_color, bg=self.bg_color)
        self.percentage_label.pack(side="right")
        
        # 4. Progress bar
        self.progress_bar = ttk.Progressbar(self.root, style="Custom.Horizontal.TProgressbar", orient="horizontal", mode="determinate")
        self.progress_bar.pack(fill="x", padx=30, pady=(0, 15))
        
        # 5. Download Button (Configured with balanced padding heights)
        self.download_btn = tk.Button(self.root, text="DOWNLOAD", font=("Segoe UI", 12, "bold"), bg=self.accent_color, fg=self.bg_color, activebackground=self.accent_hover, activeforeground=self.bg_color, bd=0, relief="flat", command=self.start_download_thread, cursor="hand2")
        self.download_btn.pack(fill="x", padx=30, pady=(10, 25), ipady=12)
        
        # Register simple hover events manually
        self.download_btn.bind("<Enter>", lambda e: self.on_hover(self.download_btn, self.accent_hover))
        self.download_btn.bind("<Leave>", lambda e: self.on_hover(self.download_btn, self.accent_color))
        
    def on_hover(self, button, color):
        if not self.is_downloading:
            button.config(bg=color)
            
    def on_format_change(self, event=None):
        if "MP4" in self.format_var.get():
            self.quality_combobox['values'] = ["360p", "480p", "720p", "1080p", "Best Available"]
            self.quality_combobox.set("Best Available")
        else:
            self.quality_combobox['values'] = ["128 kbps", "192 kbps", "320 kbps"]
            self.quality_combobox.set("192 kbps")

    def browse_directory(self):
        if self.is_downloading:
            return
        selected_dir = filedialog.askdirectory(initialdir=self.dir_var.get())
        if selected_dir:
            self.dir_var.set(selected_dir)
            
    def update_progress(self, percentage, status_text):
        self.progress_bar['value'] = percentage
        self.percentage_label.config(text=f"{percentage:.1f}%")
        self.status_label.config(text=status_text)
        
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes') or d.get('total_bytes_estimate') or 0
            
            if total > 0:
                percentage = (downloaded / total) * 100
                speed = d.get('_speed_str', 'N/A')
                eta = d.get('_eta_str', 'N/A')
                status_text = f"Status: Downloading... ({speed} | ETA: {eta})"
                self.root.after(0, self.update_progress, percentage, status_text)
            else:
                self.root.after(0, self.update_progress, 0, "Status: Extracting streams...")
        elif d['status'] == 'finished':
            self.root.after(0, self.update_progress, 100, "Status: Finalizing / Post-processing...")

    def start_download_thread(self):
        if self.is_downloading:
            return
            
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning("Validation Error", "Please provide a valid YouTube URL first.")
            return
            
        # UI Lock State configuration
        self.is_downloading = True
        self.download_btn.config(state="disabled", text="DOWNLOADING...", bg="#4E4E6E")
        self.browse_btn.config(state="disabled")
        self.fmt_combobox.config(state="disabled")
        self.quality_combobox.config(state="disabled")
        self.url_entry.config(state="disabled")
        
        self.update_progress(0, "Status: Connecting to YouTube...")
        
        # Background Processing thread
        t = threading.Thread(target=self.run_download, args=(url,), daemon=True)
        t.start()
        
    def run_download(self, url):
        fmt = self.format_var.get()
        quality = self.quality_var.get()
        save_dir = self.dir_var.get()
        
        ydl_opts = {
            'progress_hooks': [self.progress_hook],
            'outtmpl': os.path.join(save_dir, '%(title)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
        }
        
        # Configure download arguments
        if "MP4" in fmt:
            if quality == "Best Available":
                ydl_opts['format'] = 'bestvideo+bestaudio/best'
            else:
                res = quality.replace("p", "")
                ydl_opts['format'] = f'bestvideo[height<={res}]+bestaudio/best[height<={res}]'
            ydl_opts['merge_output_format'] = 'mp4'
        else:
            bitrate = quality.replace(" kbps", "")
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': bitrate,
            }]
            
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.root.after(0, self.download_complete, "Success")
        except Exception as e:
            self.root.after(0, self.download_complete, str(e))

    def download_complete(self, result):
        # UI Unlock State restoration
        self.is_downloading = False
        self.download_btn.config(state="normal", text="DOWNLOAD", bg=self.accent_color)
        self.browse_btn.config(state="normal")
        self.fmt_combobox.config(state="readonly")
        self.quality_combobox.config(state="readonly")
        self.url_entry.config(state="normal")
        
        if result == "Success":
            self.update_progress(100.0, "Status: Completed successfully.")
            messagebox.showinfo("Success", "Download completed successfully!")
        else:
            self.update_progress(0.0, "Status: Download failed.")
            if "ffmpeg" in result.lower() or "ffprobe" in result.lower():
                messagebox.showerror(
                    "FFmpeg Dependency Error", 
                    "FFmpeg is required to finalize files or convert to MP3 format.\n\n"
                    "1. Please ensure FFmpeg is installed.\n"
                    "2. Verify FFmpeg is added to your environment variables PATH.\n"
                    "Alternatively, select video formatting profiles to avoid post-processing tasks."
                )
            else:
                messagebox.showerror("Error", f"An error occurred during process execution:\n\n{result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YoudownnebApp(root)
    root.mainloop()