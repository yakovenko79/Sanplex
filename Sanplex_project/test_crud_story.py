import time

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.project_page import ProjectPage
from Sanplex_project.pages.dashboard_page import SideBar
from Sanplex_project.pages.story_page import StoryPage

USER = "MTI_group3"
PASSWORD = "HqHdMaHf6ZL737W"
LINK = "http://mentorpiece.sanplex.com"
PROJECT = "Next weird project 1"


class TestCRUDStory:

    def test_create_story(self, browser):
        page = BasePage(browser, LINK)
        page.open()
        page.login(USER, PASSWORD)
        project_page = ProjectPage(browser, browser.current_url)
        project_page.should_this_project_page()
        sidebar = SideBar(browser, browser.current_url)
        sidebar.go_to_projects_list()
        sidebar.go_to_project()
        sidebar.should_title_project_correct()
        sidebar.go_to_user_stories_list_from_sidebar()
        story = StoryPage(browser, browser.current_url)
        story.create_new_story()
        story.should_created_story_in_stories_list()

    def test_edit_story(self, browser):
        page = BasePage(browser, LINK)
        page.open()
        page.login(USER, PASSWORD)
        project_page = ProjectPage(browser, browser.current_url)
        project_page.should_this_project_page()
        sidebar = SideBar(browser, browser.current_url)
        sidebar.go_to_projects_list()
        sidebar.go_to_project()
        sidebar.should_title_project_correct()
        sidebar.go_to_user_stories_list_from_sidebar()
        story = StoryPage(browser, browser.current_url)
        story.should_created_story_in_stories_list_for_edit()
        story.dropdown_story_box()
        story.edit_story()
        story.is_the_story_edited()

    def test_delete_story(self, browser):
        page = BasePage(browser, LINK)
        page.open()
        page.login(USER, PASSWORD)
        project_page = ProjectPage(browser, browser.current_url)
        project_page.should_this_project_page()
        sidebar = SideBar(browser, browser.current_url)
        sidebar.go_to_projects_list()
        sidebar.go_to_project()
        sidebar.should_title_project_correct()
        sidebar.go_to_user_stories_list_from_sidebar()
        story = StoryPage(browser, browser.current_url)
        story.should_created_story_in_stories_list_for_edit()
        story.delete_story()
        story.is_the_story_deleted()












