from playwright.sync_api import Page, expect


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    get_started_link = page.get_by_role("link", name="GET STARTED")

    # expect element visible
    expect(get_started_link).to_be_visible()
    # expect element enabled
    expect(get_started_link).to_be_enabled()
    
    get_python_link = page.get_by_role("link", name="Get Python")

    # expect element hidden
    expect(get_python_link).to_be_hidden()
    # same as
    expect(get_python_link).not_to_be_visible()