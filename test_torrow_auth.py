import pytest
import time

from pages.locators import LoginPageLocators
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.skip
def test_email_login_with_correct_code(browser):
    link = "https://dev1.torrow.net/app/login/auth/email/text"
    page = LoginPage(browser, link)
    page.open()
    page.login_email()
    browser.execute_script('''window.open("https://emaildev1.torrow.net/api/email/asdsad@dsfsdf.sdf","_blank");''')
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)
    browser.refresh()
    code = page.get_code(6)
    browser.switch_to.window(browser.window_handles[0])
    page.enter_code(code)
    # WebDriverWait(browser, 3).until(EC.url_to_be("https://dev1.torrow.net/app/tabs/tab-context-list"))
    assert browser.current_url == "https://dev1.torrow.net/app/tabs/tab-context-list" or \
        "https://dev1.torrow.net/app/registration/user-details", "Authorization failed"

@pytest.mark.skip
def test_email_login_with_incorrect_code(browser):
    link = "https://dev1.torrow.net/app/login/auth/email/text"
    page = LoginPage(browser, link)
    page.open()
    page.login_email()
    browser.execute_script('''window.open("https://emaildev1.torrow.net/api/email/asdsad@dsfsdf.sdf","_blank");''')
    browser.switch_to.window(browser.window_handles[1])
    code = "123456"
    browser.switch_to.window(browser.window_handles[0])
    page.enter_code(code)
    assert browser.current_url == "https://dev1.torrow.net/app/login/auth/email/code", "Authorization succeed"

@pytest.mark.skip
def test_email_login_with_too_long_waiting(browser):
    link = "https://dev1.torrow.net/app/login/auth/email/text"
    page = LoginPage(browser, link)
    page.open()
    page.login_email()
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((LoginPageLocators.WARNING_TEXT)))
    page.should_be_warning_text()

@pytest.mark.skip
def test_sms_login(browser):
    link = "https://dev1.torrow.net/app/login/auth/phone/number"
    page = LoginPage(browser, link)
    page.open()
    page.login_sms()

    