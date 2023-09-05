from playwright.sync_api import sync_playwright
from time import perf_counter


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=500
    )
    page = browser.new_page()
    print("Page loading...")
    start = perf_counter()

    page.goto(
        "https://playwright.dev/python/",
        # Response received
        # wait_until='commit',

        # HTML parsed and <script> executed
        # wait_until='domcontentloaded',

        # Default, HTML loaded along with resources
        wait_until='load',

        # Network operations stopped
        # wait_until='networkidle',
    )

    time_taken = perf_counter() - start
    print(f"...Page loaded in {round(time_taken, 2)}s")
    
    browser.close()