import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
import time
from faker import Faker

# faker for auto generating testing data
fake = Faker()
test_name = fake.name()
test_username = "membertest-" + str(fake.pyint())
test_email = fake.free_email()
test_password = 'Vbnam7890!'
test_admin_name = fake.name()
test_admin_email = fake.free_email()
test_admin_username = "admintest-" + str(fake.pyint())
test_text = "this is test text" 

# prevent launch browser GUI
display = Display(visible=0, size=(800, 800))
display.start()

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()

options = [
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
]

for option in options:
    chrome_options.add_argument(option)


class TestMemberFearture:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get("http://localhost:4173")
        
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
    
    def test_display_login_button(self):
        login_button = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        assert login_button.is_displayed(), "Failed to check login button"

    def test_display_signup_button(self):
        signup_button = self.driver.find_element(By.XPATH, "//a[@href='/signup']")
        assert signup_button.is_displayed(), "Failed to check signup button"
    
    def test_register_user(self):
        signup_button = self.driver.find_element(By.XPATH, "//a[@href='/signup']")
        signup_button.click()
        time.sleep(2)


        name_field = self.driver.find_element(By.ID, "name")
        email_field = self.driver.find_element(By.ID, "email")
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        retype_password_field = self.driver.find_element(By.ID, "passwordConfirm")
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        name_field.send_keys(test_name)
        email_field.send_keys(test_email)
        username_field.send_keys(test_username)
        password_field.send_keys(test_password)
        retype_password_field.send_keys(test_password)
        submit_button.click()
        time.sleep(2)
        regis_text = self.driver.find_element(By.TAG_NAME, "h2")

        assert regis_text.text == "Account Registration Success!", "Failed to check register user"

    def test_login_account(self):
        time.sleep(5)
        login_link = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        login_link.click()
        
        username_field = self.driver.find_element(By.XPATH, "//input[@type='text']")
        password_field = self.driver.find_element(By.XPATH, "//input[@type='password']")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        username_field.send_keys(test_username)
        password_field.send_keys(test_password)
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
        text_input.send_keys(test_text)
        send_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        send_button.click()
        time.sleep(3)

        post_text = self.driver.find_element(By.CLASS_NAME, "text-body-1")

        assert post_text.text == test_text, "Failed to check post form"
    
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
        
        assert post_text != test_text, "Failed to test delete post"
    
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


class TestAdminFeature:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get("http://localhost:4173/admin_signup")
        time.sleep(5)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
    
    def test_register_admin(self):
        name_field = self.driver.find_element(By.ID, "name")
        email_field = self.driver.find_element(By.ID, "email")
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        retype_password_field = self.driver.find_element(By.ID, "passwordConfirm")
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        name_field.send_keys(test_admin_name)
        email_field.send_keys(test_admin_email)
        username_field.send_keys(test_admin_username)
        password_field.send_keys(test_password)
        retype_password_field.send_keys(test_password)
        submit_button.click()
        time.sleep(2)
        regis_text = self.driver.find_element(By.TAG_NAME, "h2")

        assert regis_text.text == "Admin Account Registration Success!", "Failed to check register user"
    
    def test_login_admin(self):
        time.sleep(5)
        login_link = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        login_link.click()
        
        username_field = self.driver.find_element(By.XPATH, "//input[@type='text']")
        password_field = self.driver.find_element(By.XPATH, "//input[@type='password']")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        username_field.send_keys(test_admin_username)
        password_field.send_keys(test_password)
        login_button.click()
        time.sleep(5)

        title_element = self.driver.find_element(By.CLASS_NAME, "v-toolbar-title__placeholder")
        assert title_element.text == "Momento", "Failed to check login process"

    def test_admin_panel(self):
        admin_panel_button = self.driver.find_element(By.CSS_SELECTOR, ".v-btn--flat:nth-child(3)")
        admin_panel_button.click()
        time.sleep(3)

        admin_page_title = self.driver.find_element(By.TAG_NAME, "h5")

        assert admin_page_title.text == "Menu Admin", "Failed to check admin panel button"


if __name__ == "__main__":
    pytest.main()



