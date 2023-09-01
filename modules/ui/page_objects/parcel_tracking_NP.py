from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ParcelTracking(BasePage):
    URL = 'https://track.ukrposhta.ua/tracking_UA.html?barcode='

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(ParcelTracking.URL)

    def try_to_find_parcel(self, tth):
        # Finding the field, we will enter wrong tth
        find_elem = self.driver.find_element(By.ID, 'trackcode')

        # Enter wrong tth
        find_elem.send_keys(tth)

        # Wait for the preloader to disappear
        WebDriverWait(self.driver, 10).until(
        EC.invisibility_of_element_located((By.ID, 'page-preloader'))
    )
    
        # Finding track button
        btn_elem = self.driver.find_element(By.CSS_SELECTOR, 'button[id="trackbutton"]')

        # Emulate a click with the left mouse button
        btn_elem.click()
    
    def check_title(self, expected_title):
        return self.driver.title == expected_title
    