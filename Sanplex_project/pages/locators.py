from selenium.webdriver.common.by import By

# from Sanplex_project.test_crud_story import PROJECT
PROJECT = 'New weird project 1'


class LoginLocators:
    """Locators for login"""
    USERNAME = (By.CSS_SELECTOR, "input#account")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    BUTTON = (By.CSS_SELECTOR, "button#submit")


class ProjectPageLocators:
    """Locators for Projects page and Add Project page """
    ADD_STORY_BTN = (By.XPATH, "//*[@id='actionBar']/a")
    MODAL_DIALOG_WINDOW = (By.CSS_SELECTOR, "div.modal-dialog")
    FRAME_DELETE_PROJECT = (By.CSS_SELECTOR, "div.modal")
    CONFIRM_BTN = (By.CSS_SELECTOR, "button.btn.item.toolbar-item.btn-wide.primary")
    DISMISS_BTN = (By.CSS_SELECTOR, "button.btn.item.toolbar-item.btn-wide.btn-default")
    CONFIRM_TEXT = (By.CSS_SELECTOR, 'div.modal-body>div:nth-child(2)')
    DELETE_PROJECT_BTN = (By.XPATH, "//div[text()='Delete']")
    PROJECT_PAGE_FRAME = (By.CSS_SELECTOR, "iframe#appIframe-project")
    CREATE_PROJECT_BTN = (By.CLASS_NAME, "create-project-btn")
    PROJECT_NAME = (By.CSS_SELECTOR, "textarea.is-required")
    DESCRIPTION = (By.CLASS_NAME, "show-desc")
    DATE_FROM = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[4]/div/div/div[1]/div/input[1]")
    DATE_DATE_FROM = (By.XPATH, "//button[text()='8']")
    DATE_DATE_FROM_UPDATE = (By.XPATH, "//button[text()='10']")
    DATE_TO = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[4]/div/div/div[2]/div/input[1]")
    DATE_DATE_TO = (By.XPATH, "//button[text()='18']")
    DATE_DATE_TO_UPDATE = (By.XPATH, "//button[text()='20']")
    RADIOBUTTON_TURN_OFF = (By.CSS_SELECTOR, "[for = multiple_0]")
    RADIOBUTTON_TURN_ON = (By.CSS_SELECTOR, "[for = multiple1]")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button.submit-btn.btn")
    SWITCH_TAB_ALL = (By.CSS_SELECTOR, "li.nav-item.item:nth-child(1)")
    SWITCH_TAB_ALL_EDIT = (By.XPATH, "//span[text()='ALL']")
    PROJECTS_LIST = (By.CSS_SELECTOR, '.is-last-row')
    ZEN_EDITOR = (By.CSS_SELECTOR, "zen-editor")
    NAME_OF_CREATED_PROJECT = (By.XPATH, "//a[text()='AutoProject']")
    NAME_OF_UPDATED_PROJECT = (By.XPATH, "//a[text()='AutoProject_updated']")
    DROPDOWN_PROJECT_BOX = (By.XPATH, "//*[@id='table-project-browse']/div[2]/div[2]/div/div[last()]/div/nav/button")
    EDIT_PROJECT = (By.XPATH, "//div[text()='Edit Project']")
    SHOW_ADDIT_FIELDS = (By.CSS_SELECTOR, "button.btn.ghost.toggle-top-btn")
    PROJECT_MANAGER_FIELD = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[5]/div/div[4]/div[2]/div")
    PROJECT_MANAGER = (By.CSS_SELECTOR, "div.item-title")
    BUDGET_FIELD = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]/form/div["
                              "5]/div/div[3]/div[2]/div/input")
    ALL_TAB = (By.XPATH, "/html/body/div/div/div[1]/div[1]/menu/li[1]/a")


class SideBarLocators:
    """Locators for sidebar"""
    BUGS_BTN = (By.XPATH, "//button/div/div/span[text()='Bugs']")
    SWITCH_TAB_ALL = (By.CSS_SELECTOR, "li.nav-item.item:nth-child(1)")
    STORY_BTN = (By.XPATH, "//button/div/div/span[text()='Stories']")
    SCOPES_DROPDOWN = (By.XPATH, "//*[@id='sidebarDemo']/div/div[2]/div/div/div[3]/button[2]/div")
    TITLE_PROJECT = (By.CSS_SELECTOR, "div.title:nth-child(2)")
    SPACE_BTN = (By.CSS_SELECTOR, "div.dropdown.spaces")
    WORK_BTN = (By.CSS_SELECTOR, 'button.sidebar-menu-header[data-type="work"]')
    TASKS_BTN = (By.CSS_SELECTOR, 'button.sidebar-menu-header[data-type="task"]')


class HeaderLocators:
    """Common locators for header"""
    QUICK_ADD_BTN = (By.CSS_SELECTOR, 'button#quickAddMenu-toggle')
    ADD_TASK_BTN = (By.CSS_SELECTOR, "menu.dropdown-menu.scrollbar-hover li:nth-child(3)")
    ADD_STORY_BTN = (By.CSS_SELECTOR, 'menu.dropdown-menu.scrollbar-hover li:nth-child(2)')
    ADD_BUG_BTN = (By.CSS_SELECTOR, 'menu.dropdown-menu.scrollbar-hover li:nth-child(1)')
    MY_PAGE_FRAME = (By.CSS_SELECTOR, "iframe#appIframe-my")


