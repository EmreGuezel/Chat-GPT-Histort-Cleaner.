import pyautogui
import time
import keyboard
working = True
def stopprogram(e):
    global working
    working = False     
keyboard.on_press_key("s", stopprogram)
while working:
    pyautogui.moveTo(489, 501)
    time.sleep(1)
    pyautogui.click(489, 501)
    time.sleep(1)
    pyautogui.click(489, 501)
    time.sleep(1)
    pyautogui.moveTo(612, 775)
    time.sleep(1)
    pyautogui.click(612, 775)
    time.sleep(1)
    pyautogui.keyDown("enter")
    time.sleep(0.5)
    pyautogui.keyUp("enter")