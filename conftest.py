import pytest
from selenium import webdriver


# Used for every test
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    # options gets rid of "DevTools listening" in terminal
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
