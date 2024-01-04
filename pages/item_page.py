from selenium.webdriver.common.by import By


class ItemPage:
    def __init__(self, driver):
        self.driver = driver
        self.price_id = "apex_desktop"

    def get_item_price(self) -> str:
        return self.driver.find_element(By.ID, self.price_id).text
