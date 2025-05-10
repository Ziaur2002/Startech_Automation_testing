from .base_page import BasePage

class ProductDetailsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_to_cart_button = page.locator("button.add-to-cart")
        self.product_availability = page.locator(".stock-availability")
        self.image_gallery = page.locator(".product-image-gallery img")

    def click_add_to_cart(self):
        self.add_to_cart_button.click()

    def is_add_to_cart_visible(self):
        return self.add_to_cart_button.is_visible()

    def is_image_gallery_displayed(self):
        return self.image_gallery.first.is_visible()

    def get_availability_status(self):
        return self.product_availability.text_content().strip()