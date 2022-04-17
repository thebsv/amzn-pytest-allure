from selenium.webdriver.common.by import By


class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.results_xpath = "//*[@id=\"search\"]/div[1]/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/span"
        self.first_res = "//*[@id=\"search\"]/div[1]/div[1]/div/span[3]/div[2]/div[2]"
        self.second_res = "//*[@id=\"search\"]/div[1]/div[1]/div/span[3]/div[2]/div[3]"

    def click_first_result(self):
        self.driver.find_element(By.XPATH, self.first_res).click()
        self.driver.implicitly_wait(1)

    def click_second_result(self):
        self.driver.find_element(By.XPATH, self.second_res).click()
        self.driver.implicitly_wait(1)

    def verify_results_page(self) -> str:
        return self.driver.find_element(By.XPATH, self.results_xpath).text
