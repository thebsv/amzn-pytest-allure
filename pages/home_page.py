from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)
        self.sign_in_id = "nav-link-accountList"
        self.search_box = "twotabsearchtextbox"
        self.search_id = "nav-search-submit-button"
        self.logout_box = "nav-link-accountList"
        self.logout_button = "https://www.amazon.com/gp/flex/sign-out.html"

    def click_signin(self):
        self.hover_over_element(self.driver.find_element(By.ID, self.sign_in_id))
        self.wait_for_element((By.ID, "nav-flyout-ya-signin"))
        self.driver.find_element(By.ID, "nav-flyout-ya-signin").click()

    def search_for(self, item):
        self.driver.find_element(By.ID, self.search_box).send_keys(item)
        self._click_search()

    def _click_search(self):
        self.driver.find_element(By.ID, self.search_id).click()

    def click_welcome(self):
        self.driver.find_element(By.ID, self.welcome_link_id).click()

    def click_logout(self):
        self.driver.get("https://www.amazon.com/gp/flex/sign-out.html")