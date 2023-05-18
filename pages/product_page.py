from pages.main_page import MainPage
from pages.locators import ProductPageLocators


class ProductPage(MainPage):

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PROD_NAME_MSG), \
            "Success message is presented, but should not be"

    def should_be_clickable_basket_btn(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def prod_name_match_prod_msg(self):
        prod_name_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        prod_msg_text = self.browser.find_element(*ProductPageLocators.PROD_NAME_MSG).text
        assert prod_name_text in prod_msg_text, "The product name is not found in the product message"

    def prod_price_match_prod_price_msg(self):
        prod_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        prod_price_msg = self.browser.find_element(*ProductPageLocators.PROD_PRICE_MSG)
        assert prod_price.text in prod_price_msg.text, "The product price is not found in the product price message"








