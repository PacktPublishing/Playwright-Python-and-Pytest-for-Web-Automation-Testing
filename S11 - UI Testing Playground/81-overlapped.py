from playwright.sync_api import Page, expect


def test_overlapped(page: Page):
    page.goto("http://uitestingplayground.com/overlapped")
    
    input = page.get_by_placeholder("Name")

    # mouse-over scroll area
    div = input.locator("..")
    div.hover()

    # scroll by 200 pixels horizontally
    page.mouse.wheel(0, 200)

    # fill data
    data = "python"
    input.fill(data)

    # take screenshot of scroll-area
    div.screenshot(path="test-overlapped.jpg")

    expect(input).to_have_value(data)