import time
from datetime import datetime, date, timedelta

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from Sanplex_project.pages.project_page import ProjectPage


def test_create_project():

    """test file"""
    page = ProjectPage()
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)

    driver.get("https://mentorpiece.sanplex.com/")
    USER = "MTI_group3"
    PASSWORD = "HqHdMaHf6ZL737W"
    PROJECT_NAME = "AutoProject"



    username = driver.find_element(By.CSS_SELECTOR, "input#account")
    username.send_keys(USER)
    # time.sleep(1)

    pswrd = driver.find_element(By.CSS_SELECTOR, "input#password")
    pswrd.send_keys(PASSWORD)
    # time.sleep(1)

    btn = driver.find_element(By.CSS_SELECTOR, "button#submit")
    btn.click()
    time.sleep(5)

    assert "project-browse" in driver.current_url, "another page is displayed"

    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe#appIframe-project"))
    create_project_btn = driver.find_element(By.CLASS_NAME, "create-project-btn")
    create_project_btn.click()
    time.sleep(3)
    project_name_field = driver.find_element(By.CSS_SELECTOR, "textarea.is-required")
    project_name_field.send_keys(PROJECT_NAME)
    time.sleep(1)
    description_frame = driver.find_element(By.CLASS_NAME, "show-desc")
    description_frame.click()
    time.sleep(1)
    ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR, "zen-editor")).click().send_keys(
        "test_description").perform()
    # time.sleep(3)
    # radio_btn_0 = driver.find_element(By.CSS_SELECTOR, "[for = multiple_0]")
    # radio_btn_0.click()
    # time.sleep(3)
    # radio_btn_1 = driver.find_element(By.CSS_SELECTOR, "[for = multiple1]")
    # radio_btn_1.click()

    time.sleep(1)

    date_from = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[4]/div/div/div[1]/div/input[1]")
    date_from.click()
    time.sleep(1)

    date_date_from = driver.find_element(By.XPATH,"//button[text()='8']")
    date_date_from.click()

    time.sleep(1)

    date_to = driver.find_element(By.XPATH,
                                    "/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[4]/div/div/div[2]/div/input[1]")
    date_to.click()
    time.sleep(1)
    date_date_to = driver.find_element(By.XPATH,"//button[text()='18']")
    date_date_to.click()
    time.sleep(1)

    # field = driver.find_element(By.CSS_SELECTOR, "div.modal-content")
    # field.click()
    time.sleep(1)
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button.submit-btn.btn")
    time.sleep(1)
    submit_btn.click()
    time.sleep(1)

    tab_all = driver.find_element(By.CSS_SELECTOR, "li.item")
    tab_all.click()

    name_project = driver.find_elements(By.CSS_SELECTOR, 'div.dtable-cell-content')
    lst = []
    for element in name_project:
        lst.append(element.text)

    print(lst)


    assert PROJECT_NAME in lst, "Project isn't displayed"

    driver.quit()





