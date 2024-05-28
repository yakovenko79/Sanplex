import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.dashboard_page import SideBar
from Sanplex_project.pages.project_page import ProjectPage
from Sanplex_project.pages.tasks_page import TasksPage

USER = "MTI_group3"
PASSWORD = "HqHdMaHf6ZL737W"
LINK = "http://mentorpiece.sanplex.com"


class TestCRUDTask:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = BasePage(browser, LINK)
        self.page.open()
        self.page.login(USER, PASSWORD)
        self.project_page = ProjectPage(browser, browser.current_url)
        self.project_page.should_this_project_page()
        self.sidebar = SideBar(browser, browser.current_url)
        self.sidebar.go_to_projects_list()
        self.sidebar.go_to_project()
        self.sidebar.should_title_project_correct()
        self.sidebar.go_to_tasks_page_from_sidebar()

    def test_create_task(self, browser):
        """Check creating a task"""
        tasks_page = TasksPage(browser, browser.current_url)
     #  tasks_page.should_this_tasks_page()
        tasks_page.create_new_task()
