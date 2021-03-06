from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time
import pytest

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_be_correct_message()
    page.should_be_correct_price()
    
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_not_be_success_message()
    
@pytest.mark.skip
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.should_not_be_success_message()
    
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.is_disappeared()
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_page()