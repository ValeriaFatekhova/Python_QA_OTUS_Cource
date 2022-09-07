from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    LOGO = (By.ID, "logo")
    LOGO_LINK = (By.CSS_SELECTOR, "#logo a")
    CART = (By.ID, "cart")
    MENU = (By.ID, "menu")
    MENU_ITEMS = (By.CSS_SELECTOR, "#menu ul.nav>li>a")
    SEARCH = (By.ID, "search")
    CONTENT = (By.ID, "content")
    SLIDESHOW = (By.ID, "slideshow0")
    COMPANIES = (By.ID, "carousel0")

    MENU_LIST = [
        ("Desktops", "http://localhost/desktops"),
        ("Laptops & Notebooks", "http://localhost/laptop-notebook"),
        ("Components", "http://localhost/component"),
        ("Tablets", "http://localhost/tablet"),
        ("Software", "http://localhost/software"),
        ("Phones & PDAs", "http://localhost/smartphone"),
        ("Cameras", "http://localhost/camera"),
        ("MP3 Players", "http://localhost/mp3-players"),
    ]

    HOME_PAGE_URL = "http://localhost/index.php?route=common/home"

    TIMEOUT_FOR_ELEMENTS = 3

    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self, url):
        self.driver.get(url)

    def is_logo(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.LOGO))
        except TimeoutException:
            raise AssertionError("Logo is not displayed on Home page")

    def is_search(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.SEARCH))
        except TimeoutException:
            raise AssertionError("Search is not displayed on Home page")

    def is_cart(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.CART))
        except TimeoutException:
            raise AssertionError("Cart is not displayed on Home page")

    def is_menu(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.MENU))
        except TimeoutException:
            raise AssertionError("Menu is not displayed on Home page")

    def is_content(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.CONTENT))
        except TimeoutException:
            raise AssertionError("Content area is not presented on Home page")

    def is_slideshow(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.SLIDESHOW))
        except TimeoutException:
            raise AssertionError("Slideshow is not displayed on Home page")

    def is_companies(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.COMPANIES))
        except TimeoutException:
            raise AssertionError("Companies list is not displayed on Home page")

    def get_link_by_locator(self, locator):
        try:
            return WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(locator)).get_attribute("href")
        except TimeoutException:
            raise AssertionError(f"Element {locator} doesn't have link to Home page")

    def check_logo_link(self, url):
        if self.get_link_by_locator(self.LOGO_LINK) != self.HOME_PAGE_URL:
            raise AssertionError("Logo link is incorrect")

    def get_menu_items(self):
        try:
            return WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_all_elements_located(self.MENU_ITEMS))
        except TimeoutException:
            raise AssertionError("Menu items are not presented on Home page")

    def check_menu_items(self, elements):
        for i in range(len(elements)):
            temp = (elements[i].text, elements[i].get_attribute("href"))
            if temp != self.MENU_LIST[i]:
                raise AssertionError("Menu items are incorrect")
