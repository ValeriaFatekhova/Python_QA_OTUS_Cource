from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminLoginPage:

    USER_NAME_FIELD = (By.ID, "input-username")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, "span.help-block")
    ADMIN_LOGO = (By.ID, "header-logo")
    ADMIN_LOGO_LINK = (By.CSS_SELECTOR, "#header-logo a")

    TIMEOUT_FOR_ELEMENTS = 3
    ADMIN_URL = "admin"
    ADMIN_LINK = "http://localhost/admin/index.php?route=common/login"

    def __init__(self, driver):
        self.driver = driver

    def open_admin_login_page(self, url):
        self.driver.get(url+self.ADMIN_URL)

    def is_user_name_field(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.USER_NAME_FIELD))
        except TimeoutException:
            raise AssertionError("User name field is not presented on Admin login page")

    def is_password_field(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        except TimeoutException:
            raise AssertionError("Password field is not presented on Admin login page")

    def is_login_button(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
        except TimeoutException:
            raise AssertionError("Login button is not presented on Admin login page")

    def is_forgotten_password_link(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.FORGOTTEN_PASSWORD))
        except TimeoutException:
            raise AssertionError("Forgotten password link is not presented on Admin login page")

    def is_admin_logo(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.ADMIN_LOGO))
        except TimeoutException:
            raise AssertionError("Logo is not presented on Admin login page")

    def get_link_by_locator(self, locator):
        try:
            return WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(locator)).get_attribute("href")
        except TimeoutException:
            raise AssertionError(f"Element {locator} doesn't have link to Admin Login page")

    def check_logo_link(self):
        if self.get_link_by_locator(self.ADMIN_LOGO_LINK) != self.ADMIN_LINK:
            raise AssertionError("Admin Logo link is incorrect")
