from playwright.sync_api import sync_playwright, expect


class DynamicLoadingPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/dynamic_loading"
        self.loading_indicator = self.page.locator("#loading").get_by_role(
            "img")
        self.start_button = self.page.get_by_role("button", name="Start")
        self.hello_world_heading = self.page.get_by_role(
            "heading", name="Hello World!")

    def goto(self):
        self.page.goto(self.url)

    def click_example_1(self):
        self.page.get_by_role(
            "link", name="Example 1: Element on page").click()

    def click_example_2(self):
        self.page.get_by_role(
            "link", name="Example 2: Element rendered").click()

    def click_start_button(self):
        self.start_button.click()
