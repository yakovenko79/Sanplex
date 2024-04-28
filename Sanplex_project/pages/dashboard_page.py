import time

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.locators import SideBarLocators


class SideBar(BasePage):

    def go_to_work_dropdown_menu(self):
        """Calling the dropdown menu by clicking the WORK button on the sidebar"""
        work_btn = self.browser.find_element(*SideBarLocators.WORK_BTN)
        work_btn.click()

    def go_to_tasks_page(self):
        """Going to the page Tasks by clicking the Tasks button on the sidebar"""
        time.sleep(2)
        tasks_btn = self.browser.find_element(*SideBarLocators.TASKS_BTN)
        tasks_btn.click()
        time.sleep(2)

