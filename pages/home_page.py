from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.locator("input[type='search']")
        self.search_button = page.locator("button.search-button")
        self.result_items = page.locator(".product-list .product-title")
        self.brand_filter_checkbox = lambda brand: page.locator(f"label:has-text('{brand}') input[type='checkbox']")

    def is_search_bar_visible(self):
        return self.search_input.is_visible()

    def search(self, query):
        self.search_input.fill(query)
        self.search_input.press("Enter")

    def are_search_results_visible(self):
        return self.result_items.first.is_visible()

    def apply_brand_filter(self, brand):
        self.brand_filter_checkbox(brand).check()

    def are_filtered_results_displayed(self, brand_name):
        return self.result_items.nth(0).text_content().lower().__contains__(brand_name.lower())
