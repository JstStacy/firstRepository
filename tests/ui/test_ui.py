import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.ui 
def test_check_incorrect_username():
    # Create an object to manage the browser
    driver = webdriver.Chrome(
        service = Service('/Users/stacy/firstRepository/chromedriver-mac-arm64/chromedriver')
    )

    # Open the page https://github.com/login
    driver.get('https://github.com/login')

    # Finding the field, we will enter wrong username or email
    login_elem = driver.find_element(By.ID, 'login_field')

    # Enter wrong username or email
    login_elem.send_keys('anastasiiataran@somemail.com')
    
    # Finding the field, we will enter wrong password
    pass_elem = driver.find_element(By.ID, 'password')

    # Enter the wrong password
    pass_elem.send_keys('wrong password')
    
    # Finding 'Sign In' button
    btn_elem = driver.find_element(By.NAME, 'commit')

    # Emulate a click with the left mouse button
    btn_elem.click()
    
    # Check that page name meets expectations
    assert driver.title == 'Sign in to GitHub · GitHub'

    # Close the browser
    driver.close()

    