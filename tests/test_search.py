import allure
import pytest
from selenium.webdriver.common.by import By

from pages.searchres_page import SearchResultsPage
from pages.home_page import HomePage
from pages.item_page import ItemPage
from utils import utils as environment


class TestSearch:
    @pytest.mark.parametrize("item", ["nike air dunk low", "adidas duffle bag"])
    def test_search(self, driver, item):
        driver.get(environment.URL)
        home = HomePage(driver)
        home.search_for(item)
        sres = SearchResultsPage(driver)
        assert "RESULTS" == sres.verify_results_page()
        sres.click_first_result()
        test_name = environment.whoami()
        screenshot_name = test_name + "_screenshot1_"
        allure.attach(driver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=allure.attachment_type.PNG)
        driver.back()
        sres.click_second_result()
        screenshot_name = test_name + "_screenshot2_"
        allure.attach(driver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=allure.attachment_type.PNG)

    @pytest.mark.parametrize("item", ["nike air dunk low", "adidas duffle bag"])
    def test_scour_item(self, driver, item):
        driver.get(environment.URL)
        home = HomePage(driver)
        home.search_for(item)
        sres = SearchResultsPage(driver)
        assert "RESULTS" == sres.verify_results_page()
        sres.click_first_result()
        item = ItemPage(driver)
        print("PRICE: ", item.get_item_price())

    # @pytest.mark.parametrize("item", ["iPhone", "macbook pro"])
    @pytest.mark.parametrize("item", ["macbook pro"])
    def test_scour_item_II(self, driver, item):
        driver.get(environment.URL)
        home = HomePage(driver)
        home.search_for(item)
        sres = SearchResultsPage(driver)
        assert "RESULTS" == sres.verify_results_page()
        print("ITEMS: \n")
        for item in sres.print_all_items():
            print(item)

    def test_today_deals(self, driver):
        driver.get(environment.URL)
        home = HomePage(driver)
        home.search_for("iPhone")
        sres = SearchResultsPage(driver)
        assert "RESULTS" == sres.verify_results_page()
        sres.click_todays_deals()
        assert "Today's Deals" == sres.verify_todays_deals()

