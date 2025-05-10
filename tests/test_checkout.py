import pytest
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.product_details_page import ProductDetailsPage

@pytest.mark.checkout
def test_guest_checkout_form_displayed(page):
    checkout = CheckoutPage(page)
    checkout.visit("https://www.startech.com.bd/checkout/onepagecheckout")
    assert checkout.first_name.is_visible()

@pytest.mark.checkout
def test_submit_billing_info_and_continue(page):
    checkout = CheckoutPage(page)
    checkout.visit("https://www.startech.com.bd/checkout/onepagecheckout")
    checkout.fill_billing_info("John", "Doe", "john@example.com", "01700000000", "123 Street", "Dhaka", "1205")
    checkout.place_order()  # Assuming proceed_to_payment is replaced by place_order
    assert checkout.is_order_successful()

@pytest.mark.checkout
def test_login_and_checkout(page):
    login = LoginPage(page)
    login.visit("https://www.startech.com.bd/account/login")
    login.perform_login("testuser@example.com", "password123")

    details = ProductDetailsPage(page)
    details.visit("https://www.startech.com.bd/haier-h32d2m-32-hd-led-television")
    details.click_add_to_cart()

    cart = CartPage(page)
    cart.visit("https://www.startech.com.bd/checkout/cart")
    page.click("a[href*='checkout']")

    checkout = CheckoutPage(page)
    checkout.fill_billing_info("Test", "User", "testuser@example.com", "01700000000", "456 Avenue", "Dhaka", "1206")
    checkout.place_order()
    assert checkout.is_order_successful()

@pytest.mark.checkout
def test_place_order(page):
    details = ProductDetailsPage(page)
    details.visit("https://www.startech.com.bd/xiaomi-mi-p1-32-inch-android-smart-tv")
    details.click_add_to_cart()

    cart = CartPage(page)
    cart.visit("https://www.startech.com.bd/checkout/cart")
    page.click("a[href*='checkout']")

    checkout = CheckoutPage(page)
    checkout.fill_billing_info("Final", "Customer", "final@example.com", "01700000000", "789 Road", "Dhaka", "1207")
    checkout.place_order()
    assert checkout.is_order_successful()
