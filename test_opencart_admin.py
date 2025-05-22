import allure
from page_objects.OpenCartAdminPage import OpenCartAdminPage
from page_objects.OpenCartMainPage import OpenCartMainPage

@allure.feature("OpenCart Full Flow")
class TestOpenCart:

    @allure.story("Полный сценарий: категория, товары, удаление, проверка")
    def test_full_flow(self, driver):
        admin = OpenCartAdminPage(driver)
        main = OpenCartMainPage(driver)

        admin.login("demo", "demo")
        admin.create_category("Devices", "Devices Meta")

        products = [
            ("Mouse 1", "Wireless Mouse 1"),
            ("Mouse 2", "Wireless Mouse 2"),
            ("Keyboard 1", "Mechanical Keyboard 1"),
            ("Keyboard 2", "Mechanical Keyboard 2")
        ]

        for name, meta in products:
            admin.add_product(name, meta, model=f"Model_{name}", category="Devices")

        for name, _ in products:
            assert main.search_product_and_check_visible(name), f"{name} not found"

        for name in ["Mouse 1", "Keyboard 1"]:
            admin.delete_product(name)

        for name in ["Mouse 2", "Keyboard 2"]:
            assert main.search_product_and_check_visible(name), f"{name} должен быть, но не найден"

        for name in ["Mouse 1", "Keyboard 1"]:
            assert not main.search_product_and_check_visible(name), f"{name} не должен быть, но найден"
