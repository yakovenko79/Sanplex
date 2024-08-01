import pytest

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.dashboard_page import SideBar
from Sanplex_project.pages.project_page import ProjectPage
from Sanplex_project.pages.tasks_page import TasksPage

USER = ""
PASSWORD = ""
LINK = "http://{domain}.sanplex.com"


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
        task = TasksPage(browser, browser.current_url)
        task.should_this_tasks_page()
        task.create_new_task()
        task.should_created_task_in_tasks_list()

    def test_edit_task(self, browser):
        """Test editing created in a previous step task"""
        task = TasksPage(browser, browser.current_url)
        task.should_task_in_tasks_list(False)
        task.edit_task()
        task.is_the_task_edited()

    def test_delete_task(self, browser):
        """Test deleting created task"""
        task = TasksPage(browser, browser.current_url)
        task.should_task_in_tasks_list(True)
        task.delete_task()
        task.is_task_deleted()
