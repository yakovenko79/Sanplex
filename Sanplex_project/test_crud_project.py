import pytest

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.project_page import ProjectPage

USER = ""
PASSWORD = ""
LINK = "http://{domain}.sanplex.com"


class TestCRUDProject:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = BasePage(browser, LINK)
        self.page.open()
        self.page.login(USER, PASSWORD)

    def test_create_project(self, browser):
        """Create a new project"""
        project_page = ProjectPage(browser, browser.current_url)
        project_page.should_this_project_page()
        project_page.create_new_project()
        project_page.switch_tab_all()
        project_page.should_project_in_a_projects_list()

    def test_edit_project(self, browser):
        """Edit the project"""
        project_page = ProjectPage(browser, browser.current_url)
        project_page.should_this_project_page()
        project_page.switch_tab_all_edit()
        project_page.dropdown_project_box()
        project_page.edit_project()
        project_page.should_update_project_in_a_projects_list()

    def test_delete_project(self, browser):
        """Delete the project"""
        project_page = ProjectPage(browser, browser.current_url)
        project_page.should_this_project_page()
        project_page.switch_tab_all_edit()
        project_page.should_update_project_in_a_projects_list()
        project_page.dropdown_project_box()
        project_page.delete_project()
        project_page.should_update_project_not_in_a_projects_list()
