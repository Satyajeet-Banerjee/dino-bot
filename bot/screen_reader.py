import pyautogui
from config import GAME_REGION

def capture_screen():
    return pyautogui.screenshot(region=GAME_REGION)