from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage:

    LEFT_MENU = (By.ID, "column-left")
    CATALOG_CONTENT = (By.ID, "content")
    ACTIVE_MENU_ITEMS = (By.CSS_SELECTOR, "#column-left .active")
    EMPTY_CATALOG_MESSAGE = (By.CSS_SELECTOR, "#content>p")
    PRODUCTS = (By.CSS_SELECTOR, ".product-layout.product-grid")
    BREADCRUMB = (By.CSS_SELECTOR, ".breadcrumb")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    LIST_VIEW_BUTTON = (By.ID, "list-view")

    TIMEOUT_FOR_ELEMENTS = 3

    def __init__(self, driver):
        self.driver = driver

    def open_catalog_page(self, url):
        self.driver.get(url)

    def is_left_menu(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.LEFT_MENU))
        except TimeoutException:
            raise AssertionError("Left menu is not displayed on Catalog page")

    def is_catalog_content(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.CATALOG_CONTENT))
        except TimeoutException:
            raise AssertionError("Catalog is not presented on Catalog page")

    def get_active_menu_items(self):
        try:
            items = WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_all_elements_located(self.ACTIVE_MENU_ITEMS))
            texts = []
            for i in items:
                texts.append(self.get_text_by_element(i))
            return texts
        except TimeoutException:
            raise AssertionError("No active elements in left menu on Catalog page")

    def get_text_by_element(self, element):
        return element.text

    def is_catalog_empty(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.EMPTY_CATALOG_MESSAGE))
        except TimeoutException:
            raise AssertionError("Catalog should be empty")

    def get_products(self):
        try:
            return WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_all_elements_located(self.PRODUCTS))
        except TimeoutException:
            raise AssertionError("No products in catalog")

    def is_breadcrumbs(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.BREADCRUMB))
        except TimeoutException:
            raise AssertionError("Breadcrumbs is not presented on Catalog page")

    def is_continue_button(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.CONTINUE_BUTTON))
        except TimeoutException:
            raise AssertionError("Continue button is not presented in empty catalog")

    def is_list_view_button(self):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_FOR_ELEMENTS).until(EC.visibility_of_element_located(self.LIST_VIEW_BUTTON))
        except TimeoutException:
            raise AssertionError("List view button is not presented")
