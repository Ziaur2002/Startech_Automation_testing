from .base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name = page.locator("input[name='billing[firstname]']")
        self.last_name = page.locator("input[name='billing[lastname]']")
        self.email = page.locator("input[name='billing[email]']")
        self.phone = page.locator("input[name='billing[telephone]']")
        self.address = page.locator("input[name='billing[street][]']")
        self.city = page.locator("input[name='billing[city]']")
        self.postcode = page.locator("input[name='billing[postcode]']")
        self.place_order_button = page.locator("button[title='Place Order']")
        self.success_message = page.locator(".checkout-onepage-success .page-title h1")

    def fill_billing_info(self, first, last, email, phone, address, city, postcode):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.email.fill(email)
        self.phone.fill(phone)
        self.address.fill(address)
        self.city.fill(city)
        self.postcode.fill(postcode)

    def place_order(self):
        self.place_order_button.click()

    def is_order_successful(self):
        return self.success_message.is_visible()
