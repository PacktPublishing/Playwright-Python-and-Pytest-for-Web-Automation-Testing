from playwright.sync_api import Page, expect


def test_text_input(page: Page):
    page.goto("http://uitestingplayground.com/textinput")
    # text input value
    great_stuff = "great stuff"
    # fill value
    input = page.get_by_label("Set New Button Name")
    input.fill(great_stuff)
    # click button
    btn = page.locator("button.btn-primary")
    btn.click()
    # expect button text to be input value
    expect(btn).to_have_text(great_stuff)