from playwright.sync_api import Page


class HoversPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/hovers"
        self.figure_locator = self.page.locator("div.figure")

    def goto(self):
        self.page.goto(self.url)

    def get_figures(self):
        return self.figure_locator

    def hover_over_figure(self, index: int):
        figure = self.figure_locator.nth(index)
        figure.hover()

    def get_caption_and_profile_link(self, index: int):
        figure = self.figure_locator.nth(index)
        caption = figure.locator("div.figcaption h5")
        profile_link = figure.locator("a", has_text="View profile")
        return caption, profile_link

    def get_figure_count(self):
        return self.figure_locator.count()
