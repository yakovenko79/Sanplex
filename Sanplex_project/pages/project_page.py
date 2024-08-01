import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.locators import ProjectPageLocators

PROJECT_NAME = "AutoProject"


class ProjectPage(BasePage):

    def should_this_project_page(self):
        """Returns True if the project page should be"""
        assert self.is_element_present(*ProjectPageLocators.PROJECT_PAGE_FRAME), "another page is displayed"

    def create_new_project(self):
        """Creates a new project"""
        self.browser.switch_to.frame(self.browser.find_element(*ProjectPageLocators.PROJECT_PAGE_FRAME))
        create_project_btn = self.browser.find_element(*ProjectPageLocators.CREATE_PROJECT_BTN)
        create_project_btn.click()
        project_name_field = self.browser.find_element(*ProjectPageLocators.PROJECT_NAME)
        project_name_field.send_keys(PROJECT_NAME)
        description_frame = self.browser.find_element(*ProjectPageLocators.DESCRIPTION)
        time.sleep(2)
        description_frame.click()
        ActionChains(self.browser).move_to_element(self.browser.find_element(*ProjectPageLocators.ZEN_EDITOR)).click().send_keys(
            "test_description").perform()
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
        """Switch to tab all"""
        tab_all = self.browser.find_element(*ProjectPageLocators.SWITCH_TAB_ALL)
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(tab_all))
        tab_all.click()

    def should_project_in_a_projects_list(self):
        """Check if project is in a list of projects"""
        assert self.is_element_present(*ProjectPageLocators.NAME_OF_CREATED_PROJECT)

    def dropdown_project_box(self):
        """Pressing the 3 dots dropdown project box button"""
        box = self.browser.find_element(*ProjectPageLocators.DROPDOWN_PROJECT_BOX)
        box.click()

    def switch_tab_all_edit(self):
        """Switch to tab all"""
        self.browser.switch_to.frame(self.browser.find_element(*ProjectPageLocators.PROJECT_PAGE_FRAME))
        tab_all = self.browser.find_element(*ProjectPageLocators.ALL_TAB)
        tab_all.click()
        time.sleep(1)

    def edit_project(self):
        """Editing the project"""
        edit_project_btn = self.browser.find_element(*ProjectPageLocators.EDIT_PROJECT)
        edit_project_btn.click()
        time.sleep(3)
        name_project = self.browser.find_element(*ProjectPageLocators.PROJECT_NAME).text
        assert name_project == "AutoProject", "Not your project"
        project_name = self.browser.find_element(*ProjectPageLocators.PROJECT_NAME)
        project_name.send_keys("_updated")
        description_frame = self.browser.find_element(*ProjectPageLocators.DESCRIPTION)
        description_frame.click()
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(*ProjectPageLocators.ZEN_EDITOR)).click().send_keys(
            "_more_and_more").perform()
        date_from = self.browser.find_element(*ProjectPageLocators.DATE_FROM)
        date_from.click()
        time.sleep(1)
        date_date_from = self.browser.find_element(*ProjectPageLocators.DATE_DATE_FROM_UPDATE)
        date_date_from.click()
        date_to = self.browser.find_element(*ProjectPageLocators.DATE_TO)
        date_to.click()
        time.sleep(1)
        date_date_to = self.browser.find_element(*ProjectPageLocators.DATE_DATE_TO_UPDATE)
        date_date_to.click()
        time.sleep(1)
        show_additional = self.browser.find_element(*ProjectPageLocators.SHOW_ADDIT_FIELDS)
        show_additional.click()
        pm_field = self.browser.find_element(*ProjectPageLocators.PROJECT_MANAGER_FIELD)
        pm_field.click()
        pm_person = self.browser.find_element(*ProjectPageLocators.PROJECT_MANAGER)
        pm_person.click()
        budget = self.browser.find_element(*ProjectPageLocators.BUDGET_FIELD)
        budget.send_keys(5)
        submit_btn = self.browser.find_element(*ProjectPageLocators.SUBMIT_BTN)
        submit_btn.click()

    def should_update_project_in_a_projects_list(self):
        """Check updated project is in a project list"""
        assert self.is_element_present(*ProjectPageLocators.NAME_OF_UPDATED_PROJECT), "Project doesn't exist"

    def delete_project(self):
        """Deleting a project"""
        assert self.is_element_present(*ProjectPageLocators.NAME_OF_UPDATED_PROJECT)
        delete_project_btn = self.browser.find_element(*ProjectPageLocators.DELETE_PROJECT_BTN)
        delete_project_btn.click()
        wait = WebDriverWait(self.browser, 3)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.item.toolbar-item.btn-wide.primary"))).click()

    def should_update_project_not_in_a_projects_list(self):
        """Check updated project is not in a projects list"""
        assert self.is_element_present(*ProjectPageLocators.NAME_OF_UPDATED_PROJECT)
        time.sleep(3)
        assert self.is_element_not_present(*ProjectPageLocators.NAME_OF_UPDATED_PROJECT), "Project is still displayed"






















