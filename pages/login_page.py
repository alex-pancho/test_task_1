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

    def login_email(self):
        country = self.browser.find_element(*LoginPageLocators.COUNTRY_INPUT)
        country.click()
        country_option = self.browser.find_element(*LoginPageLocators.COUNTRY_OPTION)
        country_option.click()
        email = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email.send_keys("asdsad@dsfsdf.sdf")
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.click()

    def get_code(self):
        html = self.browser.page_source
        #search using regex 
        x = re.findall('[0-9]+', html)
        
        def filterNumber(n):
            if len(n) == 6:
                return True
            else:
                return False
        
        code = list(filter(filterNumber, x))
        return code
    
    def enter_code(self, code):
        print(code)
        for i in code[0]:
            number = self.browser.find_element(By.CSS_SELECTOR, selector_numbers[i])
            number.click()
        





