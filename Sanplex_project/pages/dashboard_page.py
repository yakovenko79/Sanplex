import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.locators import SideBarLocators, ProjectPageLocators
from selenium.webdriver.support import expected_conditions as EC

PROJECT = "Next weird project 1"


class SideBar(BasePage):

    def go_to_work_dropdown_menu(self):
        """Calling the dropdown menu by clicking the WORK button on the sidebar"""
        work_btn = self.browser.find_element(*SideBarLocators.WORK_BTN)
        work_btn.click()

    def go_to_tasks_page(self):
        """Going to the page Tasks by clicking the Tasks button on the sidebar"""
        tasks_btn = self.browser.find_element(*SideBarLocators.TASKS_BTN)
        tasks_btn.click()

    def go_to_projects_list(self):
        """Going to the list of projects by clicking the SPACE button on the sidebar"""
        space = self.browser.find_element(*SideBarLocators.SPACE_BTN)
        space.click()

    def go_to_project(self):
        """Go to the project by clicking the project on the dropdown list of projects"""
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//li//button//div[text()='Next weird project 1']"))).click()

    def should_title_project_correct(self):
        """Check that project in sidebar is displayed correctly"""
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Next weird "
                                                                                          "project 1'] [@title='Next "
                                                                                          "weird project 1']")))
        title = self.browser.find_element(*SideBarLocators.TITLE_PROJECT)
        assert title.text == PROJECT

    def go_to_user_stories_list_from_sidebar(self):
        """Go to the projects user stories list from sidebar"""
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='sidebarDemo']/div/div[2]/div/div/div[3]/button[2]/div"))).click()
        story_btn = self.browser.find_element(*SideBarLocators.STORY_BTN)
        story_btn.click()
        time.sleep(3)

    def switch_tab_all(self):
        self.browser.switch_to.frame(self.browser.find_element(*ProjectPageLocators.PROJECT_PAGE_FRAME))
        tab_all = self.browser.find_element(*SideBarLocators.SWITCH_TAB_ALL)
        tab_all.click()

    def go_to_bugs_page(self):
        """Go to the projects bugs list from sidebar"""
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='sidebarDemo']/div/div[2]/div/div/div[3]/button[2]/div"))).click()
        bugs_btn = self.browser.find_element(*SideBarLocators.BUGS_BTN)
        bugs_btn.click()







