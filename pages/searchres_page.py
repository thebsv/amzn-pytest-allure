from selenium.webdriver.common.by import By


class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.results_xpath = "//*[@id=\"search\"]/div[1]/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/span"
        self.first_res_type1 = "//*[@id=\"search\"]/div[1]/div[1]/div/span[3]/div[2]/div[2]"
        self.second_res_type1 = "//*[@id=\"search\"]/div[1]/div[1]/div/span[3]/div[2]/div[3]"

    def click_first_result(self):
        self.driver.find_element(By.XPATH, self.first_res_type1).click()
        self.driver.implicitly_wait(1)

    def click_second_result(self):
        self.driver.find_element(By.XPATH, self.second_res_type1).click()
        self.driver.implicitly_wait(1)

    def click_first_result_type2(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div").click()
        self.driver.implicitly_wait(1)

    def click_todays_deals(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"nav-xshop\"]/a[1]").click()
        self.driver.implicitly_wait(1)

    def verify_results_page(self) -> str:
        return self.driver.find_element(By.XPATH, self.results_xpath).text

    def verify_todays_deals(self) -> str:
        return self.driver.find_element(By.XPATH, "//*[@id=\"slot-2\"]/div").text
