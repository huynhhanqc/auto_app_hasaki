from time import sleep
from src.locators.locator_shopping_cart import AbstractShoppingCartLocator
from src.pages.base_page import BasePage
import logging


class ShoppingCartPage(BasePage):

    def __init__(self, driver, locator_factory: AbstractShoppingCartLocator):
        super().__init__(driver)
        self.locators = locator_factory

    def click_btn_proceed_to_order(self):
        try:
            self.click_element(self.locators.btn_proceed_to_order())
        except Exception as e:
            logging.error(f"An error occurred while clicking proceed to order button: {e}")
            raise