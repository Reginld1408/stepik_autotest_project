from pages.product_page import ProductPage
from pages.basket_page import BasketPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    browser.get(link)
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/"
    browser.get(link)
    page = BasketPage(browser, link)
    page.go_to_view_basket_page()
    page.test_guest_basket_is_empty()


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    browser.get(link)
    page = ProductPage(browser, link)
    page.should_not_be_success_message()
    page.should_be_clickable_basket_btn()
    page.prod_name_match_prod_msg()
    page.prod_price_match_prod_price_msg()


