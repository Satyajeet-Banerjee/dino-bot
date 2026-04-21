import keyboard

running = True

def toggle_bot():
    global running
    running = not running
    print("Bot Running:", running)

keyboard.add_hotkey("F8", toggle_bot)