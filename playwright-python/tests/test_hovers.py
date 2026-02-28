import pytest
from playwright.sync_api import sync_playwright

HOVERS_URL = "https://the-internet.herokuapp.com/hovers"


def test_hovers(page):
    """
    Test the hover functionality on all figures, verifying captions, profile links, and navigation.
    """
    # Navigate to the hover page
    page.goto(HOVERS_URL)

    # Locate all figure elements
    figures = page.locator("div.figure")
    count = figures.count()

    for i in range(count):
        figure = figures.nth(i)
        # Hover over the figure to reveal caption and profile link
        figure.hover()

        # Locate caption and profile link within the figure
        caption = figure.locator("div.figcaption h5")
        profile_link = figure.locator("a", has_text="View profile")

        # Wait for caption and profile link to become visible
        caption.wait_for(state="visible", timeout=5000)
        profile_link.wait_for(state="visible", timeout=5000)

        # Extract the caption text (username)
        name = caption.inner_text()

        # Verify caption is not empty
        assert name.strip() != "", "Caption should contain username"

        # Verify profile link is visible after hover
        assert profile_link.is_visible(), "Profile link should be visible after hover"

        # Verify link text
        link_text = profile_link.inner_text()
        assert "View profile" in link_text, "Link text should be 'View profile'"

        # Get the href attribute from the profile link
        href = profile_link.get_attribute("href")
        # Verify the href pattern
        assert href.startswith(
            "/users/"), f"Profile link href should start with /users/ but got {href}"

        # Extract the user ID from href
        user_identifier = href.split("/users/")[-1]
        # Construct the expected full URL
        expected_url = f"https://the-internet.herokuapp.com/users/{user_identifier}"

        # Click the profile link
        profile_link.click()

        # Verify URL contains the expected path
        current_url = page.url
        assert current_url == expected_url, f"Expected URL: {expected_url}, but got {current_url}"
        print(f"Navigated to: {current_url}")

        # Go back to the original page
        page.go_back()
        page.wait_for_load_state("load")
