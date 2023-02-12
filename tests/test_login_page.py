import pytest
from pages.login_page import LoginPage
from time import sleep
from pages.locators import LoginPageLocators

@pytest.fixture()
def main_page(browser):
    main_page = LoginPage(browser)
    main_page.open()
    return main_page


def test_main_page(main_page):
    main_page.input_user('standard_user')
    main_page.input_password('secret_sauce')
    main_page.click_login()
    sleep(3)


def test_main_page_negative(main_page):
    main_page.input_user('standard_user')
    main_page.input_password('araswori_paroli')
    main_page.click_login()
    expected_text = "Epic sadface: Username and password do not match any user in this service"
    actual_text = main_page.find_element(LoginPageLocators.ERROR_MESSAGE).text
    assert actual_text == expected_text


def test_main_page_negative_username(main_page):
    main_page.input_user('araswori_username')
    main_page.input_password('secret_sauce')
    main_page.click_login()
    expected_text = "Epic sadface: Username and password do not match any user in this service"
    actual_text = main_page.find_element(LoginPageLocators.ERROR_MESSAGE).text
    assert actual_text == expected_text