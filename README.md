# 📁 Youdownneb (Custom YouTube Downloader)

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)
![Batch Script](https://img.shields.io/badge/Batch_Script-4D4D4D?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

**Youdownneb** is a lightweight, intuitive graphical application designed to download YouTube content directly into high-quality MP4 video or MP3 audio files. It features a modern desktop interface and runs background processing threads to keep downloads efficient and stutter-free.

> **🌱 Learning Repository:**
> This repository serves as a **learning playground** for desktop GUI development and API integrations. The code demonstrates practical implementations of thread-safe operations in Tkinter, structured object-oriented programming (OOP), custom UI styling, and robust wrappers around standard CLI tools.
> 
> 

## 📖 Project Description

Downloading media from online platforms often leads to cluttered command lines, complex arguments, or suspicious third-party sites tracking your layout.

**Youdownneb** provides a standalone desktop utility to resolve this issue. Built with an eye-pleasing theme, it allows users to paste a URL, configure individual quality steps, and choose destination directories visually. The application handles network handshakes and formatting seamlessly underneath.

## ✨ Key Features

* ⚡ **Format Flexibility:** Directly processes high-res media options for standard `MP4 (Video)` formats or seamless conversions to crystal clear `MP3 (Audio)` tracks.


* 🪶 **Stutter-Free Architecture:** Leverages multi-threading execution so the user interface stays completely interactive while media streams process in the background.


* 🛠️ **Granular Control:** Provides selective dropdown resolution parameters ranging from standard definitions up to maximum stream properties.


* 🛡️ **Responsive Status Trackers:** Includes dynamic granular progress tracking modules, instant download speed readouts, and remaining time calculation formulas built into real-time feedback meters.



## 💻 Tech Stack

* **Language:** Python 3


* **Environment:** Tkinter Framework (GUI), Custom `ttk` Styles


* **Core Library Dependencies:** `yt_dlp` engine, native `threading` modules



## 🚀 Installation

Setting up the local environment and runtime components takes only a brief moment:

1. **Clone the Repository**
Open your terminal/CMD and run:
`git clone https://github.com/BenTimothyM/Youdownneb.git`
2. **Acquire Python Framework Core Tools**
Ensure Python 3.x is configured correctly on the native platform system variables path.



## 💡 How to Use

> ⚠️ **IMPORTANT: FFmpeg Executable Requirements**
> High-resolution merges (such as combing separate audio and 1080p video blocks) and precise MP3 extraction rely on system access to binary utilities like `ffmpeg` and `ffprobe`.
> 
> 

You can execute the application launch framework in two ways:

**Method 1: GUI (Automated Batch Launcher)**

1. Navigate to the folder where you placed the package files.
2. Double-click the file named `Launcher.bat`.


3. The script will look over the workspace, patch local missing packages, auto-fetch required portable binaries, and trigger execution automatically.


**Method 2: Command Line Manual Startup**

1. Open a system terminal/CMD within the workspace folder.
2. Run installation modules to satisfy external layout needs:
`pip install --upgrade yt-dlp`

3. Initialize the operational script structure manually:
`python main.py`


**Terminal Output Launcher Example:**

```text
===================================================
            YOUDOWNNEB LAUNCHER
         Developed By Ben Timothy
===================================================

[INFO] Inspecting Python environment and requirements...
[INFO] Checking and upgrading yt-dlp...
[INFO] FFmpeg is missing. It is required to merge high-res video and extract MP3.
[INFO] Downloading portable FFmpeg binary (approx. 60MB), please wait...

[INFO] Extracting FFmpeg binaries...
[INFO] Portable FFmpeg successfully configured!

[INFO] All system requirements resolved.
[INFO] Launching Youdownneb App...

```

## 🤝 Contributing (Let's Learn Together!)
As this is a dedicated learning repository, contributions are highly encouraged! If you want to introduce extra streaming adapters, redesign container interfaces, or adapt asset files for broader ecosystem needs, feel free to pitch in:

1. Fork this repository.
2. Create your feature branch (`git checkout -b feature-ui-enhancements`).
3. Commit your changes (`git commit -m 'Add custom visual skin updates'`).
4. Push to your branch (`git push origin feature-ui-enhancements`).
5. Open a Pull Request.

## 👨‍💻 Credits
This project is developed and maintained by:
* **Ben Timothy** - [@BenTimothyM](https://www.google.com/search?q=https://github.com/BenTimothyM)


## 📜 License
This project is distributed under the **MIT License**. See the `LICENSE` file for more details.
