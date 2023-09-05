import re
from playwright.sync_api import Page, expect


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    
    docs_link = page.get_by_role("link", name="Docs")

    # expect exact class value
    expect(docs_link).to_have_class(
        "navbar__item navbar__link"
    )
    
    # expect class to contain value
    expect(docs_link).to_have_class(
        re.compile(r"navbar__link")
    )

    # expect id
    # expect(locator).to_have_id("value")

    # expect attribute in locator
    expect(docs_link).to_have_attribute("href")

    # expect attribute and value in locator
    expect(docs_link).to_have_attribute(
        "href", "/python/docs/intro"
    )