import time

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.dashboard_page import SideBar
from Sanplex_project.pages.tasks_page import TasksPage

USER = "MTI_group7"
PASSWORD = "HqHdMaHf6ZL737W"
LINK = "https://mentorpiece.sanplex.com/my-index.html"


class TestCRUDTask:

    def test_create_task(self, browser):
        page = BasePage(browser, LINK)
        page.open()
        page.login(USER, PASSWORD)
        side = SideBar(browser, browser.current_url)
     #   time.sleep(3)
        side.go_to_work_dropdown_menu()
     #   time.sleep(3)
        side.go_to_tasks_page()
        time.sleep(3)
        tasks_page = TasksPage(browser, browser.current_url)
        tasks_page.should_this_tasks_page()