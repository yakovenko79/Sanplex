from selenium.common import NoSuchElementException

from Sanplex_project.pages.locators import LoginLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.set_window_size(1920, 1080)
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def login(self, user, pswd):
        username = self.browser.find_element(*LoginLocators.USERNAME)
        username.send_keys(user)
        password = self.browser.find_element(*LoginLocators.PASSWORD)
        password.send_keys(pswd)
        button = self.browser.find_element(*LoginLocators.BUTTON)
        button.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_not_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return True
        return False



