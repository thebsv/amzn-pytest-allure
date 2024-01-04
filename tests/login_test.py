import allure

from pages.signin_page import LoginPage
from pages.home_page import HomePage
from utils import utils as environment


class TestLogin:
    def test_login(self, driver):
        driver.get(environment.URL)
        home = HomePage(driver)
        home.click_signin()
        test_name = environment.whoami()
        screenshot_name = test_name + "_screenshot_login"
        # save screenshot in allure
        allure.attach(driver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=allure.attachment_type.PNG)
        driver.get_screenshot_as_file("./screenshots/test1.png")

    def test_logout(self, driver):
        try:
            homepage = HomePage(driver)
            homepage.click_logout()
            assert driver.title == "Amazon Sign-In"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            testName = environment.whoami()
            screenshotName = testName + "_screenshot_"
            # save screenshot in allure
            allure.attach(driver.get_screenshot_as_png(),name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            # to get the file on specific path
            driver.get_screenshot_as_file("./screenshots/" + screenshotName + ".png")
            raise
        except:
            print("There was an exception")
            testName = environment.whoami()
            screenshotName = testName + "_screenshot_"
            # save screenshot in allure
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            # to get the file on specific path
            driver.get_screenshot_as_file("./screenshots/" + screenshotName + ".png")
            # the raise is to show it as a failure
            raise
        else:
            print("No exceptions occurred")
        finally:
            print("Inside finally block")
