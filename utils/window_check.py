import pygetwindow as gw

def is_game_active():
    try:
        active = gw.getActiveWindow()
        return active and "Chrome" in active.title
    except:
        return False