from .base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.quantity_input = page.locator("input.qty-input")
        self.remove_button = page.locator(".remove-product")
        self.total_price = page.locator(".total-price")

    def update_quantity(self, quantity):
        self.quantity_input.fill(str(quantity))
        self.quantity_input.press("Enter")

    def remove_item(self):
        self.remove_button.click()

    def get_total_price_text(self):
        return self.total_price.text_content().strip()

    def is_cart_empty(self):
        return self.remove_button.count() == 0
