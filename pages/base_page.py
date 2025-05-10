class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def wait(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)

    def is_element_visible(self, selector):
        return self.page.locator(selector).is_visible()

    def get_element_text(self, selector):
        return self.page.locator(selector).text_content()

    def click_element(self, selector):
        self.page.locator(selector).click()

    def fill_input(self, selector, value):
        self.page.locator(selector).fill(value)

    def check_checkbox(self, selector):
        checkbox = self.page.locator(selector)
        if not checkbox.is_checked():
            checkbox.check()

    def get_url(self):
        return self.page.url

    def count_elements(self, selector):
        return self.page.locator(selector).count()
