from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    # Login page tests
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    # Product page tests
    def go_to_product_page(self):
        link = self.browser.find_element(*MainPageLocators.PRODUCT_PAGE_LINK)
        link.click()

    def should_be_product_page_link(self):
        assert self.is_element_present(*MainPageLocators.PRODUCT_PAGE_LINK), "Product page link is not presented"

