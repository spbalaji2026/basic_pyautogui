import time
from datetime import datetime
from pathlib import Path

import pyautogui
import pyperclip
from openpyxl import Workbook


# ---------------------------------------------------------
# SETTINGS
# ---------------------------------------------------------

# Website to open
WEATHER_URL = "https://www.google.com/search?q=weather+Tamil+Nadu"

# Folder where the Excel file and screenshot will be saved
OUTPUT_FOLDER = Path.cwd()

# Short comment to put in the report
COMMENT = "Balaji - Hurray! Success, you did the first automation in Python."

# Give PyAutoGUI a small pause between actions
pyautogui.PAUSE = 0.5


# ---------------------------------------------------------
# HELPER FUNCTION
# ---------------------------------------------------------

def wait(seconds=2):
    """Wait for a specified number of seconds."""
    time.sleep(seconds)


# ---------------------------------------------------------
# STEP 1: OPEN CHROME
# ---------------------------------------------------------

def open_chrome():
    print("Opening Chrome...")

    # Windows shortcut to open the Run dialog
    pyautogui.hotkey("win", "r")
    wait(1)

    # Type chrome and press Enter
    pyautogui.write("chrome", interval=0.05)
    pyautogui.press("enter")

    # Give Chrome time to open
    wait(4)


# ---------------------------------------------------------
# STEP 2: OPEN WEATHER WEBSITE
# ---------------------------------------------------------

def open_weather_page():
    print("Opening Tamil Nadu weather page...")

    # Ctrl + L selects the browser address bar
    pyautogui.hotkey("ctrl", "l")

    # Type website address
    pyautogui.write(WEATHER_URL, interval=0.01)

    # Open the website
    pyautogui.press("enter")

    # Wait for the page to load
    wait(5)


# ---------------------------------------------------------
# STEP 3: COPY TEMPERATURE
# ---------------------------------------------------------

def get_temperature():
    print("Trying to copy temperature...")

    # Google weather pages can change layout.
    # We use Ctrl+A and Ctrl+C to copy the visible page text.
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")

    wait(1)

    # Read the copied text from the clipboard
    page_text = pyperclip.paste()

    # Display some information for debugging
    print("Weather page text copied.")

    # Try to find a temperature such as 32°C or 32 °C
    lines = page_text.splitlines()

    for line in lines:
        line = line.strip()

        if "°C" in line:
            print("Temperature found:", line)
            return line

    # If temperature was not found
    return "Temperature not found"


# ---------------------------------------------------------
# STEP 4: CREATE EXCEL FILE
# ---------------------------------------------------------

def create_excel_report(temperature):
    print("Creating Excel report...")

    # Get current date and time
    now = datetime.now()

    # Date for filename
    current_date = now.strftime("%Y-%m-%d")

    # Date and time for the Excel row
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Create a new Excel workbook
    workbook = Workbook()

    # Select the active worksheet
    worksheet = workbook.active

    # Give the worksheet a name
    worksheet.title = "Daily Report"

    # Create headings
    worksheet["A1"] = "Date & Time"
    worksheet["B1"] = "Temperature"
    worksheet["C1"] = "Comment"

    # Create the first data row
    worksheet["A2"] = date_time
    worksheet["B2"] = temperature
    worksheet["C2"] = COMMENT

    # Make columns wider
    worksheet.column_dimensions["A"].width = 22
    worksheet.column_dimensions["B"].width = 20
    worksheet.column_dimensions["C"].width = 65

    # Create filename
    filename = f"daily_report_{current_date}.xlsx"

    # Full file path
    excel_path = OUTPUT_FOLDER / filename

    # Save Excel file
    workbook.save(excel_path)

    print(f"Excel file saved: {excel_path}")

    return excel_path


# ---------------------------------------------------------
# STEP 5: OPEN EXCEL
# ---------------------------------------------------------

def open_excel(excel_path):
    print("Opening Excel...")

    # Open the saved Excel file using Windows
    pyautogui.hotkey("win", "r")
    wait(1)

    pyautogui.write(str(excel_path), interval=0.01)
    pyautogui.press("enter")

    # Excel may take some time to start
    wait(7)


# ---------------------------------------------------------
# STEP 6: TAKE SCREENSHOT
# ---------------------------------------------------------

def take_screenshot(current_date):
    print("Taking screenshot...")

    screenshot_name = f"daily_report_{current_date}.png"

    screenshot_path = OUTPUT_FOLDER / screenshot_name

    # Take screenshot of the whole screen
    screenshot = pyautogui.screenshot()

    # Save screenshot
    screenshot.save(screenshot_path)

    print(f"Screenshot saved: {screenshot_path}")

    return screenshot_path


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

def main():

    print("----------------------------------------")
    print("Daily Report Automation Started")
    print("----------------------------------------")

    # Step 1
    open_chrome()

    # Step 2
    open_weather_page()

    # Step 3
    temperature = get_temperature()

    print("Fetched temperature:", temperature)

    # Get today's date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Step 4
    excel_path = create_excel_report(temperature)

    # Step 5
    open_excel(excel_path)

    # Give Excel time to display the sheet
    wait(3)

    # Step 6
    screenshot_path = take_screenshot(current_date)

    print("----------------------------------------")
    print("Automation completed successfully!")
    print("----------------------------------------")
    print("Excel file:", excel_path)
    print("Screenshot:", screenshot_path)


# ---------------------------------------------------------
# START PROGRAM
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
