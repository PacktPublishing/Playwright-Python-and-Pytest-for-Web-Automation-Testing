import pytest
from creds import *
from playwright.sync_api import *


@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    headers = {
        # We set this header per GitHub guidelines.
        "Accept": "application/vnd.github.v3+json",
        # Acces token
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    context = playwright.request.new_context(
        base_url="https://api.github.com/",
        extra_http_headers=headers,
    )
    yield context
    context.dispose()


@pytest.fixture(scope="session", autouse=True)
def create_test_repository(api_context: APIRequestContext):
    # Before all
    new_repo = api_context.post("/user/repos", data={"name": GITHUB_REPO})
    assert new_repo.ok
    yield
    # After all
    deleted_repo = api_context.delete(f"/repos/{GITHUB_USER}/{GITHUB_REPO}")
    assert deleted_repo.ok