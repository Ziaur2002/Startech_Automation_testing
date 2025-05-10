import pytest
from pages.home_page import HomePage

@pytest.mark.search
def test_search_bar_visibility(page):
    home = HomePage(page)
    home.visit("https://www.startech.com.bd")
    assert home.is_search_bar_visible()

@pytest.mark.search
def test_search_for_product(page):
    home = HomePage(page)
    home.visit("https://www.startech.com.bd/amd-ryzen-5-3400g-processor")
    home.search("laptop")
    assert home.are_search_results_visible()

@pytest.mark.search
def test_apply_brand_filter(page):
    home = HomePage(page)
    home.visit("https://www.startech.com.bd/laptop")
    home.apply_brand_filter("HP")
    assert home.are_filtered_results_displayed("HP")
