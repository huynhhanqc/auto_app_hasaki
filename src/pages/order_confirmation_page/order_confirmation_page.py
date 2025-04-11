from time import sleep
from src.locators.locator_order_confirmation import AbstractOrderConfirmMationLocator
from src.pages.base_page import BasePage
import logging


class OrderConfirmationPage(BasePage):
    
    def __init__(self, driver, locator_factory: AbstractOrderConfirmMationLocator):
        super().__init__(driver)
        self.locators = locator_factory

    def click_change_address_button(self):
        try:
            self.click_element(self.locators.change_address_button())
        except Exception as e:
            logging.error(f"An error occurred while clicking change address button: {e}")
            raise
    
    def click_payment_expression_button(self):
        try:
            self.click_element(self.locators.payment_expression_button())
        except Exception as e:
            logging.error(f"An error occurred while clicking payment expression button: {e}")
            raise
    
    def click_discount_code_button(self):
        try:
            self.click_element(self.locators.discount_code_button())
        except Exception as e:
            logging.error(f"An error occurred while clicking discount code button: {e}")
            raise
    
    def click_voucher_button(self):
        try:
            self.click_element(self.locators.voucher_button())
        except Exception as e:
            logging.error(f"An error occurred while clicking voucher button: {e}")
            raise

    def click_order_button(self):
        try:
            self.click_element(self.locators.order_button())
            sleep(7)
        except Exception as e:
            logging.error(f"An error occurred while clicking order cod button: {e}")
            raise