import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.locators import BugsPageLocators, ProjectPageLocators
from selenium.webdriver.support import expected_conditions as EC


class BugsPage(BasePage):
    def create_new_bug(self):
        report_bug_btn = self.browser.find_element(*BugsPageLocators.REPORT_BUG_BTN)
        report_bug_btn.click()
        bug_name = self.browser.find_element(*BugsPageLocators.BUG_NAME_FIELD)
        bug_name.send_keys("Test bug")
        steps_field = self.browser.find_element(By.CSS_SELECTOR, "div.accordion-card>div:nth-child(1)>div:nth-child(2)")
        steps_field.click()
        time.sleep(2)
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(*BugsPageLocators.STEPS_FIELD)).click().send_keys(
            "_more_and_more").perform()
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.accordion-card>div:nth-child(2)>div:nth-child(2)"))).click()
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.accordion-card>div:nth-child(2)>div:nth-child(2)"))).click()
        time.sleep(2)
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(*BugsPageLocators.RESULTS_INPUT_FIELD)).click().send_keys(
            "test results").perform()
        time.sleep(2)
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.accordion-card>div:nth-child(3)>div:nth-child(2)"))).click()
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.accordion-card>div:nth-child(3)>div:nth-child(2)"))).click()
        time.sleep(2)
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(*BugsPageLocators.EXPECTATIONS_FIELD)).click().send_keys(
            "test expectations").move_to_element(self.browser.find_element(*BugsPageLocators.EXPECTATIONS_TITLE)).click().perform()
        create_bug_btn = self.browser.find_element(*BugsPageLocators.CREATE_BUG_BTN)
        create_bug_btn.click()

    def is_this_bug_page(self):
        self.browser.switch_to.frame(self.browser.find_element(*ProjectPageLocators.PROJECT_PAGE_FRAME))
        assert self.is_element_present(*BugsPageLocators.BUGS_TITLE), "This is not a bug page"

    def is_bug_present_in_the_bugs_list(self):
        assert self.is_element_present(*BugsPageLocators.CREATED_BUG), "Bug has not been created"
