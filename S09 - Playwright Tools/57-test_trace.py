import pytest
from playwright.sync_api import BrowserContext, Page

DOCS_URL = "https://playwright.dev/python/docs/intro"


@pytest.fixture(autouse=True)
def trace_test(context: BrowserContext):
    # start tracing
    context.tracing.start(
        name="playwright",
        screenshots=True,
        snapshots=True,
        sources=True,
    )
    # pause until test function finishes
    yield
    # stop tracing and save it
    context.tracing.stop(path="trace.zip")


def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    
    assert page.url == DOCS_URL