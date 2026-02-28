from playwright.sync_api import sync_playwright
from typing import List


class CheckboxesPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/checkboxes"

    def goto(self):
        self.page.goto(self.url)

    @property
    def checkboxes(self) -> Locator:
        return self.page.locator("#checkboxes input")

    def click_first_checkbox(self):
        """Click the first checkbox."""
        self.checkboxes.nth(0).click()

    def click_second_checkbox(self):
        """Click the second checkbox."""
        self.checkboxes.nth(1).click()
