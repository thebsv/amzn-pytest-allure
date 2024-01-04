from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def hover_over_element(self, locator):
        hover = ActionChains(self.driver).move_to_element(locator)
        hover.perform()

    def wait_for_element(self, *locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(*locator))