class TaskPageLocators:
    """Locators for Tasks page and Add task page"""
    TASK_NAME = (By.CSS_SELECTOR, "textarea.is-required")
    TASK_TYPE_SELECT = (By.XPATH, '//label[text()="Type"]//following-sibling::div/div[@tabindex="-1"]')
    TASK_DESCRIPTION_FRAME = (By.CLASS_NAME, "show-desc")
    ZEN_EDITOR = (By.CSS_SELECTOR, "zen-editor")
    TASK_TYPE_SELECT_DEV = (By.CSS_SELECTOR, 'li.menu-item.item[z-key="devel"]')


class StoryPageLocators:
    DELETE_STORY_BTN = (By.CSS_SELECTOR, "div.float-toolbar-view>div:last-child>div>a:last-child")
    STORIES_PAGE_HEADER = (By.CSS_SELECTOR, "#heading button span.text")
    STORY_CARD_ESTIMATION = (By.CSS_SELECTOR, "div.h-16>div:nth-child(2)>div:last-child")
    STORY_CARD_PRIORITY = (By.CSS_SELECTOR, "div.h-16 div:nth-child(5)>div:nth-child(2)")
    STORY_CARD_CATEGORY = (By.CSS_SELECTOR, "div.h-16 div:nth-child(4)>div:last-child")
    STORY_CARD_TITLE = (By.CSS_SELECTOR, "div.task-title")
    EDITED_STORY = (By.XPATH, "//a[text()='Autostory']")
    SAVE_EDIT_BTN = (By.XPATH, '//button/span[text()="Save"]')
    CATEGORY_INTERFACE_EDIT_BTN = (By.XPATH, '//div[text()="Interface"]')
    CATEGORY_EDIT_LIST = (By.XPATH, "//span[@title='Feature']")
    DEVELOP_PHASE_BTN = (By.XPATH, "//div[text()='Developed']")
    PHASE_STORY_LIST = (By.XPATH, "//span[text()='Projected']")
    ESTIMATION = (By.NAME, "estimate")
    URGENT_PRIORITY_BTN = (By.XPATH, '//div[text()="Urgent"]')
    EDIT_PRIORITY_DD = (By.XPATH, '//div/span[text()="Low"]')
    EDIT_BTN_IN_DROPDOWN_LIST = (By.XPATH, '//div[text()="Edit"]')
    STORY_IN_THE_STORIES_LIST = (By.XPATH, '//div//a[text()="Autostory"]')
    SUBMIT_BTN = (By.CSS_SELECTOR, "button.submit-btn")
    CATEGORY_BOX = (By.CSS_SELECTOR, "div.custom-fields .field-item:nth-child(3) div.field-control")
    CATEGORY_STORY = (By.CSS_SELECTOR, 'menu.menu.picker-menu-list a')
    SHOW_ADD_FIELDS = (By.XPATH, "//button//span[text()='Show Additional Fields']")
    ESTIMATION_STORY = (By.XPATH, '//input[@name="estimate"]')
    PRIORITY_LIST_LOW = (By.XPATH, "//div/div[text()='Low']")
    PRIORITY_STORY_ROW = (By.XPATH, "//div/span[text()='No Priority']")
    ASSIGN_PERSON = (By.CSS_SELECTOR, "div.item-title")
    ASSIGNEE_STORY = (By.CSS_SELECTOR, "div.form-group-wrapper div > span.picker-select-placeholder")
    ACCEPTANCE_CRITERIA_ROW = (By.XPATH, "//div[@placeholder='Enter Acceptance Criteria']")
    ACCEPTANCE_CRITERIA_FIELD = (By.XPATH, '//zen-editor[@placeholder="Enter Acceptance Criteria"]')
    STORY_NAME = (By.CSS_SELECTOR, "textarea:nth-child(1)")
    ADD_STORY_BTN = (By.XPATH, "//*[@id='actionBar']/a")
    STORY_LIST_THREE_DOTS_BTN = (By.CSS_SELECTOR, 'div > nav')


class BugsPageLocators:
    EXPECTATIONS_TITLE = (By.XPATH, "//div[2]/div[3]/div[1]/span")
    CREATED_BUG = (By.XPATH, '//a[text()="Test bug"]')
    CREATE_BUG_BTN = (By.CSS_SELECTOR, "button.toolbar-item.submit-btn")
    EXPECTATIONS_FIELD = (By.CSS_SELECTOR, "div.accordion-card>:nth-child(3)>:last-child")
    RESULTS_FIELD = (By.XPATH, "div.accordion-card>div:nth-child(2)>div:nth-child(2)")
    STEPS_INPUT_FIELD = (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div[2]/div[2]/p")
    STEPS_FIELD = (By.CSS_SELECTOR, "div.accordion-card>div:nth-child(1)>div:nth-child(2)")
    RESULTS_INPUT_FIELD = (By.CSS_SELECTOR, "div.accordion-card>div:nth-child(2)>div:nth-child(2)")
    TITLE_STEPS_TO_REPRODUCE = (By.XPATH, '//div/span[text()="Steps to Reproduce"]')
    ZEN_EDITOR_STEPS = (By.CSS_SELECTOR, "div.accordion-card>div.form-group:nth-child(1)>div:nth-child(2)>div>zen-editor")
    BUG_NAME_FIELD = (By.XPATH, "//form/div/div/textarea")
    REPORT_BUG_BTN = (By.XPATH, "//a//span[text()='Report Bug']")
    BUGS_TITLE = (By.XPATH, "//button/span[text()='Bugs']")
