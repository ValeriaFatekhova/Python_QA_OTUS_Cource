from tests.tests_opencart_5_homework.pages.home_page import HomePage


def test_home_page_logo(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_logo()
    home_page.check_logo_link(url)


def test_home_page_menu(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_menu()
    home_page.check_menu_items(home_page.get_menu_items())


def test_home_page_search(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_search()


def test_home_page_cart(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_cart()


def test_home_page_slideshow(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_slideshow()


def test_home_page_content(driver, url):
    home_page = HomePage(driver)
    home_page.open_home_page(url)
    home_page.is_content()
