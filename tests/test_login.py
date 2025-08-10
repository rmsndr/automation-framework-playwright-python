import pytest
from playwright.sync_api import Page
#from playwright import browser_context
from pages.LoginPage import LoginPage

from utils.accessibility_utils import accessibility_utils

@pytest.mark.login
def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"
    assert page.locator(".inventory_list").is_visible()
    print("Login successful. User is on the inventory page.")


@pytest.mark.skip(reason="This test is for invalid login scenarios")
@pytest.mark.login
def test_invalid_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("invalid_user", "wrong_password")
    
    assert page.url == "https://www.saucedemo.com/"
    assert page.locator(".error-message-container").is_visible()
    assert "Username and password do not match" in page.locator(".error-message-container").text_content()