import pytest
from playwright.sync_api import sync_playwright

LOGIN_URL = "https://the-internet.herokuapp.com/login"


def test_login_and_logout(page):
    """
    Test a full login and logout cycle with valid credentials.
    """
    page.goto(LOGIN_URL)
    # Fill in username and password
    page.fill('#username', 'tomsmith')
    page.fill('#password', 'SuperSecretPassword!')
    # Submit the login form
    page.click('button[type="submit"]')

    # Assert successful login by checking for the success message
    assert page.locator('.flash.success').is_visible()
    assert "You logged into a secure area!" in page.inner_text(
        '.flash.success')

    # Click on the logout link to log out
    page.click('a[href="/logout"]')

    # Verify that we are back on the login page
    assert page.url == LOGIN_URL
    # Check for logout success message
    assert page.locator('.flash.success').is_visible()
    assert "You logged out of the secure area!" in page.inner_text(
        '.flash.success')


def test_good_username_wrong_password(page):
    """
    Test login attempt with correct username but incorrect password.
    Expect an invalid password error.
    """
    page.goto(LOGIN_URL)
    # Fill in wrong username and password
    page.fill('#username', 'tomsmith')
    page.fill('#password', 'wrongpassword')
    page.click('button[type="submit"]')

    # Expect an error message about invalid password
    assert page.locator('.flash.error').is_visible()
    assert "Your password is invalid!" in page.inner_text('.flash.error')


def test_wrong_login(page):
    """
    Test login attempt with incorrect username and password.
    Expect an invalid username error.
    """
    page.goto(LOGIN_URL)
    # Fill in wrong username and password
    page.fill('#username', 'wronguser')
    page.fill('#password', 'wrongpassword')
    page.click('button[type="submit"]')

    # Expect an error message about invalid username
    assert page.locator('.flash.error').is_visible()
    assert "Your username is invalid!" in page.inner_text('.flash.error')


def test_empty_credentials(page):
    """
    Test login attempt with empty username and password fields.
    Expect an error indicating invalid username or password.
    """
    page.goto(LOGIN_URL)
    # Leave username and password empty and submit
    page.fill('#username', '')
    page.fill('#password', '')
    page.click('button[type="submit"]')

    # Expect an error message about invalid username
    assert page.locator('.flash.error').is_visible()
    assert "Your username is invalid!" in page.inner_text('.flash.error')


def test_only_username(page):
    """
    Test submitting login form with only username filled.
    Expect an error indicating invalid password.
    """
    page.goto(LOGIN_URL)
    page.fill('#username', 'tomsmith')
    # Leave password empty
    page.fill('#password', '')
    page.click('button[type="submit"]')

    # Expect an error message about invalid password
    assert page.locator('.flash.error').is_visible()
    assert "Your password is invalid!" in page.inner_text('.flash.error')


def test_only_password(page):
    """
    Test submitting login form with only password filled.
    Expect an error indicating invalid username.
    """
    page.goto(LOGIN_URL)
    # Leave username empty
    page.fill('#username', '')
    page.fill('#password', 'SuperSecretPassword!')
    page.click('button[type="submit"]')

    # Expect an error message about invalid username
    assert page.locator('.flash.error').is_visible()
    assert "Your username is invalid!" in page.inner_text('.flash.error')


def test_special_characters_in_credentials(page):
    """
    Test login with special characters in username and password.
    Verify system handles special characters gracefully.
    """
    special_username = "!@#$%^&*()_+"
    special_password = "<script>alert('xss')</script>"

    page.goto(LOGIN_URL)
    page.fill('#username', special_username)
    page.fill('#password', special_password)
    page.click('button[type="submit"]')

    # Expect an error message about invalid username or password
    assert page.locator('.flash.error').is_visible()


def test_very_long_credentials(page):
    """
    Test login with very long username and password strings.
    Verify system handles large input gracefully.
    """
    long_username = 'user' * 50  # 200 characters
    long_password = 'pass' * 50  # 200 characters

    page.goto(LOGIN_URL)
    page.fill('#username', long_username)
    page.fill('#password', long_password)
    page.click('button[type="submit"]')

    # Expect an error message about invalid username or password
    assert page.locator('.flash.error').is_visible()


def test_credentials_with_leading_trailing_spaces(page):
    """
    Test login with username and password containing leading/trailing spaces.
    Expect login failure, spaces are not trimmed.
    """
    username_with_spaces = '  tomsmith  '
    password_with_spaces = '  SuperSecretPassword!  '

    page.goto(LOGIN_URL)
    page.fill('#username', username_with_spaces)
    page.fill('#password', password_with_spaces)
    page.click('button[type="submit"]')

    # Expect an error message about invalid username or password
    assert page.locator('.flash.error').is_visible()
