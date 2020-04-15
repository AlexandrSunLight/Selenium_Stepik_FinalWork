from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_correct_message(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_CART_MESSAGE).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, "Wrong product name in message"

    def should_be_correct_price(self):
        assert self.browser.find_element(*ProductPageLocators.CART_PRICE_MESSAGE).text == self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, "Wrong price in message"