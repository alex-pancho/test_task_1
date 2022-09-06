from selenium.webdriver.common.by import By


class LoginPageLocators():
    COUNTRY_INPUT = (By.CSS_SELECTOR, "#country-autocomplete-input")
    COUNTRY_OPTION = (By.CSS_SELECTOR, "#mat-option-0")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#mat-input-1")
    PHONE_INPUT = (By.CSS_SELECTOR, "input.phone-input-label")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.submit-button")
    CODE = (By.CSS_SELECTOR, ".ng-untouched")
    WARNING_TEXT = (By.CSS_SELECTOR, ".warning-text")

    