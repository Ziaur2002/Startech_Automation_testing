from .base_page import BasePage

class ProductListingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.hp_brand_checkbox = page.locator("label[for='brand-hp'] input")
        self.in_stock_checkbox = page.locator("label[for='stock-yes'] input")
        self.sort_dropdown = page.locator("select[name='sort']")
        self.product_items = page.locator(".p-item")

    def apply_hp_brand_filter(self):
        self.hp_brand_checkbox.check()

    def apply_in_stock_filter(self):
        self.in_stock_checkbox.check()

    def sort_by_price_low_to_high(self):
        self.sort_dropdown.select_option("price_asc")

    def count_products(self):
        return self.product_items.count()

    def get_first_product_price(self):
        return float(
            self.page.locator(".p-item .price").first.text_content().replace(",", "").replace("৳", "").strip()
        )
