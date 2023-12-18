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
        cls.test_text = "this is test text"  

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
    
    # def test_username_field(self):
    #     username_field = self.driver.find_element(By.XPATH, "//input[@type='text']")
    #     assert username_field.is_enabled(), "Failed to check username field"
    
    # def test_password_field(self):
    #     password_field = self.driver.find_element(By.XPATH, "//input[@type='password']")
    #     assert password_field.is_enabled(), "Failde to check password field"
    
    # def test_login_button(self):
    #     login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
    #     assert login_button.is_displayed(), "Failed to check login button"

    def test_login_account(self):
        username_field = self.driver.find_element(By.XPATH, "//input[@type='text']")
        password_field = self.driver.find_element(By.XPATH, "//input[@type='password']")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        username_field.send_keys('testuser')
        password_field.send_keys('Abcd1234!')
        login_button.click()
        time.sleep(5)

        title_element = self.driver.find_element(By.CLASS_NAME, "v-toolbar-title__placeholder")
        assert title_element.text == "Momento", "Failed to check login process"
    
    def test_display_post_button(self):
        button_post = self.driver.find_element(By.CLASS_NAME, "v-btn--elevated")
        assert button_post.is_displayed(), "Failed to check post button"
    
    def test_form_post(self):
        button_post = self.driver.find_element(By.CLASS_NAME, "v-btn--elevated")
        button_post.click()
        time.sleep(3)

        text_input = self.driver.find_element(By.XPATH, "//textarea")
        text_input.click()
        text_input.send_keys(self.test_text)
        send_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        send_button.click()
        time.sleep(3)

        post_text = self.driver.find_element(By.CLASS_NAME, "text-body-1")

        assert post_text.text == self.test_text, "Failed to check post form"
    
    def test_like_post(self):
        like_button = self.driver.find_element(By.CLASS_NAME, "text-red")
        like_button.click()
        time.sleep(2)

        like_number = self.driver.find_element(By.CLASS_NAME, "subheading")

        assert like_number.text == "1", "Failed to check like feature"
    
    def test_dislike_post(self):
        like_button = self.driver.find_element(By.CLASS_NAME, "text-red")
        like_button.click()
        time.sleep(2)

        like_number = self.driver.find_element(By.CLASS_NAME, "subheading")

        assert like_number.text == "0", "Failed to check like feature"
    
    def test_delete_post(self):
        delete_button = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .v-card:nth-child(1) .v-btn:nth-child(3) .v-icon__svg:nth-child(1)")
        delete_button.click()
        time.sleep(3)
        confirm_button = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        confirm_button.click()
        time.sleep(3)
        post_text = self.driver.find_element(By.CLASS_NAME, "text-body-1")
        
        assert post_text != self.test_text, "Failed to test delete post"
    
    def test_leaderboard(self):
        leaderboard_button = self.driver.find_element(By.CSS_SELECTOR, ".v-btn:nth-child(2) > .v-btn__content")
        leaderboard_button.click()
        time.sleep(3)
        leaderboard_table = self.driver.find_element(By.TAG_NAME, "table")
        assert leaderboard_table.is_displayed(), "Failed to test leaderboard"
    
    def test_logout(self):
        logout_button = self.driver.find_element(By.CSS_SELECTOR, ".v-btn:nth-child(4) > .v-btn__content")
        logout_button.click()
        confirm_button = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        confirm_button.click()
        time.sleep(3)
        login_page_text = self.driver.find_element(By.CLASS_NAME, "mt-8")
        assert login_page_text.is_displayed(), "Failed to test logout"




if __name__ == "__main__":
    pytest.main()



