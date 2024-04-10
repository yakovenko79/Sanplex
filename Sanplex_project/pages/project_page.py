import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.locators import ProjectPageLocators

PROJECT_NAME = "AutoProject"


class ProjectPage(BasePage):

    def should_this_project_page(self):

        assert "project-browse" in self.browser.current_url, "another page is displayed"

    def create_new_project(self):
        self.browser.switch_to.frame(self.browser.find_element(*ProjectPageLocators.PROJECT_PAGE_FRAME))
        create_project_btn = self.browser.find_element(*ProjectPageLocators.CREATE_PROJECT_BTN)
        create_project_btn.click()
        project_name_field = self.browser.find_element(*ProjectPageLocators.PROJECT_NAME)
        project_name_field.send_keys(PROJECT_NAME)
        description_frame = self.browser.find_element(By.CLASS_NAME, "show-desc")
        description_frame.click()
        ActionChains(self.browser).move_to_element(self.browser.find_element(By.CSS_SELECTOR, "zen-editor")).click().send_keys(
            "test_description").perform()
        time.sleep(2)
        radio_btn_0 = self.browser.find_element(*ProjectPageLocators.RADIOBUTTON_TURN_OFF)
        radio_btn_0.click()
        radio_btn_1 = self.browser.find_element(*ProjectPageLocators.RADIOBUTTON_TURN_ON)
        radio_btn_1.click()
        date_from = self.browser.find_element(*ProjectPageLocators.DATE_FROM)
        date_from.click()
        date_date_from = self.browser.find_element(*ProjectPageLocators.DATE_DATE_FROM)
        date_date_from.click()
        time.sleep(2)
        date_to = self.browser.find_element(*ProjectPageLocators.DATE_TO)
        date_to.click()
        date_date_to = self.browser.find_element(*ProjectPageLocators.DATE_DATE_TO)
        date_date_to.click()
        submit_btn = self.browser.find_element(*ProjectPageLocators.SUBMIT_BTN)
        submit_btn.click()

    def switch_tab_all(self):
        tab_all = self.browser.find_element(*ProjectPageLocators.SWITCH_TAB_ALL)
        tab_all.click()

    def should_project_in_a_projects_list(self):
        name_project = self.browser.find_elements(*ProjectPageLocators.PROJECTS_LIST)
        lst = []
        for element in name_project:
            lst.append(element.text)
            print("element: ", element.text)
        assert PROJECT_NAME in lst, "No project"
