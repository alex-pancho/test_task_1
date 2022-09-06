import re
from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

selector_numbers = {
    "0": "ion-row:nth-child(4) > ion-col:nth-child(2) > button",
    "1": "ion-row:nth-child(1) > ion-col:nth-child(1) > button",
    "2": "ion-row:nth-child(1) > ion-col:nth-child(2) > button",
    "3": "ion-row:nth-child(1) > ion-col:nth-child(3) > button",
    "4": "ion-row:nth-child(2) > ion-col:nth-child(1) > button",
    "5": "ion-row:nth-child(2) > ion-col:nth-child(2) > button",
    "6": "ion-row:nth-child(2) > ion-col:nth-child(3) > button",
    "7": "ion-row:nth-child(3) > ion-col:nth-child(1) > button",
    "8": "ion-row:nth-child(3) > ion-col:nth-child(2) > button",
    "9": "ion-row:nth-child(3) > ion-col:nth-child(3) > button",
}

class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def login_email(self, email):
        country = self.browser.find_element(*LoginPageLocators.COUNTRY_INPUT)
        country.click()
        country_option = self.browser.find_element(*LoginPageLocators.COUNTRY_OPTION)
        country_option.click()
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_btn.click()

    def login_sms(self):
        phone = self.browser.find_element(*LoginPageLocators.PHONE_INPUT)
        phone.click()
        phone.send_keys("911123456")
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_btn.click()
        
    def get_code(self, chars):
        html = self.browser.page_source
        #search using regex 
        x = re.findall('[0-9]+', html)
        
        def filterNumber(n):
            if len(n) == chars:
                return True
            else:
                return False
        
        code = list(filter(filterNumber, x))
        return code
    
    def enter_code(self, code):
        for i in code[0]:
            number = self.browser.find_element(By.CSS_SELECTOR, selector_numbers[i])
            number.click()

    def should_be_warning_text(self):
        assert self.is_element_present(*LoginPageLocators.WARNING_TEXT), "Warning text is not presented"




