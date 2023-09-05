from playwright.sync_api import *


def test_users_api(playwright: Playwright):
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
    )

    response = api_context.get("/users/1")

    user_data = response.json()

    assert "firstName" in user_data
    assert "lastName" in user_data

    assert user_data["firstName"] == "Terry"
    assert user_data["lastName"] == "Medhurst"