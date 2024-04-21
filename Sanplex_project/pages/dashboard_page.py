from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.locators import SideBarLocators


class SideBar(BasePage):

    def go_to_work_dropdown_menu(self):
        work_btn = self.browser.find_element(*SideBarLocators.WORK_BTN)
        work_btn.click()
