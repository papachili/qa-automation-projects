import pytest
from pages.status_codes_page import StatusCodesPage


# List of expected status codes to verify
EXPECTED_STATUS_CODES = ["200", "301", "404", "500"]


def test_status_codes(page):
    """
    Test the status codes page by verifying that clicking on each status code link
    navigates to the correct page displaying the expected status code message.
    """
    status_codes_page = StatusCodesPage(page)
    status_codes_page.goto()

    for status_code in EXPECTED_STATUS_CODES:
        # Click on the link corresponding to the current status code
        status_codes_page.click_status_code_link(status_code)

        # Verify the correct status code message is displayed
        assert f"This page returned a {status_code} status code" in page.text_content(
            "div.example p")

        # Navigate back to the status codes page for the next iteration
        page.go_back()


def test_status_codes_and_clik_here_link(page):
    """
    Test the status codes page by verifying that clicking on each status code link
    navigates to the correct page and then clicking the 'click here' link returns to the main page.
    """
    status_codes_page = StatusCodesPage(page)
    status_codes_page.goto()

    for status_code in EXPECTED_STATUS_CODES:
        # Click on the link corresponding to the current status code
        status_codes_page.click_status_code_link(status_code)

        # Verify the correct status code message is displayed
        assert f"This page returned a {status_code} status code" in page.text_content(
            "div.example p")

        # Click on the 'click here' link to return to the main status codes page
        status_codes_page.click_here_link()
