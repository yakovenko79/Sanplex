from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.project_page import ProjectPage

USER = "MTI_group3"
PASSWORD = "HqHdMaHf6ZL737W"
LINK = "http://mentorpiece.sanplex.com"


class TestCRUDProject:

    def test_create_project(self, browser):
        page = BasePage(browser, LINK)
        page.open()
        page.login(USER, PASSWORD)
        project_page = ProjectPage(browser, browser.current_url)
        project_page.should_this_project_page()
        project_page.create_new_project()
        project_page.switch_tab_all()
        project_page.should_project_in_a_projects_list()

    def test_edit_project(self, browser):
        page = BasePage(browser, LINK)
        page.open()
        page.login(USER, PASSWORD)
        project_page = ProjectPage(browser, browser.current_url)
        project_page.should_this_project_page()
        project_page.switch_tab_all_edit()
        project_page.dropdown_project_box()
        project_page.edit_project()
        project_page.should_update_project_in_a_projects_list()
