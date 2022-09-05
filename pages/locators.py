from selenium.webdriver.common.by import By


class BasePageLocators():
    BODY = (By.CSS_SELECTOR, 'body')

class LoginPageLocators():
    COUNTRY_INPUT = (By.CSS_SELECTOR, "#country-autocomplete-input")
    COUNTRY_OPTION = (By.CSS_SELECTOR, "#mat-option-0")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#mat-input-1")
    LOGIN_BTN = (By.CSS_SELECTOR, "button.submit-button")
    CODE_INPUT = (By.CSS_SELECTOR, ".ng-untouched")
    NUMBER_ONE_INPUT = (By.CSS_SELECTOR, "ion-row:nth-child(1) > ion-col:nth-child(1) > button")
    

    