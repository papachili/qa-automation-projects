import pytest
from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the login page
        page.goto("https://the-internet.herokuapp.com/login")

        # Fill in username and password
        page.fill('#username', 'thebesttester')
        page.fill('#password', 'TestingIsFun!')
        page.click('button[type="submit"]')

        # Assert successful login
        assert page.locator('.flash.success').is_visible()
        assert "You logged into a secure area!" in page.inner_text(
            '.flash.success')

        browser.close()
