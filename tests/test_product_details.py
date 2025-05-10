import pytest
from pages.product_details_page import ProductDetailsPage

@pytest.mark.details
def test_image_gallery_displayed(page):
    details = ProductDetailsPage(page)
    details.visit("https://www.startech.com.bd/haier-h32d2m-32-hd-led-television")
    assert details.is_image_gallery_visible()

@pytest.mark.details
def test_availability_status_shown(page):
    details = ProductDetailsPage(page)
    details.visit("https://www.startech.com.bd/haier-h32d2m-32-hd-led-television")
    status = details.get_availability_status()
    assert status != ""

@pytest.mark.details
def test_add_to_cart_button_visible(page):
    details = ProductDetailsPage(page)
    details.visit("https://www.startech.com.bd/haier-h32d2m-32-hd-led-television")
    assert details.is_add_to_cart_button_visible()
