import pytest
from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage

@pytest.mark.filter
def test_filter_by_hp_brand(page):
    home = HomePage(page)
    home.visit("https://www.startech.com.bd/laptop-notebook/laptop")
    listing = ProductListingPage(page)
    listing.apply_hp_brand_filter()
    listing.wait(2000)
    assert listing.count_products() > 0

@pytest.mark.filter
def test_filter_by_in_stock(page):
    home = HomePage(page)
    home.visit("https://www.startech.com.bd/component/graphics-card")
    listing = ProductListingPage(page)
    listing.apply_in_stock_filter()
    listing.wait(2000)
    assert listing.count_products() > 0

@pytest.mark.sorting
def test_sort_by_price_low_to_high(page):
    home = HomePage(page)
    home.visit("https://www.startech.com.bd/monitor")
    listing = ProductListingPage(page)
    listing.sort_by_price_low_to_high()
    listing.wait(2000)
    first_price = listing.get_first_product_price()
    assert first_price > 0
