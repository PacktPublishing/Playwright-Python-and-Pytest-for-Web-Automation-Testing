from playwright.sync_api import Page, expect


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    input = page.get_by_placeholder("Search docs")

    # input is hidden initially
    expect(input).to_be_hidden()

    # search button
    search_btn = page.get_by_role("button", name="Search")
    search_btn.press("Control+KeyK") 
    
    # input should be visible/editable
    expect(input).to_be_editable()
    # input should be empty initially
    expect(input).to_be_empty()

    # type some query in the input
    query = "assertions"
    input.fill(query)

    # expect the input value as query
    expect(input).to_have_value(query)