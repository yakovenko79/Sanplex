from selenium.webdriver.common.by import By


class LoginLocators():
    """Locators for login"""
    USERNAME = (By.CSS_SELECTOR, "input#account")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    BUTTON = (By.CSS_SELECTOR, "button#submit")


class ProjectPageLocators():
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
    SWITCH_TAB_ALL_EDIT = (By.XPATH, "//span[text()='ALL]")
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
