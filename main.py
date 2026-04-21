import time
import pyautogui
from bot.screen_reader import capture_screen
from bot.detector import detect_obstacle
from config import COOLDOWN, SCAN_DELAY

last_jump = 0
stable_counter = 0

print("Switch to game in 3 seconds...")
time.sleep(3)

print("Bot started 🚀")

try:
    while True:
        screen = capture_screen()

        if detect_obstacle(screen):
            stable_counter += 1
        else:
            stable_counter = 0

        now = time.time()

        if stable_counter >= 2:
            if now - last_jump > COOLDOWN:
                pyautogui.press("space")
                print("Jump!")
                last_jump = now
                stable_counter = 0

        time.sleep(SCAN_DELAY)

except KeyboardInterrupt:
    print("\n🛑 Bot stopped manually (Ctrl + C)")
    print("✔ Exiting cleanly... Goodbye!")

except Exception as e:
    print("\n💥 Unexpected error occurred:", str(e))
    print("✔ Bot shutting down safely...")

finally:
    print("🏁 Dino Bot session ended.")