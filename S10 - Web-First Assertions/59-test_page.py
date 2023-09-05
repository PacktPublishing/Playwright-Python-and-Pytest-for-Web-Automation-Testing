from playwright.sync_api import Page, expect

DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    
    # assert statement
    assert page.url == DOCS_URL
    # expect page url
    expect(page).to_have_url(DOCS_URL)
    # expect page title
    expect(page).to_have_title("Installation | Playwright Python")