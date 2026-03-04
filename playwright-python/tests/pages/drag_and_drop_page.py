from playwright.sync_api import sync_playwright


class DragAndDropPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/drag_and_drop"
        self.column_a = self.page.locator("#column-a")
        self.column_b = self.page.locator("#column-b")
        self.label_a = self.page.get_by_text("A", exact=True)
        self.label_b = self.page.get_by_text("B", exact=True)

    def goto(self):
        self.page.goto(self.url)

    def get_position(self, element):
        box = element.bounding_box()
        return box

    def label_a_position(self):
        return self.get_position(self.label_a)

    def label_b_position(self):
        return self.get_position(self.label_b)
