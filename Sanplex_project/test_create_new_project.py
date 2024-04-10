import time

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.project_page import ProjectPage

user = "MTI_group3"
password = "HqHdMaHf6ZL737W"
LINK = "http://mentorpiece.sanplex.com"


class TestCRUDProject:

    def test_create_project(self, browser):
        page = BasePage(browser, LINK)
        page.open()
        page.login(user, password)
        project_page = ProjectPage(browser, browser.current_url)
        time.sleep(3)
        project_page.should_this_project_page()
        project_page.create_new_project()
        project_page.switch_tab_all()
        time.sleep(3)
        project_page.should_project_in_a_projects_list()





