from playwright.sync_api import Page


class DropdownPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/dropdown"
        self.dropdown = '#dropdown'

    def goto(self):
        self.page.goto(self.url)

    def click_dropdown(self):
        self.page.locator(self.dropdown).click()

    def select_option(self, value: str):
        self.page.select_option(self.dropdown, value)

    def get_dropdown_value(self):
        return self.page.locator(self.dropdown).input_value()
