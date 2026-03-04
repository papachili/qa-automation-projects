import pytest
from pages.dynamic_loading_page import DynamicLoadingPage
from playwright.sync_api import expect


TIMEOUT = 10000


def test_dynamic_loading(page: Page):
    """
    Test the dynamic loading functionality on the page.
    This test navigates through two examples of dynamic loading,
    waits for the loading indicator to appear and then disappear,
    and verifies that the "Hello World" message appears after loading completes.
    """
    dynamic_loading_page = DynamicLoadingPage(page)
    dynamic_loading_page.goto()

    # Test Example 1
    dynamic_loading_page.click_example_1()
    # Wait for the start button to be visible
    expect(dynamic_loading_page.start_button).to_be_visible(timeout=TIMEOUT)
    # Click the start button
    dynamic_loading_page.click_start_button()
    # Wait the start button to disappear
    expect(dynamic_loading_page.start_button).to_be_hidden(timeout=TIMEOUT)
    # Wait for the loading indicator to appear
    expect(dynamic_loading_page.loading_indicator).to_be_visible(timeout=TIMEOUT)
    # Wait for loading indicator to disappear
    expect(dynamic_loading_page.loading_indicator).to_be_hidden(timeout=TIMEOUT)
    expect(dynamic_loading_page.hello_world_heading).to_be_visible(
        timeout=TIMEOUT)

    # Reset to main page before testing example 2
    dynamic_loading_page.goto()

    # Test Example 2
    dynamic_loading_page.click_example_2()
    # Wait for the start button to be visible
    expect(dynamic_loading_page.start_button).to_be_visible(timeout=TIMEOUT)
    # Click the start button
    dynamic_loading_page.click_start_button()
    # Wait the start button to disappear
    expect(dynamic_loading_page.start_button).to_be_hidden(timeout=TIMEOUT)
    # Wait for the loading indicator to appear
    expect(dynamic_loading_page.loading_indicator).to_be_visible(timeout=TIMEOUT)
    # Wait for loading indicator to disappear
    expect(dynamic_loading_page.loading_indicator).to_be_hidden(timeout=TIMEOUT)
    expect(dynamic_loading_page.hello_world_heading).to_be_visible(
        timeout=TIMEOUT)
