
from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.bugs_page import BugsPage
from Sanplex_project.pages.dashboard_page import SideBar
from Sanplex_project.pages.project_page import ProjectPage

USER = "MTI_group3"
PASSWORD = "HqHdMaHf6ZL737W"
LINK = "http://mentorpiece.sanplex.com"


class TestCRUDBugs:

    def test_create_bug(self, browser):
        page = BasePage(browser, LINK)
        page.open()
        page.login(USER, PASSWORD)
        project_page = ProjectPage(browser, browser.current_url)
        project_page.should_this_project_page()
        sidebar = SideBar(browser, browser.current_url)
        sidebar.go_to_projects_list()
        sidebar.go_to_project()
        sidebar.should_title_project_correct()
        sidebar.go_to_bugs_page()
        bugs_page = BugsPage(browser, browser.current_url)
        bugs_page.is_this_bug_page()
        bugs_page.create_new_bug()
        bugs_page.is_bug_present_in_the_bugs_list()



    def test_edit_bug(self, browser):
        page = BasePage(browser, LINK)
        page.open()
        page.login(USER, PASSWORD)
        project_page = ProjectPage(browser, browser.current_url)
        project_page.should_this_project_page()
        sidebar = SideBar(browser, browser.current_url)

