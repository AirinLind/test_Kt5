from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from .BasePage import BasePage

class OpenCartMainPage(BasePage):
    URL = "https://demo.opencart.com/"

    def search_product_and_check_visible(self, name):
        self.driver.get(self.URL)
        search_box = self.element((By.NAME, 'search'))
        self._input(search_box, name)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        return name in self.driver.page_source
