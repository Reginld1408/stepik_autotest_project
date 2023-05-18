from pages.base_page import BasePage
from pages.locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()

    def should_be_login_url(self):
        # implement a check for a valid url address
        assert self.browser.current_url(*LoginPageLocators.LOGIN_URL), "Login url is not present"

    def should_be_login_form(self):
        # implement a check that there is a login form
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # implement a check that there is a registration form on the page
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"





