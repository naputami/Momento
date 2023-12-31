import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
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


chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()

options = [
    "--headless",
    "--window-size=1920,1080",
    "--ignore-certificate-errors",
    'user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"',
    "--no-sandbox"
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
        time.sleep(2)
        send_button.click()
        time.sleep(10)

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
        delete_button = self.driver.find_element(By.CLASS_NAME, "delete-post")
        delete_button.click()
        time.sleep(3)
        confirm_button = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        confirm_button.click()
        time.sleep(1)
        delete_notification = self.driver.find_element(By.ID, "swal2-title")
        
        assert delete_notification.text == 'Deleting post successfully!', "Failed to test delete post"
    
    def test_leaderboard(self):
        leaderboard_button = self.driver.find_element(By.XPATH, "//div[@id='app']/div/div/header/div/div[3]/a[2]")
        time.sleep(5)
        leaderboard_button.click()
        time.sleep(5)
        leaderboard_table = self.driver.find_element(By.TAG_NAME, "table")
        assert leaderboard_table.is_displayed(), "Failed to test leaderboard"
    
    def test_logout(self):
        logout_button = self.driver.find_element(By.XPATH, "//div[@id='app']/div/div/header/div/div[3]/button/span[3]")
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
        admin_panel_button = self.driver.find_element(By.XPATH, "//div[@id='app']/div/div/header/div/div[3]/a[3]/span[3]")
        admin_panel_button.click()
        time.sleep(3)

        admin_page_title = self.driver.find_element(By.TAG_NAME, "h5")

        assert admin_page_title.text == "Menu Admin", "Failed to check admin panel button"


if __name__ == "__main__":
    pytest.main()



