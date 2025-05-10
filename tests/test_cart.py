import pytest
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage

@pytest.mark.cart
def test_add_to_cart_from_product_page(page):
    details = ProductDetailsPage(page)
    details.visit("https://www.startech.com.bd/haier-h32d2m-32-hd-led-television")
    details.page.click("btn submit-btn")
    details.wait(1000)
    cart = CartPage(page)
    cart.go_to_cart()
    assert cart.cart_quantity_input.is_visible()

@pytest.mark.cart
def test_update_quantity_in_cart(page):
    details = ProductDetailsPage(page)
    details.visit("https://www.startech.com.bd/haier-h32d2m-32-hd-led-television")
    details.page.click("btn")
    details.wait(1000)
    cart = CartPage(page)
    cart.go_to_cart()
    cart.update_quantity(2)
    cart.wait(1000)
    assert cart.cart_quantity_input.input_value() == "2"

@pytest.mark.cart
def test_remove_item_from_cart(page):
    details = ProductDetailsPage(page)
    details.visit("https://www.startech.com.bd/haier-h32d2m-32-hd-led-television")
    details.page.click("btn btn-danger")
    details.wait(1000)
    cart = CartPage(page)
    cart.go_to_cart()
    cart.remove_item()
    cart.wait(1000)
    assert cart.cart_quantity_input.count() == 0

@pytest.mark.cart
def test_cart_total_price_is_correct(page):
    details = ProductDetailsPage(page)
    details.visit("https://www.startech.com.bd/haier-h32d2m-32-hd-led-television")
    details.page.click("btn btn-primary checkout-btn")
    details.wait(1000)
    cart = CartPage(page)
    cart.go_to_cart()
    total = cart.get_total_price()
    assert total > 0
