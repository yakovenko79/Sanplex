Sanplex_project is Automation QA project<br>

It contains:
1. conftest.py - fixtures and driver initialization
2. pages (directory) contains: <br>
    2.1 locators.py - contains locators<br>
    2.2 base_page.py - contains base class (parent)<br>
    2.3 project_page.py - contains project class and corresponding functions<br>
3. test_crud_project.py - test suit for creating new project and edit new project
4. test_DRAFT.py - draft for experiments
----------------------------------------------------------------
test_crud_project.py
Tests for CRUD the project are launched by running the class TestCRUDProject
or sequential launch of tests:
- test_create_project
- test_edit_project
- test_delete_project
----------------------------------------------------------------
markers coming soon...