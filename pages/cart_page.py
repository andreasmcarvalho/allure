from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def remover_item(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    def item_esta_no_carrinho(self):
        return "Sauce Labs Backpack" in self.driver.page_source
