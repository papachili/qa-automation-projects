import pytest
from pages.dropdown_page import DropdownPage


def test_dropdown_with_select_option(page):
    """
    Test selecting options directly using the select_option method
    """
    dropdown_page = DropdownPage(page)
    dropdown_page.goto()

    # Verify that the default value is empty
    assert dropdown_page.get_dropdown_value() == ""

    # Select option with value "1"
    dropdown_page.select_option("1")
    # Verify that the selected value updates correctly
    assert dropdown_page.get_dropdown_value() == "1"

    # Select option with value "2"
    dropdown_page.select_option("2")
    # Verify the value updates again
    assert dropdown_page.get_dropdown_value() == "2"


def test_dropdown_with_keyboard(page):
    """
    Test interacting with the dropdown using keyboard navigation
    """
    dropdown_page = DropdownPage(page)
    dropdown_page.goto()

    # Verify the default value is empty
    assert dropdown_page.get_dropdown_value() == ""

    # Click to open the dropdown menu
    dropdown_page.click_dropdown()
    # Press ArrowDown to move to the first option
    page.keyboard.press('ArrowDown')
    # Press Enter to select the highlighted option
    page.keyboard.press('Enter')
    # Verify that the selected value is now "1"
    assert dropdown_page.get_dropdown_value() == "1"

    # Repeat for second option
    dropdown_page.click_dropdown()
    page.keyboard.press('ArrowDown')
    page.keyboard.press('Enter')
    # Verify that the selected value is now "2"
    assert dropdown_page.get_dropdown_value() == "2"

    # Navigate back up to the first option
    dropdown_page.click_dropdown()
    page.keyboard.press('ArrowUp')
    page.keyboard.press('Enter')
    # Verify the value is "1" again
    assert dropdown_page.get_dropdown_value() == "1"

    # Try arrow up again; should stay on "1"
    dropdown_page.click_dropdown()
    page.keyboard.press('ArrowUp')
    page.keyboard.press('Enter')
    # Confirm the value remains "1"
    assert dropdown_page.get_dropdown_value() == "1"
