import pytest

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.bugs_page import BugsPage
from Sanplex_project.pages.dashboard_page import SideBar
from Sanplex_project.pages.project_page import ProjectPage

USER = "MTI_group3"
PASSWORD = ""
LINK = "http://mentorpiece.sanplex.com"


class TestCRUDBugs:
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
        self.sidebar.go_to_bugs_page()
        self.bugs_page = BugsPage(browser, browser.current_url)
        self.bugs_page.is_this_bug_page()

    def test_create_bug(self, browser):
        """Test create bug"""
        bugs_page = BugsPage(browser, browser.current_url)
        bugs_page.create_new_bug()
        bugs_page.is_bug_present_in_the_bugs_list()

    def test_edit_bug(self, browser):
        """Test edit bug"""
        bugs_page = BugsPage(browser, browser.current_url)
        bugs_page.edit_bug()
        bugs_page.is_bug_edited()

    def test_delete_bug(self, browser):
        """Deleting edited bug"""
        bugs_page = BugsPage(browser, browser.current_url)
        bugs_page.delete_bug()
        bugs_page.is_bug_deleted()
