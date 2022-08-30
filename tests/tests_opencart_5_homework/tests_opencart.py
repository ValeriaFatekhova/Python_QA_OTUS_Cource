import pytest

from tests.tests_opencart_5_homework.pages.admin_login_page import AdminLoginPage
from tests.tests_opencart_5_homework.pages.catalog_page import CatalogPage
from tests.tests_opencart_5_homework.pages.home_page import HomePage
from tests.tests_opencart_5_homework.pages.product_page import ProductPage

# """Home page tests"""
#
#
# def test_home_page_logo(driver, url):
#     home_page = HomePage(driver)
#     home_page.open_home_page(url)
#     home_page.is_logo()
#     home_page.check_logo_link(url)
#
#
# def test_home_page_menu(driver, url):
#     home_page = HomePage(driver)
#     home_page.open_home_page(url)
#     home_page.is_menu()
#     home_page.check_menu_items(home_page.get_menu_items())
#
#
# def test_home_page_search(driver, url):
#     home_page = HomePage(driver)
#     home_page.open_home_page(url)
#     home_page.is_search()
#
#
# def test_home_page_cart(driver, url):
#     home_page = HomePage(driver)
#     home_page.open_home_page(url)
#     home_page.is_cart()
#
#
# def test_home_page_slideshow(driver, url):
#     home_page = HomePage(driver)
#     home_page.open_home_page(url)
#     home_page.is_slideshow()
#
#
# def test_home_page_content(driver, url):
#     home_page = HomePage(driver)
#     home_page.open_home_page(url)
#     home_page.is_content()
#
#
# """Catalog page tests"""
#
#
# @pytest.mark.parametrize(
#     "add_to_url",
#     [
#         "component/scanner",
#         "component/monitor",
#     ]
# )
# def test_catalog_left_menu(driver, url, add_to_url):
#     url = url + add_to_url
#     catalog_page = CatalogPage(driver)
#     catalog_page.open_catalog_page(url)
#     catalog_page.is_left_menu()
#     active_items = catalog_page.get_active_menu_items()
#     expected_items = add_to_url.split("/")
#     for i in range(len(expected_items)):
#         if expected_items[i].lower() in active_items[i].lower():
#             continue
#         else:
#             raise AssertionError(f"Incorrect active items in left menu")
#
#
# @pytest.mark.parametrize(
#     "add_to_url",
#     [
#         "component/scanner",
#         "component/monitor",
#     ]
# )
# def test_catalog_content(driver, url, add_to_url):
#     url = url + add_to_url
#     catalog_page = CatalogPage(driver)
#     catalog_page.open_catalog_page(url)
#     catalog_page.is_catalog_content()
#     if catalog_page.get_active_menu_items()[-1].find("0") != -1:
#         catalog_page.is_catalog_empty()
#     else:
#         assert str(len(catalog_page.get_products())) in catalog_page.get_active_menu_items()[-1]
#
#
# @pytest.mark.parametrize(
#     "add_to_url",
#     [
#         "component/scanner",
#         "component/monitor",
#     ]
# )
# def test_catalog_breadcrumbs(driver, url, add_to_url):
#     url = url + add_to_url
#     catalog_page = CatalogPage(driver)
#     catalog_page.open_catalog_page(url)
#     catalog_page.is_breadcrumbs()
#
#
# @pytest.mark.parametrize(
#     "add_to_url",
#     [
#         "component/scanner",
#         "component/monitor",
#     ]
# )
# def test_catalog_continue_button(driver, url, add_to_url):
#     url = url + add_to_url
#     catalog_page = CatalogPage(driver)
#     catalog_page.open_catalog_page(url)
#     if catalog_page.get_active_menu_items()[-1].find("0") != -1:
#         catalog_page.is_continue_button()
#     else:
#         try:
#             catalog_page.is_continue_button()
#         except AssertionError:
#             pass
#
#
# @pytest.mark.parametrize(
#     "add_to_url",
#     [
#         "component/scanner",
#         "component/monitor",
#     ]
# )
# def test_list_view_button(driver, url, add_to_url):
#     url = url + add_to_url
#     catalog_page = CatalogPage(driver)
#     catalog_page.open_catalog_page(url)
#     if catalog_page.get_active_menu_items()[-1].find("0") != -1:
#         try:
#             catalog_page.is_list_view_button()
#         except AssertionError:
#             pass
#     else:
#         catalog_page.is_list_view_button()
#
#
# """Product page tests"""
#
#
# @pytest.mark.parametrize(
#     "add_to_url",
#     [
#         "monitor/test",
#         "laptop-notebook/hp-lp3065",
#     ]
# )
# def test_product_thumbnails(driver, url, add_to_url):
#     url = url + add_to_url
#     product_page = ProductPage(driver)
#     product_page.open_product_page(url)
#     product_page.is_thumbnails()
#
#
# @pytest.mark.parametrize(
#     "add_to_url",
#     [
#         "monitor/test",
#         "laptop-notebook/hp-lp3065",
#     ]
# )
# def test_product_description(driver, url, add_to_url):
#     url = url + add_to_url
#     product_page = ProductPage(driver)
#     product_page.open_product_page(url)
#     product_page.is_product_description()
#
#
# @pytest.mark.parametrize(
#     "add_to_url",
#     [
#         "monitor/test",
#         "laptop-notebook/hp-lp3065",
#     ]
# )
# def test_product_review(driver, url, add_to_url):
#     url = url + add_to_url
#     product_page = ProductPage(driver)
#     product_page.open_product_page(url)
#     product_page.is_product_review()
#
#
# @pytest.mark.parametrize(
#     "add_to_url",
#     [
#         "monitor/test",
#         "laptop-notebook/hp-lp3065",
#     ]
# )
# def test_add_to_cart_button(driver, url, add_to_url):
#     url = url + add_to_url
#     product_page = ProductPage(driver)
#     product_page.open_product_page(url)
#     product_page.is_add_to_cart_button()
#
#
# @pytest.mark.parametrize(
#     "add_to_url",
#     [
#         "monitor/test",
#         "laptop-notebook/hp-lp3065",
#     ]
# )
# def test_product_rating(driver, url, add_to_url):
#     url = url + add_to_url
#     product_page = ProductPage(driver)
#     product_page.open_product_page(url)
#     product_page.is_rating()
#
#
# """Admin login page tests"""
#
#
# def test_admin_login_page_logo(driver, url):
#     admin_page = AdminLoginPage(driver)
#     admin_page.open_admin_login_page(url)
#     admin_page.is_admin_logo()
#     admin_page.check_logo_link()
#
#
# def test_al_username_field(driver, url):
#     admin_page = AdminLoginPage(driver)
#     admin_page.open_admin_login_page(url)
#     admin_page.is_user_name_field()
#
#
# def test_al_password_field(driver, url):
#     admin_page = AdminLoginPage(driver)
#     admin_page.open_admin_login_page(url)
#     admin_page.is_password_field()
#
#
# def test_al_login_button(driver, url):
#     admin_page = AdminLoginPage(driver)
#     admin_page.open_admin_login_page(url)
#     admin_page.is_login_button()
#
#
# def test_al_forgotten_password_link(driver, url):
#     admin_page = AdminLoginPage(driver)
#     admin_page.open_admin_login_page(url)
#     admin_page.is_forgotten_password_link()


"""Admin login page tests"""