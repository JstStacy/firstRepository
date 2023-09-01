# firstRepository
Hi there! This is my first project with Python and Pytest.
# General Information
This project consist of API, Database, and UI tests that were a practical part of Automation Testing study.
It is still in progres and will be supplemented with new tests.
# Folder structure from the root directory of the project
```
/chromedriver-mac-arm-64
  /chromedriver-mac-arm-64/chromedriver
  /chromedriver-mac-arm-64/LICENSE.chomedriver
  
/config
  /config/config.py

/modules
  /modules/api
    /modules/api/clients/__init__.py
    /modules/api/clients/github.py

  /modules/common
    /modules/common/__init__.py
    /modules/common/database.py

  /modules/ui
    /modules/ui/page_objects/__init__.py
    /modules/ui/page_objects/base_page.py
    /modules/ui/page_objects/sign_in_page.py
    /modules/ui/page_objects/parcel_tracking_UP.py

/tests
  /tests/api
    /tests/api/test_api.py
    /tests/api/test_fixture.py
    /tests/api/test_github_api.py

  /tests/database
    /tests/database/test_database.py

  /tests/ui
    /tests/ui/test_ui_page_object.py
    /tests/ui/test_ui.py
    /tests/ui/test_ui_parcel_tracking_UP.py

  /tests/test_http.py
    
/become_qa_auto.db

/conftest.py

/pytest.ini
```
# Usage
To run all tests from this repository you need to use the proper directory (/*your_folders*/firstRepository). 

To run all tests use next command in terminal
```
pytest
```
To run API tests use next command in terminal
```
pytest -m api
```
To run DB tests use next command in terminal
```
pytest -m database
```
To run UI tests use next command in terminal
```
pytest -m ui
```



