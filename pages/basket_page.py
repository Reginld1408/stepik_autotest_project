from pages.base_page import BasePage
from pages.locators import MainPageLocators


class BasketPage(BasePage):
    # Basket page tests
    def should_be_view_basket_button(self):
        assert self.is_element_present(*MainPageLocators.VIEW_BASKET_BUTTON), "View basket button not present"

    def go_to_view_basket_page(self):
        link = self.browser.find_element(*MainPageLocators.VIEW_BASKET_BUTTON)
        link.click()

    def should_be_view_basket_page(self):
        # implement a check for a valid url address
        assert self.browser.current_url(*MainPageLocators.VIEW_BASKET_PAGE_URL), "View basket url is not present"

    def test_guest_basket_is_empty(self):
        basket_item_msg = self.browser.find_element(*MainPageLocators.BASKET_ITEM_MSG).text
        assert "empty" in basket_item_msg, "Basket is not empty"
