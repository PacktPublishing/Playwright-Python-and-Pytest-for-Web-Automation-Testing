from playwright.sync_api import Page, expect


def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/dynamicid")

    button = page.get_by_role(
        "button", name="Button with Dynamic ID"
    )
    expect(button).to_be_visible()

    button.click()