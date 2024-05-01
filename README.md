Sanplex_project is Automation QA project<br>

It contains:
1. conftest.py - fixtures and driver initialization
2. pages (directory) contains: <br>
    2.1 locators.py - contains locators<br>
    2.2 base_page.py - contains base class (parent)<br>
    2.3 dashboard_page.py - contains sidebar class and corresponding functions<br>
    2.4 project_page.py - contains project class and corresponding functions<br>
    2.5 story_page.py - contains user story class and corresponding functions<br>
    2.6 tasks_page.py - contains tasks class and corresponding functions<br>
3. test_crud_project.py - test suit for creating, editing and deleting a project
4. tests_crud_story.py - test suit for creating, editing and deleting user story
5. tests_crud_task.py - test suit for creating, editing and deleting task
----------------------------------------------------------------
test_crud_project.py
Tests for CRUD the project are launched by running the class TestCRUDProject
or sequential launch of tests:
- test_create_project
- test_edit_project
- test_delete_project
----------------------------------------------------------------
test_crud_story.py
Tests for CRUD the user story are launched by running the class TestCRUDStory
or sequential launch of tests:
- test_create_story
- test_edit_story
- test_delete_story
------------------------------------------------------------------
test_crud_task.py
Tests for CRUD the task are launched by running the class TestCRUDStory
or sequential launch of tests:
-test_create_task
-------------------------------------------------------------------
markers coming soon...