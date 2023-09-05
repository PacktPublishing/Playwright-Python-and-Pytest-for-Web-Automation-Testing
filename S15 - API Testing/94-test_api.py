from playwright.sync_api import *


def test_users_api(page: Page):
    response = page.goto("https://dummyjson.com")

    user_data = response.json()

    assert "firstName" in user_data
    assert "lastName" in user_data

    assert user_data["firstName"] == "Terry"
    assert user_data["lastName"] == "Medhurst"