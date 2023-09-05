from creds import *
from playwright.sync_api import *


def test_create_issue(api_context: APIRequestContext):
    issue_data = {
        "title": "[Bug] That failed",
        "body": "When running this, that failed with error.",
    }

    issue = api_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues",
        data=issue_data,
    )

    assert issue.ok


def test_issue_page(page: Page):
    page.goto(f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues")
    page.screenshot(path="issues-page.jpg", full_page=True)


def test_new_issue_created(api_context: APIRequestContext):
    all_issues = api_context.get(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues",
    )

    assert all_issues.ok

    new_issue = [
        issue 
        for issue in all_issues.json()
        if issue["title"] == "[Bug] That failed"
    ][0]

    assert new_issue["body"] == "When running this, that failed with error."