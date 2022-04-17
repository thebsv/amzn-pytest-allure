from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "ap_email"
        self.username_fwd = "continue"
        self.password_textbox_id = "ap_password"
        self.login_button_id = "signInSubmit"

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)
        self.driver.find_element(By.ID, self.username_fwd).click()

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)
        self.driver.find_element(By.ID, self.login_button_id).click()

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button_id).click()