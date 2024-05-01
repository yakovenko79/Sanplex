import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.locators import ProjectPageLocators, StoryPageLocators

STORY_NAME = "Autostory"


class StoryPage(BasePage):

    def create_new_story(self):
        """Filling create new story form"""
        self.browser.switch_to.frame(self.browser.find_element(*ProjectPageLocators.PROJECT_PAGE_FRAME))
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located((By.XPATH, "//header//span[text("
                                                                                          ")='Stories']"))).click()
        add_story_btn = self.browser.find_element(*StoryPageLocators.ADD_STORY_BTN)
        add_story_btn.click()

        story_name_field = self.browser.find_element(*StoryPageLocators.STORY_NAME)
        story_name_field.send_keys(STORY_NAME)
        description_frame = self.browser.find_element(*ProjectPageLocators.DESCRIPTION)
        description_frame.click()
        time.sleep(3)
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(*ProjectPageLocators.ZEN_EDITOR)).click().send_keys(
            "test_story_description").perform()
        acceptance_criteria_row = self.browser.find_element(*StoryPageLocators.ACCEPTANCE_CRITERIA_ROW)
        acceptance_criteria_row.click()
        acceptance_criteria_row.click()
        time.sleep(3)
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(*StoryPageLocators.ACCEPTANCE_CRITERIA_FIELD)).click().send_keys(
            "Create a new autostory").perform()
        assignee = self.browser.find_element(*StoryPageLocators.ASSIGNEE_STORY)
        assignee.click()
        assign_person = self.browser.find_element(*StoryPageLocators.ASSIGN_PERSON)
        assign_person.click()
        priority_row = self.browser.find_element(*StoryPageLocators.PRIORITY_STORY_ROW)
        priority_row.click()
        priority_list_low = self.browser.find_element(*StoryPageLocators.PRIORITY_LIST_LOW)
        priority_list_low.click()
        estimation_story = self.browser.find_element(*StoryPageLocators.ESTIMATION_STORY)
        estimation_story.send_keys("8")
        show_add_fields_btn = self.browser.find_element(*StoryPageLocators.SHOW_ADD_FIELDS)
        show_add_fields_btn.click()
        time.sleep(1)
        category_box = self.browser.find_element(*StoryPageLocators.CATEGORY_BOX)
        category_box.click()
        category_story = self.browser.find_element(*StoryPageLocators.CATEGORY_STORY)
        category_story.click()
        press_submit_btn = self.browser.find_element(*StoryPageLocators.SUBMIT_BTN)
        press_submit_btn.click()

    def should_created_story_in_stories_list(self):
        assert self.is_element_present(
            *StoryPageLocators.STORY_IN_THE_STORIES_LIST), "Story isn't created in the stories list"

    def dropdown_story_box(self):
        """Pressing the 3 dots dropdown project box button"""
        box = self.browser.find_element(*StoryPageLocators.STORY_LIST_THREE_DOTS_BTN)
        box.click()
        edit_btn = self.browser.find_element(*StoryPageLocators.EDIT_BTN_IN_DROPDOWN_LIST)
        edit_btn.click()

    def edit_story(self):
        time.sleep(2)
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(*StoryPageLocators.EDIT_PRIORITY_DD)).click().click().perform()
        urgent_priority_btn = self.browser.find_element(*StoryPageLocators.URGENT_PRIORITY_BTN)
        urgent_priority_btn.click()
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(*StoryPageLocators.ESTIMATION_STORY)).click().send_keys(
            Keys.BACKSPACE).send_keys("13").send_keys(Keys.TAB).perform()
        phase_story_list = self.browser.find_element(*StoryPageLocators.PHASE_STORY_LIST)
        phase_story_list.click()
        phase_story_devlop_btn = self.browser.find_element(*StoryPageLocators.DEVELOP_PHASE_BTN)
        phase_story_devlop_btn.click()
        category_edit_list = self.browser.find_element(*StoryPageLocators.CATEGORY_EDIT_LIST)
        category_edit_list.click()
        category_edit_interface_btn = self.browser.find_element(*StoryPageLocators.CATEGORY_INTERFACE_EDIT_BTN)
        category_edit_interface_btn.click()
        save_edit_btn = self.browser.find_element(*StoryPageLocators.SAVE_EDIT_BTN)
        save_edit_btn.click()

    def is_the_story_edited(self):
        """Check story is edited"""
        edited_story = self.browser.find_element(*StoryPageLocators.EDITED_STORY)
        edited_story.click()
        time.sleep(2)
        story_card_title = self.browser.find_element(*StoryPageLocators.STORY_CARD_TITLE)
        assert story_card_title.text == "Autostory", "This is another user story"
        story_card_category = self.browser.find_element(*StoryPageLocators.STORY_CARD_CATEGORY)
        assert story_card_category.text == "Interface", "Wrong category"
        story_card_priority = self.browser.find_element(*StoryPageLocators.STORY_CARD_PRIORITY)
        assert story_card_priority.text == "Urgent", "Wrong priority"
        story_card_estimation = self.browser.find_element(*StoryPageLocators.STORY_CARD_ESTIMATION)
        value_estimate = story_card_estimation.text
        list_est = value_estimate.split()
        number_est = list_est[0]
        assert number_est == "13", "Wrong estimation points"

    def delete_story(self):
        """Delete the story"""
        edited_story = self.browser.find_element(*StoryPageLocators.EDITED_STORY)
        edited_story.click()
        time.sleep(2)
        delete_btn = self.browser.find_element(*StoryPageLocators.DELETE_STORY_BTN)
        delete_btn.click()
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//button//span[text()='Confirm']"))).click()

    def is_the_story_deleted(self):
        time.sleep(2)
        assert self.is_element_not_present(*StoryPageLocators.EDITED_STORY), "Story wasn't deleted"

    def should_created_story_in_stories_list_for_edit(self):
        self.browser.switch_to.frame(self.browser.find_element(*ProjectPageLocators.PROJECT_PAGE_FRAME))
        assert self.is_element_present(
            *StoryPageLocators.STORY_IN_THE_STORIES_LIST), "Story isn't created in the stories list"

