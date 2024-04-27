import time

from selenium.webdriver import ActionChains

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.locators import HeaderLocators, TaskPageLocators

TASK_NAME = "Auto Task"


class TasksPage(BasePage):

    def should_this_tasks_page(self):
        """Check 'my-work-task' in URL"""
        assert "my-work-task" in self.browser.current_url, "another page is displayed"

    def create_new_task(self):
        """Creating new task with valid data"""
        self.browser.switch_to.frame(self.browser.find_element(*HeaderLocators.MY_PAGE_FRAME))
        quick_add_btn = self.browser.find_element(*HeaderLocators.QUICK_ADD_BTN)
        quick_add_btn.click()
        time.sleep(2)
        add_task_btn = self.browser.find_element(*HeaderLocators.ADD_TASK_BTN)
        add_task_btn.click()
        # time.sleep(3)
        task_name_field = self.browser.find_element(*TaskPageLocators.TASK_NAME)
        task_name_field.send_keys(TASK_NAME)
        description_frame = self.browser.find_element(*TaskPageLocators.TASK_DESCRIPTION_FRAME)
        time.sleep(1)
        description_frame.click()
        time.sleep(1)
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(*TaskPageLocators.ZEN_EDITOR)).click().send_keys(
            "autotest_task_description").perform()
        task_type_list_btn = self.browser.find_element(*TaskPageLocators.TASK_TYPE_SELECT)
        task_type_list_btn.click()
        task_type_develop = self.browser.find_element(*TaskPageLocators.TASK_TYPE_SELECT_DEV)
        task_type_develop.click()
        time.sleep(2)
