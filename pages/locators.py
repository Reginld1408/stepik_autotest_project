from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inv")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    PRODUCT_PAGE_LINK = (By.XPATH, "//a[normalize-space()='All products']")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    BASKET_ITEM_MSG = (By.CSS_SELECTOR, "div[id='content_inner'] p")
    VIEW_BASKET_PAGE_URL = "https://selenium1py.pythonanywhere.com/en-gb/basket/"


class LoginPageLocators:
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    PRODUCT_PAGE_URL = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/"
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button[value='Add to basket']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] h1")
    PROD_NAME_MSG = (By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "body div div[id='content_inner'] div div p:nth-child(2)")
    PROD_PRICE_MSG = (By.CSS_SELECTOR, "div[id='messages'] p:nth-child(1)")
