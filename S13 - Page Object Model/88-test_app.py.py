from models.login_page import LoginPage
from playwright.sync_api import Page, expect


def test_successful_login(page: Page):
    username = "dan"
    password = "pwd"

    login_page = LoginPage(page)

    login_page.login(username, password)

    expect(login_page.label).to_have_text(
        f"Welcome, {username}!"
        )


def test_failed_login(page: Page):
    username = "dan"
    password = "cnasdjc"

    login_page = LoginPage(page)

    login_page.login(username, password)

    expect(login_page.label).to_have_text(
        "Invalid username/password"
    )