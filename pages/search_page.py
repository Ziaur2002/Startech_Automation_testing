from .base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_results = page.locator(".p-item")
        self.no_results_text = page.locator(".search-result .content")

    def has_results(self):
        return self.search_results.count() > 0

    def get_no_results_message(self):
        return self.no_results_text.text_content().strip()
