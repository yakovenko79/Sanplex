import pytest

from Sanplex_project.pages.base_page import BasePage
from Sanplex_project.pages.project_page import ProjectPage
from Sanplex_project.pages.dashboard_page import SideBar
from Sanplex_project.pages.story_page import StoryPage

USER = ""
PASSWORD = ""
LINK = "http://{domain}.sanplex.com"
PROJECT = "Next weird project 1"


class TestCRUDStory:
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
        self.sidebar.go_to_user_stories_list_from_sidebar()

    def test_create_story(self, browser):
        """Test creating a new story"""
        story = StoryPage(browser, browser.current_url)
        story.create_new_story()
        story.should_created_story_in_stories_list()

    def test_edit_story(self, browser):
        """Test editing created in a previous step story"""
        story = StoryPage(browser, browser.current_url)
        story.should_created_story_in_stories_list_for_edit()
        story.dropdown_story_box()
        story.edit_story()
        story.is_the_story_edited()

    def test_delete_story(self, browser):
        """Test deleting edited in a previous step story"""
        story = StoryPage(browser, browser.current_url)
        story.should_created_story_in_stories_list_for_edit()
        story.delete_story()
        story.is_the_story_deleted()












