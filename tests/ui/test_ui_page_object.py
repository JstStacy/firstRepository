from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui 
def test_check_incorrect_username_page_object():
    # Create page object
    sign_in_page = SignInPage()

    # Open https://github.com/login
    sign_in_page.go_to()

    # Try to login to GitHub
    sign_in_page.try_login('page_object@gmail.com', 'wrong password')

    # Check that page name meets expectations
    assert sign_in_page.check_title('Sign in to GitHub · GitHub')

    # Close the browser
    sign_in_page.close()

