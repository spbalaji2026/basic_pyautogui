import pyautogui
import time

#keyboard operation
#time.sleep(2)  # Wait for 2 seconds
#pyautogui.press("enter")  # Press the Enter key
'''
pyautogui.typewrite("Hello, World!", interval=0.1)  # Type the text "Hello, World!"
'''
#hotkey operation
#pyautogui.hotkey("ctrl", "c")  #Press the Ctrl+C hotkey
#pyautogui.hotkey("ctrl", "v")  # Press the Ctrl+V hotkey
#pyautogui.hotkey("ctrl", "a")  # Press the Ctrl+A hotkey
#pyautogui.hotkey("ctrl", "x")  # Press the Ctrl+X hotkey
#screenshot operations
screenshot = pyautogui.screenshot()  # Take a screenshot of the entire screen
screenshot.save("screenshot.png")  # Save the screenshot as "screenshot.png"
