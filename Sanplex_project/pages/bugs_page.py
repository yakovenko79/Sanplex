import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.locators import BugsPageLocators, ProjectPageLocators
from selenium.webdriver.support import expected_conditions as EC


class BugsPage(BasePage):
    def create_new_bug(self):
        """Create a new bug"""
        report_bug_btn = self.browser.find_element(*BugsPageLocators.REPORT_BUG_BTN)
        report_bug_btn.click()
        bug_name = self.browser.find_element(*BugsPageLocators.BUG_NAME_FIELD)
        bug_name.send_keys("Test bug")
        steps_field = self.browser.find_element(By.CSS_SELECTOR, "div.accordion-card>div:nth-child(1)>div:nth-child(2)")
        steps_field.click()
        time.sleep(2)
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(*BugsPageLocators.STEPS_FIELD)).click().send_keys(
            " more and_more").perform()
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
            "test expectations").move_to_element(
            self.browser.find_element(*BugsPageLocators.EXPECTATIONS_TITLE)).click().perform()
        create_bug_btn = self.browser.find_element(*BugsPageLocators.CREATE_BUG_BTN)
        create_bug_btn.click()

    def is_this_bug_page(self):
        """Check this is a bug page"""
        self.browser.switch_to.frame(self.browser.find_element(*ProjectPageLocators.PROJECT_PAGE_FRAME))
        assert self.is_element_present(*BugsPageLocators.BUGS_TITLE), "This is not a bug page"

    def is_bug_present_in_the_bugs_list(self):
        """Check that the bug is in the bugs list"""
        assert self.is_element_present(*BugsPageLocators.CREATED_BUG), "Bug has not been created"

    def edit_bug(self):
        """Edit bug"""
        test_bug = self.browser.find_element(*BugsPageLocators.TEST_BUG)
        test_bug.click()
        time.sleep(2)
        print(self.browser.find_element(*BugsPageLocators.TITLE_BUG).text)
        assert self.browser.find_element(*BugsPageLocators.TITLE_BUG).text == "Test bug"
        edit_btn = self.browser.find_element(*BugsPageLocators.EDIT_BUG_BTN)
        edit_btn.click()
        bug_name = self.browser.find_element(*BugsPageLocators.BUG_NAME_FIELD)
        bug_name.send_keys(" edited")
        steps_field = self.browser.find_element(By.CSS_SELECTOR, "div.accordion-card>div:nth-child(1)>div:nth-child(2)")
        steps_field.click()
        time.sleep(1)
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(*BugsPageLocators.STEPS_FIELD)).click().send_keys(
            " _edited").perform()
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.accordion-card>div:nth-child(2)>div:nth-child(2)"))).click()
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.accordion-card>div:nth-child(2)>div:nth-child(2)"))).click()
        time.sleep(1)
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(*BugsPageLocators.RESULTS_INPUT_FIELD)).click().send_keys(
            " edited").perform()
        time.sleep(1)
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.accordion-card>div:nth-child(3)>div:nth-child(2)"))).click()
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.accordion-card>div:nth-child(3)>div:nth-child(2)"))).click()
        time.sleep(2)
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(*BugsPageLocators.EXPECTATIONS_FIELD)).click().send_keys(
            " edited").move_to_element(
            self.browser.find_element(*BugsPageLocators.EXPECTATIONS_TITLE)).click().perform()
        priority_dd_btn = self.browser.find_element(*BugsPageLocators.PRIORITY_DD_BTN)
        priority_dd_btn.click()
        priority_dd = self.browser.find_element(*BugsPageLocators.PRIORITY_DD_BTN)
        priority_dd.click()
        urgent_priority = self.browser.find_element(*BugsPageLocators.URGENT_PRIORITY)
        urgent_priority.click()
        severity_dd_btn = self.browser.find_element(*BugsPageLocators.SEVERITY_DD_BTN)
        severity_dd_btn.click()
        critical_severity = self.browser.find_element(*BugsPageLocators.CRITICAL_SEVERITY)
        critical_severity.click()
        save_edit_bug_btn = self.browser.find_element(*BugsPageLocators.SAVE_EDIT_BUG_BTN)
        save_edit_bug_btn.click()

    def is_bug_edited(self):
        """Check that the edited bug is in the bugs list"""
        assert self.is_element_present(*BugsPageLocators.EDITED_TITLE_BUG_IN_BUGS_LIST), ("Edited bug isn't in the "
                                                                                          "bugs list")

    def delete_bug(self):
        """Delete the edited bug"""
        test_edited_bug = self.browser.find_element(*BugsPageLocators.TEST_EDITED_BUG)
        test_edited_bug.click()
        time.sleep(2)
        assert self.browser.find_element(*BugsPageLocators.TITLE_EDITED_BUG).text == "Test bug edited", ("This is not "
                                                                                                         "a bug"
                                                                                                         "for deleting")
        delete_btn = self.browser.find_element(*BugsPageLocators.DELETE_BUG_BTN)
        delete_btn.click()
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.item.toolbar-item.btn-wide.primary"))).click()

    def is_bug_deleted(self):
        """Check if a bug has been deleted"""
        time.sleep(2)
        assert self.is_element_not_present(*BugsPageLocators.TEST_EDITED_BUG), "Bug wasn't deleted"

