from playwright.sync_api import Page


class LogInPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/login"
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = 'button[type="submit"]'
        self.logout_link = 'a[href="/logout"]'
        self.success_message = ".flash.success"
        self.error_message = ".flash.error"

    def goto(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def logout(self):
        self.page.click(self.logout_link)

    def get_success_message(self):
        return self.page.inner_text(self.success_message)

    def get_error_message(self):
        return self.page.inner_text(self.error_message)

    def is_success_visible(self):
        return self.page.locator(self.success_message).is_visible()

    def is_error_visible(self):
        return self.page.locator(self.error_message).is_visible()
