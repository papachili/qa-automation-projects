import pytest
from pages.checkboxes_page import CheckboxesPage


def test_checkboxes(page):
    """
    Test the checkboxes page, verifying initial state and checkbox click behavior.
    """
    checkboxes_page = CheckboxesPage(page)
    checkboxes_page.goto()

    # Assert initial state of checkboxes
    assert not checkboxes_page.checkboxes.nth(0).is_checked()
    assert checkboxes_page.checkboxes.nth(1).is_checked()

    # Click checkboxes and verify state change
    checkboxes_page.click_first_checkbox()
    assert checkboxes_page.checkboxes.nth(0).is_checked()
    checkboxes_page.click_second_checkbox()
    assert not checkboxes_page.checkboxes.nth(1).is_checked()
