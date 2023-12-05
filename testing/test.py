import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
import time

# display = Display(visible=0, size=(800, 800))
# display.start()

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()

options = [
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
]

for option in options:
    chrome_options.add_argument(option)


class TestFrontPage:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get("http://localhost:4173")
        

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
    
    def test_display_login_button(self):
        login_button = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        assert login_button.is_displayed(), "Pengecekan login button gagal"

    def test_display_signup_button(self):
        signup_button = self.driver.find_element(By.XPATH, "//a[@href='/signup']")
        assert signup_button.is_displayed(), "Pengecekan signup button gagal"

class TestLoginPage:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get("http://localhost:4173/login")
        time.sleep(5)  

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
    
    def test_username_field(self):
        username_field = self.driver.find_element(By.XPATH, "//input[@type='text']")
        assert username_field.is_enabled(), "Failed to check username field"
    
    def test_password_field(self):
        password_field = self.driver.find_element(By.XPATH, "//input[@type='password']")
        assert password_field.is_enabled(), "Failde to check password field"
    
    def test_login_button(self):
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        assert login_button.is_displayed(), "Failed to check login button"

    def test_login_account(self):
        username_field = self.driver.find_element(By.XPATH, "//input[@type='text']")
        password_field = self.driver.find_element(By.XPATH, "//input[@type='password']")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        username_field.send_keys('admin1')
        password_field.send_keys('Abcd1234!')
        login_button.click()
        time.sleep(10)

        title_element = self.driver.find_element(By.CLASS_NAME, "v-toolbar-title__placeholder")
        assert title_element.text == "Momento", "Failed to check login process"


if __name__ == "__main__":
    pytest.main()



