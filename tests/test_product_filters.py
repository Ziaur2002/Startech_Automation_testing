from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage

def test_brand_filter_hp(page):
    home = HomePage(page)
    home.visit("https://www.startech.com.bd/laptop-notebook")
    
    product_page = ProductListingPage(page)
    product_page.apply_hp_brand_filter()
    page.wait_for_timeout(3000)
    
    assert product_page.count_filtered_products() > 0
