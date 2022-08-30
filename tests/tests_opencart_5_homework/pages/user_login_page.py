from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserLoginPage:

    FIRST_NAME_FIELD = (By.ID, "input-firstname")
    LAST_NAME_FIELD= (By.ID, "input-lastname")
    EMAIL_FIELD = (By.ID, "input-email")
    PHONE_FIELD = (By.ID, "input-telephone")
    RIGHT_MENU = (By.ID, "column-right")
    MENU_ITEMS = (By.CSS_SELECTOR, "#column-right div a")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#column-right div a")

    TIMEOUT_FOR_ELEMENTS = 3
    USER_LOGIN_URL = "index.php?route=account/register"

    MENU_LIST = [
        ("Login", "http://localhost/index.php?route=account/login"),
        ("Register", "http://localhost/index.php?route=account/register"),
        ("Forgotten Password", "http://localhost/index.php?route=account/forgotten"),
        ("My Account", "http://localhost/index.php?route=account/account"),
        ("Address Book", "http://localhost/index.php?route=account/address"),
        ("Wish List", "http://localhost/index.php?route=account/wishlist"),
        ("Order History", "http://localhost/index.php?route=account/order"),
        ("Downloads", "http://localhost/index.php?route=account/download"),
        ("Recurring payments", "http://localhost/index.php?route=account/recurring"),
        ("Reward Points", "http://localhost/index.php?route=account/reward"),
        ("Returns", "http://localhost/index.php?route=account/return"),
        ("Transactions", "http://localhost/index.php?route=account/transaction"),
        ("Newsletter", "http://localhost/index.php?route=account/newsletter"),
    ]

    def __init__(self, driver):
        self.driver = driver

    def open_user_login_page(self, url):
        self.driver.get(url+self.USER_LOGIN_URL)

    def is_first_name_field(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        except TimeoutException:
            raise AssertionError("First name field is not presented on User login page")

    def is_last_name_field(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.LAST_NAME_FIELD))
        except TimeoutException:
            raise AssertionError("Last name field is not presented on User login page")

    def is_email_field(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        except TimeoutException:
            raise AssertionError("Email field is not presented on User login page")

    def is_continue_button(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        except TimeoutException:
            raise AssertionError("Continue button is not presented on User login page")

    def is_right_menu(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.RIGHT_MENU))
        except TimeoutException:
            raise AssertionError("Menu is not displayed on User login page")

    def get_menu_items(self):
        try:
            return WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_all_elements_located(self.MENU_ITEMS))
        except TimeoutException:
            raise AssertionError("Menu items are not presented onUser login page")

    def check_menu_items(self, elements):
        for i in range(len(elements)):
            temp = (elements[i].text, elements[i].get_attribute("href"))
            if temp != self.MENU_LIST[i]:
                raise AssertionError("Menu items are incorrect")

