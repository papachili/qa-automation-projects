from playwright.sync_api import sync_playwright


class StatusCodesPage:
    def __init__(self, Page):
        self.page = Page
        self.url = "https://the-internet.herokuapp.com/status_codes"

    def goto(self):
        self.page.goto(self.url)

    def click_status_code_link(self, status_code: str):
        """Click the link for the specified status code."""
        self.page.get_by_role("link", name=f"{status_code}").click()

    def click_here_link(self):
        """Click the 'here' link to navigate back to the status codes page."""
        self.page.get_by_role("link", name="here").click()
