import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(
    filename="logs/test_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def element(self, locator):
        logging.info(f"🔍 Ожидание элемента: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, element):
        logging.info(f"🖱️ Клик по элементу: {element}")
        element.click()

    def _input(self, element, value):
        logging.info(f"⌨️ Ввод '{value}' в поле {element}")
        element.clear()
        element.send_keys(value)
