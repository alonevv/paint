import pyautogui
import keyboard
import subprocess
import time
subprocess.Popen('w.exe')
time.sleep(3)

keyboard.press("1")
time.sleep(0.1)
keyboard.release("1")
keyboard.press("r")
time.sleep(0.1)
keyboard.release("r")
screenWidth, screenHeight = pyautogui.size()  # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(300, 200)

pyautogui.drag(1003, 0, duration=1)   # move right

pyautogui.drag(0, 30, duration=1)   # move down
keyboard.press("5")
time.sleep(0.1)
keyboard.release("5")
pyautogui.drag(-100, 0, duration=1)  # move left

pyautogui.drag(0, 30, duration=1)   # move down
keyboard.press("3")
time.sleep(0.1)
keyboard.release("3")
pyautogui.drag(100, 0, duration=1)   # move right




