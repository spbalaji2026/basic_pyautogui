# cricbuzz_score.py

from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    # 1. Launch Chromium in headed mode
    browser = p.chromium.launch(headless=False)

    # 2. Create a new browser page
    page = browser.new_page()

    # 3. Open Cricbuzz
    page.goto("https://www.cricbuzz.com")

    # 4. Wait for the score element
    # Replace this selector with the selector you found
    # by inspecting the Cricbuzz page.
    score = page.locator("YOUR_SCORE_SELECTOR").first

    score.wait_for(state="visible")

    # 5. Get and print the score
    score_text = score.inner_text()

    print("Latest score:")
    print(score_text)

    # 6. Save screenshot
    page.screenshot(path="score.png", full_page=True)

    # 7. Close browser
    browser.close()
