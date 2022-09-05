from selenium.webdriver.common.by import By


class BasePageLocators():
    BODY = (By.CSS_SELECTOR, 'body')

class LoginPageLocators():
    COUNTRY = (By.CSS_SELECTOR, "#country-autocomplete-input")
    COUNTRY_OPTION = (By.CSS_SELECTOR, "#mat-option-0")
    LOGIN = (By.CSS_SELECTOR, "#mat-input-1")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.submit-button")
    CODE = (By.CSS_SELECTOR, ".ng-untouched")
    WARNING_TEXT = (By.CSS_SELECTOR, ".warning-text")

    