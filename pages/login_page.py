from common.constants import Url
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = Url.BASE_URL

    def open(self):
        self.browser.get(self.url)

    def input_user(self, username):
        self.find_element(LoginPageLocators.USER_NAME).send_keys(username)

    def input_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD).send_keys(password)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def find_element(self, locator, time=10):
        print(f"Finding element {locator}...")
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator), f"Locator {locator} was not found!")
