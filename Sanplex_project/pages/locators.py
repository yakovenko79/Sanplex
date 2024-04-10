from selenium.webdriver.common.by import By


class LoginLocators():
    USERNAME = (By.CSS_SELECTOR, "input#account")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    BUTTON = (By.CSS_SELECTOR, "button#submit")


class ProjectPageLocators():
    PROJECT_PAGE_FRAME = (By.CSS_SELECTOR, "iframe#appIframe-project")
    CREATE_PROJECT_BTN = (By.CLASS_NAME, "create-project-btn")
    PROJECT_NAME = (By.CSS_SELECTOR, "textarea.is-required")
    DATE_FROM = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[4]/div/div/div[1]/div/input[1]")
    DATE_DATE_FROM = (By.XPATH, "//button[text()='8']")
    DATE_TO = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[4]/div/div/div[2]/div/input[1]")
    DATE_DATE_TO = (By.XPATH, "//button[text()='18']")
    RADIOBUTTON_TURN_OFF = (By.CSS_SELECTOR, "[for = multiple_0]")
    RADIOBUTTON_TURN_ON = (By.CSS_SELECTOR, "[for = multiple1]")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button.submit-btn.btn")
    SWITCH_TAB_ALL = (By.CSS_SELECTOR, "li.item")
    PROJECTS_LIST = (By.CSS_SELECTOR, '.is-last-row')


