from playwright.sync_api import Page


def test_scrollbars(page: Page):
    page.goto("http://uitestingplayground.com/scrollbars")
    
    btn = page.get_by_role("button", name="Hiding Button")

    btn.scroll_into_view_if_needed()
    # click also ensures the above
    # btn.click()

    page.screenshot(path="test-scrollbars.jpg")