import pytest
from playwright.sync_api import Browser, Page

DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_has_get_started_link(browser: Browser):
    context = browser.new_context(
        record_video_dir="video/"
    )
    page = context.new_page()

    page.goto("https://playwright.dev/python")

    theme_btn = page.get_by_title("Switch between dark and light mode (currently dark mode)")
    theme_btn.click()

    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    
    assert page.url == DOCS_URL