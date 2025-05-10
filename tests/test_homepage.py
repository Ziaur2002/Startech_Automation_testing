import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
def test_homepage_loads_with_correct_title(page):
    home = HomePage(page)
    home.visit("https://www.startech.com.bd/")
    assert "Star Tech" in home.get_title()

@pytest.mark.ui
def test_navbar_is_visible(page):
    home = HomePage(page)
    home.visit("https://www.startech.com.bd/")
    assert home.is_navbar_visible()

@pytest.mark.ui
def test_carousel_visible_on_homepage(page):
    home = HomePage(page)
    home.visit("https://www.startech.com.bd/")
    assert home.is_carousel_visible()

@pytest.mark.ui
def test_featured_products_are_listed(page):
    home = HomePage(page)
    home.visit("https://www.startech.com.bd/")
    assert home.has_featured_products()

@pytest.mark.search
def test_search_with_valid_keyword(page):
    home = HomePage(page)
    home.visit("https://www.startech.com.bd/")
    home.search_product("laptop")
    assert "search" in home.get_url().lower()
