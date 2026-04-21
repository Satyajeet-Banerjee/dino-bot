🦖 Chrome Dino Bot

A Python automation bot that plays the Chrome Dino game by detecting obstacles on the screen and triggering jumps automatically.

🚀 Features
Automatic obstacle detection using screen capture
Smart jump control with cooldown system
Stable detection to avoid false jumps
Clean shutdown handling (Ctrl + C support)
Lightweight and fast execution

🛠️ Tech Stack
Python
PyAutoGUI
Pillow (PIL)
PyGetWindow

How It Works
1.Captures the game screen using a fixed region
2.Scans pixels in the obstacle zone
3.Detects cactus based on pixel brightness
4.Sends a jump command when obstacle is detected
5.Uses cooldown + stability check to avoid spam jumps

How to Run
1. Install dependencies
pip install -r requirements.txt
2. Open Chrome Dino game
Go to Chrome Dino game
Press F11 (recommended for full screen)
Start the game once manually
3. Run the bot
python main.py
