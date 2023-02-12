from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, '//div[@class="error-message-container error"]/h3[@data-test="error"]')
