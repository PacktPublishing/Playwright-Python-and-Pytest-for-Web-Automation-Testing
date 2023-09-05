import pytest
from playwright.sync_api import Page, expect, Route


NOT_ALLOWED_RESOURCES = (
    "image", "font", "stylesheet", "media"
)


def on_route(route: Route):
    if route.request.resource_type in NOT_ALLOWED_RESOURCES:
        route.abort()
    else:
        route.continue_()


@pytest.fixture(autouse=True)
def skip_resources(page: Page):
    page.route("**", on_route)


def test_page_has_docs_link(page: Page):
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="docs")

    expect(link).to_be_visible()


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()

    expect(page).to_have_url(
        "https://playwright.dev/python/docs/intro"
    )