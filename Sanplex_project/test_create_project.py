import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


def test_create_project():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    # time.sleep(1)

    driver.get("https://mentorpiece.sanplex.com/")
    # time.sleep(1)

    user = "MTI_group3"
    password = "HqHdMaHf6ZL737W"
    PROJECT_NAME = "AutoProject"

    username = driver.find_element(By.CSS_SELECTOR, "input#account")
    username.send_keys(user)
    # time.sleep(1)

    pswrd = driver.find_element(By.CSS_SELECTOR, "input#password")
    pswrd.send_keys(password)
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
    time.sleep(5)
    description_frame = driver.find_element(By.CLASS_NAME, "show-desc")
    description_frame.click()
    time.sleep(3)
    ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR, "zen-editor")).click().send_keys("test_description").perform()
    time.sleep(3)
    radio_btn_0 = driver.find_element(By.CSS_SELECTOR, "[for = multiple_0]")
    radio_btn_0.click()
    time.sleep(3)
    radio_btn_1 = driver.find_element(By.CSS_SELECTOR, "[for = multiple1]")
    radio_btn_1.click()
    time.sleep(3)