from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    PRODUCT_DESCRIPTION = (By.ID, "tab-description")
    PRODUCT_REVIEW = (By.CSS_SELECTOR, ".nav.nav-tabs li:nth-child(2)")
    THUMBNAILS = (By.CSS_SELECTOR, ".thumbnails")
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    RATING = (By.CSS_SELECTOR, ".rating")

    TIMEOUT_FOR_ELEMENTS = 3

    def __init__(self, driver):
        self.driver = driver

    def open_product_page(self, url):
        self.driver.get(url)

    def is_thumbnails(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.THUMBNAILS))
        except TimeoutException:
            raise AssertionError("Thumbnails are not presented for product")

    def is_product_description(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.PRODUCT_DESCRIPTION))
        except TimeoutException:
            raise AssertionError("Description is not presented for product")

    def is_product_review(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.PRODUCT_REVIEW))
        except TimeoutException:
            raise AssertionError("Review tab is not presented for product")

    def is_add_to_cart_button(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.ADD_TO_CART_BUTTON))
        except TimeoutException:
            raise AssertionError("'Add to cart' button is not presented for product")

    def is_rating(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.RATING))
        except TimeoutException:
            raise AssertionError("Rating is not presented for product")
