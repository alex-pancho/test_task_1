import pytest
from pages.locators import LoginPageLocators
from .pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_email_login_with_correct_code(browser):
    link = "https://dev1.torrow.net/app/login/auth/email/text"
    page = LoginPage(browser, link)
    page.open()
    page.login_email("asdsad@dsfsdf.sdf")
    # create new tab to extract authorization code
    browser.execute_script('''window.open("https://emaildev1.torrow.net/api/email/asdsad@dsfsdf.sdf","_blank");''')
    browser.switch_to.window(browser.window_handles[1])
    code = page.get_code(6)
    browser.switch_to.window(browser.window_handles[0])
    page.enter_code(code)
    assert browser.current_url == "https://dev1.torrow.net/app/tabs/tab-context-list" or \
        "https://dev1.torrow.net/app/registration/user-details", "Authorization failed"

def test_email_login_with_incorrect_code(browser):
    link = "https://dev1.torrow.net/app/login/auth/email/text"
    page = LoginPage(browser, link)
    page.open()
    page.login_email("asdsad@dsfsdf.sdf")
    # create new tab to extract authorization code
    browser.execute_script('''window.open("https://emaildev1.torrow.net/api/email/asdsad@dsfsdf.sdf","_blank");''')
    browser.switch_to.window(browser.window_handles[1])
    code = page.get_code(6)
    code = str(int(code[0])-1)
    browser.switch_to.window(browser.window_handles[0])
    page.enter_code(code)
    assert browser.current_url == "https://dev1.torrow.net/app/login/auth/email/code", "Authorization succeed"

def test_email_login_with_too_long_waiting(browser):
    link = "https://dev1.torrow.net/app/login/auth/email/text"
    page = LoginPage(browser, link)
    page.open()
    page.login_email("asdsad@dsfsdf.sdf")
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((LoginPageLocators.WARNING_TEXT)))
    page.should_be_warning_text()

def test_sms_login_with_correct_code(browser):
    link = "https://dev1.torrow.net/app/login/auth/phone/number"
    page = LoginPage(browser, link)
    page.open()
    page.login_sms()
    # create new tab to extract authorization code
    browser.execute_script('''window.open("https://smsdev1.torrow.net/api/phone/7911123456","_blank");''')
    browser.switch_to.window(browser.window_handles[1])
    code = page.get_code(4)
    browser.switch_to.window(browser.window_handles[0])
    page.enter_code(code)
    assert browser.current_url == "https://dev1.torrow.net/app/tabs/tab-context-list" or \
        "https://dev1.torrow.net/app/registration/user-details", "Authorization failed"

def test_sms_login_with_incorrect_code(browser):
    link = "https://dev1.torrow.net/app/login/auth/phone/number"
    page = LoginPage(browser, link)
    page.open()
    page.login_sms()
    # create new tab to extract authorization code
    browser.execute_script('''window.open("https://smsdev1.torrow.net/api/phone/7911123456","_blank");''')
    browser.switch_to.window(browser.window_handles[1])
    code = page.get_code(4)
    code = str(int(code[0])-1)
    browser.switch_to.window(browser.window_handles[0])
    page.enter_code(code)
    assert browser.current_url == "https://dev1.torrow.net/app/login/auth/phone/code", "Authorization succeed"

def test_sms_login_with_too_long_waiting(browser):
    link = "https://dev1.torrow.net/app/login/auth/phone/number"
    page = LoginPage(browser, link)
    page.open()
    page.login_sms()
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((LoginPageLocators.WARNING_TEXT)))
    page.should_be_warning_text()

