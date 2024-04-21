from Sanplex_project.pages.base_page import BasePage


class TasksPage(BasePage):

    def should_this_tasks_page(self):
        """Check 'my-work-task' in URL"""
        assert "my-work-task" in self.browser.current_url, "another page is displayed"
