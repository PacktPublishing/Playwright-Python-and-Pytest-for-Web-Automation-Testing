from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # Create a new page
    page = browser.new_page()
    # Visit the playwright website
    page.goto("https://playwright.dev/python")

    # Locate a link element with "Docs" text
    docs_button = page.get_by_role('link', name="Docs")
    docs_button.click()

    # Get the url
    print("Docs:", page.url)

    browser.close()