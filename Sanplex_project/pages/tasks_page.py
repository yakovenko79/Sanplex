import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.locators import TaskPageLocators, ProjectPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TASK_NAME = "Auto Task"


class TasksPage(BasePage):

    def should_this_tasks_page(self):
        """Check that it is Tasks page"""
        time.sleep(2)
        assert "project-task" in self.browser.current_url, "another page is displayed"

    def create_new_task(self):
        """Creating new task with valid data"""
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
            *TaskPageLocators.CREATED_TASK), "Task isn't created in the tasks list"

    def should_task_in_tasks_list(self, edited=False):
        """Check that created task for edit is in the tasks list"""
        self.browser.switch_to.frame(self.browser.find_element(*ProjectPageLocators.PROJECT_PAGE_FRAME))
        per_page_btn = self.browser.find_element(*TaskPageLocators.PER_PAGE_BTN)
        per_page_btn.click()
        per_page_50_btn = self.browser.find_element(*TaskPageLocators.PER_PAGE_50_BTN)
        per_page_50_btn.click()
        if self.is_element_not_present(*TaskPageLocators.TASK_TITLE_SORT_ASC):
            title_sort_btn = self.browser.find_element(*TaskPageLocators.TASK_TITLE_SORT_BTN)
            title_sort_btn.click()
            time.sleep(2)
        if edited:
            assert self.is_element_present(
                *TaskPageLocators.EDITED_TASK), "Edited task isn't in the tasks list"
        else:
            assert self.is_element_present(
                *TaskPageLocators.CREATED_TASK), "Created task isn't in the tasks list"

    def edit_task(self):
        """Edit task"""
        test_task = self.browser.find_element(*TaskPageLocators.CREATED_TASK)
        test_task.click()
        time.sleep(3)
        edit_btn = self.browser.find_element(*TaskPageLocators.EDIT_TASK_BTN)
        edit_btn.click()
        task_name = self.browser.find_element(*TaskPageLocators.TASK_NAME_FIELD)
        task_name.send_keys(" edited")
        task_estimation = self.browser.find_element(*TaskPageLocators.TASK_ESTIMATION)
        task_estimation.send_keys("5")
        save_edit_btn = self.browser.find_element(*TaskPageLocators.SAVE_EDIT_BTN)
        save_edit_btn.click()

    def is_the_task_edited(self):
        """Check that the edited task is in the tasks list"""
        time.sleep(2)
        assert self.is_element_present(*TaskPageLocators.EDITED_TASK), "Edited task isn't in the tasks list"

    def delete_task(self):
        deleting_task = self.browser.find_element(*TaskPageLocators.EDITED_TASK)
        deleting_task.click()
        time.sleep(2)
        delete_task_btn = self.browser.find_element(*TaskPageLocators.DELETE_TASK_BTN)
        delete_task_btn.click()
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.item.toolbar-item.btn-wide.primary"))).click()
        time.sleep(3)

    def is_task_deleted(self):
        """Check if the task has been deleted"""
        time.sleep(2)
#        self.browser.switch_to.frame(self.browser.find_element(*ProjectPageLocators.PROJECT_PAGE_FRAME))
        assert self.is_element_not_present(*TaskPageLocators.EDITED_TASK), "Task wasn't deleted"


