import re
from time import sleep
from src.locators.locator_order_success import AbstractOrderSuccessLocator
from src.pages.base_page import BasePage
import logging


class OrderSuccessPage(BasePage):

    def __init__(self, driver, locator_factory: AbstractOrderSuccessLocator):
        super().__init__(driver)
        self.locators = locator_factory

    def get_text_order_code(self):
        try:
            full_text = self.get_text_element(self.locators.text_order_code())
            logging.info(f"Full text: {full_text}")
            order_code = re.search(r"Mã đơn hàng: (\d+)", full_text)
            if order_code:
                code = order_code.group(1)  
                logging.info(f"Mã đơn hàng: {code}")
                print(f"Mã đơn hàng: {code}")
                return code
            else:
                raise ValueError("Order number not found in string")
        except Exception as e:
            logging.error(f"An error occurred while getting order code text: {e}")
            raise

    def get_text_order_success(self):
        try:
            return self.get_text_element(self.locators.text_order_success())
        except Exception as e:
            logging.error(f"An error occurred while getting order success text: {e}")
            raise
    
    def click_back_icon(self):
        try:
            self.click_element(self.locators.back_icon_button())
        except Exception as e:
            logging.error(f"An error occurred while clicking back icon: {e}")
            raise
    
    def click_purchased_order_button(self):
        try:
            self.click_element(self.locators.purchased_order_button())
        except Exception as e:
            logging.error(f"An error occurred while clicking purchased order button: {e}")
            raise
    
    def click_home_btn(self):
        try:
            self.click_element(self.locators.home_btn())    
        except Exception as e:
            logging.error(f"An error occurred while clicking home button: {e}")
            raise
        
    def assert_text_order_success(self):
        try:
            self.get_text_element(self.locators.text_order_success())
        except Exception as e:
            logging.error(f"An error occurred while asserting text order success: {e}")
            raise