from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging
from .BasePage import BasePage

class OpenCartAdminPage(BasePage):
    URL = "https://demo.opencart.com/admin"

    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CLOSE_MODAL = (By.CSS_SELECTOR, ".btn-close")

    def login(self, username, password):
        logging.info("Логин в админку")
        self.driver.get(self.URL)
        self._input(self.element(self.USERNAME), username)
        self._input(self.element(self.PASSWORD), password)
        self.click(self.element(self.LOGIN_BUTTON))
        time.sleep(1)
        try:
            self.click(self.element(self.CLOSE_MODAL))
        except:
            logging.info("Модальное окно не появилось")

    def create_category(self, name, meta):
        self.click(self.element((By.ID, 'menu-catalog')))
        self.click(self.element((By.XPATH, "//a[contains(text(),'Categories')]")))
        self.click(self.element((By.CSS_SELECTOR, 'a[data-original-title="Add New"]')))
        self._input(self.element((By.ID, 'input-name1')), name)
        self._input(self.element((By.ID, 'input-meta-title1')), meta)
        self.click(self.element((By.CSS_SELECTOR, 'button[data-original-title="Save"]')))
        time.sleep(2)

    def add_product(self, name, meta, model="Default", category="Devices"):
        self.click(self.element((By.ID, 'menu-catalog')))
        self.click(self.element((By.XPATH, "//a[contains(text(),'Products')]")))
        self.click(self.element((By.CSS_SELECTOR, 'a[data-original-title="Add New"]')))
        self._input(self.element((By.ID, 'input-name1')), name)
        self._input(self.element((By.ID, 'input-meta-title1')), meta)
        self.click(self.element((By.XPATH, "//a[contains(text(),'Data')]")))
        self._input(self.element((By.ID, 'input-model')), model)
        self.click(self.element((By.XPATH, "//a[contains(text(),'Links')]")))
        cat_input = self.element((By.ID, 'input-category'))
        self._input(cat_input, category)
        time.sleep(1)
        cat_input.send_keys(Keys.ENTER)
        self.click(self.element((By.CSS_SELECTOR, 'button[data-original-title="Save"]')))
        time.sleep(2)

    def delete_product(self, name):
        self.click(self.element((By.ID, 'menu-catalog')))
        self.click(self.element((By.XPATH, "//a[contains(text(),'Products')]")))
        search = self.element((By.ID, 'input-name'))
        self._input(search, name)
        self.click(self.element((By.ID, 'button-filter')))
        time.sleep(1)
        try:
            self.click(self.element((By.NAME, 'selected[]')))
            self.click(self.element((By.CSS_SELECTOR, 'button[data-original-title="Delete"]')))
            self.driver.switch_to.alert.accept()
            time.sleep(2)
        except Exception as e:
            logging.warning(f"Не удалось удалить {name}: {e}")
