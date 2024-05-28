import time

from selenium.webdriver import ActionChains

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.locators import TaskPageLocators, ProjectPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TASK_NAME = "Auto Task"


class TasksPage(BasePage):

    def should_this_tasks_page(self):
        """Returns True if the tasks page should be"""
        assert self.is_element_present(*TaskPageLocators.TASK_LIST_FRAME), "another page is displayed"

    def create_new_task(self):
        """Creating new task with valid data"""
     #   self.browser.switch_to.frame(self.browser.find_element(*HeaderLocators.MY_PAGE_FRAME))
     #   quick_add_btn = self.browser.find_element(*HeaderLocators.QUICK_ADD_BTN)
     #   quick_add_btn.click()
     #   time.sleep(2)
     #   add_task_btn = self.browser.find_element(*HeaderLocators.ADD_TASK_BTN)
     #   add_task_btn.click()
        self.browser.switch_to.frame(self.browser.find_element(*ProjectPageLocators.PROJECT_PAGE_FRAME))
        add_task_btn = self.browser.find_element(*TaskPageLocators.ADD_TASK_BTN)
        add_task_btn.click()
        task_name_field = self.browser.find_element(*TaskPageLocators.TASK_NAME)
        task_name_field.send_keys(TASK_NAME)
        description_frame = self.browser.find_element(*TaskPageLocators.TASK_DESCRIPTION_FRAME)
        description_frame.click()
        zen_editor = self.browser.find_element(*TaskPageLocators.ZEN_EDITOR)
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(zen_editor))
        ActionChains(self.browser).move_to_element(zen_editor).click().send_keys("autotest_task_description").perform()
        task_type_list_btn = self.browser.find_element(*TaskPageLocators.TASK_TYPE_SELECT)
        task_type_list_btn.click()
        task_type_develop = self.browser.find_element(*TaskPageLocators.TASK_TYPE_SELECT_DEV)
        task_type_develop.click()
        press_submit_btn = self.browser.find_element(*TaskPageLocators.SUBMIT_BTN)
        press_submit_btn.click()

    def should_created_task_in_tasks_list(self):
        """Check that the story is in the stories list"""
        assert self.is_element_present(
            *TaskPageLocators.TASK_IN_THE_TASKS_LIST), "Task isn't created in the tasks list"
