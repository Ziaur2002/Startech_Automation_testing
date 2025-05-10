from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = page.locator("input[name='input-username']")
        self.password_input = page.locator("input[name='input-password']")
        self.login_button = page.locator("button[type='submit']")

    def perform_login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
