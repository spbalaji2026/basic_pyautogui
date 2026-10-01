import pyautogui
import time
#mouse operation
#pyautogui.moveTo(100, 100, duration=2)  # Move the mouse to (100, 100) over 1 second
#pyautogui.rightClick()  # Right-click at the current mouse positiongui
#pyautogui.dragTo(200, 200, duration=2)  # Drag the mouse to (200, 200) over 1 second
#scrolling up and down
time.sleep(2)  # Wait for 2 seconds
pyautogui.scroll(900)  # Scroll down 500 units
time.sleep(2)  # Wait for 2 seconds
pyautogui.scroll(-900)  # Scroll up 500 units

