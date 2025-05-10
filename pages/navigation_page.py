from .base_page import BasePage

class NavigationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.menu_links = page.locator("nav .main-menu a")
        self.carousel = page.locator(".home-slider")

    def click_menu_item(self, item_text):
        self.page.locator(f"nav .main-menu a:has-text('{item_text}')").click()

    def is_carousel_visible(self):
        return self.carousel.is_visible()

    def get_all_menu_texts(self):
        return [link.text_content().strip() for link in self.menu_links.all()]
