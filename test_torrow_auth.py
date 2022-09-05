import pytest
import time
from .pages.base_page import BasePage
from .pages.login_page import LoginPage


def test_email_login(browser):
    link = "https://dev1.torrow.net/app/login/auth/email/text"
    page = LoginPage(browser, link)
    page.open()
    page.login_email()
    browser.execute_script('''window.open("https://emaildev1.torrow.net/api/email/asdsad@dsfsdf.sdf","_blank");''')
    browser.switch_to.window(browser.window_handles[1])
    browser.refresh()
    code = page.get_code()
    browser.switch_to.window(browser.window_handles[0])
    page.enter_code(code)



