import pytest
from pages.login_page import LogInPage


def test_login_and_logout(page):
    """
    Test a full login and logout cycle with valid credentials.
    """
    login_page = LogInPage(page)
    login_page.goto()
    # Fill in username and password and log in
    login_page.login('tomsmith', 'SuperSecretPassword!')

    # Assert successful login by checking for the success message
    assert login_page.is_success_visible()
    assert "You logged into a secure area!" in login_page.get_success_message()

    # Logout
    login_page.logout()
    # Verify that we are back on the login page
    assert page.url == login_page.url
    # Check for logout success message
    assert login_page.is_success_visible()
    assert "You logged out of the secure area!" in login_page.get_success_message()


def test_good_username_wrong_password(page):
    """
    Test login attempt with correct username but incorrect password.
    Expect an invalid password error.
    """
    login_page = LogInPage(page)
    login_page.goto()
    # Fill in wrong username and password
    login_page.login('tomsmith', 'wrongpassword!')

    # Expect an error message about invalid password
    assert login_page.is_error_visible()
    assert "Your password is invalid!" in login_page.get_error_message()


def test_wrong_login(page):
    """
    Test login attempt with incorrect username and password.
    Expect an invalid username error.
    """
    login_page = LogInPage(page)
    login_page.goto()
    # Fill in wrong username and password
    login_page.login('wronguser', 'wrongpassword!')

    # Expect an error message about invalid username
    assert login_page.is_error_visible()
    assert "Your username is invalid!" in login_page.get_error_message()


def test_empty_credentials(page):
    """
    Test login attempt with empty username and password fields.
    Expect an error indicating invalid username or password.
    """
    login_page = LogInPage(page)
    login_page.goto()
    # Leave username and password empty and submit
    login_page.login('', '')

    # Expect an error message about invalid username
    assert login_page.is_error_visible()
    assert "Your username is invalid!" in login_page.get_error_message()


def test_only_username(page):
    """
    Test submitting login form with only username filled.
    Expect an error indicating invalid password.
    """
    login_page = LogInPage(page)
    login_page.goto()
    # Leave password empty
    login_page.login('tomsmith', '')

    # Expect an error message about invalid password
    assert login_page.is_error_visible()
    assert "Your password is invalid!" in login_page.get_error_message()


def test_only_password(page):
    """
    Test submitting login form with only password filled.
    Expect an error indicating invalid username.
    """
    login_page = LogInPage(page)
    login_page.goto()
    # Leave username empty
    login_page.login('', 'SuperSecretPassword!')

    # Expect an error message about invalid username
    assert login_page.is_error_visible()
    assert "Your username is invalid!" in login_page.get_error_message()


def test_special_characters_in_credentials(page):
    """
    Test login with special characters in username and password.
    Verify system handles special characters gracefully.
    """
    special_username = "!@#$%^&*()_+"
    special_password = "<script>alert('xss')</script>"

    login_page = LogInPage(page)
    login_page.goto()
    login_page.login(special_username, special_password)

    # Expect an error message about invalid username or password
    assert login_page.is_error_visible()


def test_very_long_credentials(page):
    """
    Test login with very long username and password strings.
    Verify system handles large input gracefully.
    """
    long_username = 'user' * 50  # 200 characters
    long_password = 'pass' * 50  # 200 characters

    login_page = LogInPage(page)
    login_page.goto()
    login_page.login(long_username, long_password)

    # Expect an error message about invalid username or password
    assert login_page.is_error_visible()


def test_credentials_with_leading_trailing_spaces(page):
    """
    Test login with username and password containing leading/trailing spaces.
    Expect login failure, spaces are not trimmed.
    """
    username_with_spaces = '  tomsmith  '
    password_with_spaces = '  SuperSecretPassword!  '

    login_page = LogInPage(page)
    login_page.goto()
    login_page.login(username_with_spaces, password_with_spaces)

    # Expect an error message about invalid username or password
    assert login_page.is_error_visible()
