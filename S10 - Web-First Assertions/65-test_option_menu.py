from playwright.sync_api import Page, expect


def test_app(page: Page):
    page.goto("https://bootswatch.com/default")
    
    option_menu = page.get_by_label("Example select")
    
    # expect selected option
    expect(option_menu).to_have_value("1")

    multi_option_menu = page.get_by_label("Example multiple select")
    multi_option_menu.select_option(["2", "4"])

    # expect selected options
    expect(multi_option_menu).to_have_values(["2", "4"])