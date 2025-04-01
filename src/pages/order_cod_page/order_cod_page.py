import re
from time import sleep
from src.pages.order_cod_page.locator import LocatorOrderCod
from src.utils.common import ActionElement
import logging
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException


class OrderCodPage(ActionElement):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sendkeys_search(self, text):
        try:
            self.click_element(LocatorOrderCod.search_text_field)
            self.send_keys_element(LocatorOrderCod.search_text_field, text)
        except Exception as e:
            logging.error(f"An error occurred while clicking search text: {e}")
            raise

    def click_btn_search(self):
        try:
            self.click_element(LocatorOrderCod.search_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking search button: {e}")
            raise

    def click_accept_product(self):
        try:
            self.click_element(LocatorOrderCod.accept_product)
        except Exception as e:
            logging.error(f"An error occurred while clicking accept product: {e}")
            raise

    def click_buy_product(self):
        try:
            self.click_element(LocatorOrderCod.buy_product_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking buy product: {e}")
            raise

    def click_btn_cart(self):
        try:
            self.click_element(LocatorOrderCod.cart_button)
            sleep(5)
        except Exception as e:
            logging.error(f"An error occurred while clicking cart button: {e}")
            raise

    def click_btn_proceed_to_order(self):
        try:
            self.click_element(LocatorOrderCod.proceed_to_order_button)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking proceed to order button: {e}")
            raise

    def click_btn_order_cod(self):
        try:
            self.click_element(LocatorOrderCod.order_cod_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking order cod button: {e}")
            raise

    def get_text_order_code(self):
        try:
            full_text = self.get_attribute_element(LocatorOrderCod.text_order_code, "name")
            logging.info(f"Full text: {full_text}")
            order_code = re.search(r"Mã đơn hàng: (\d+)", full_text)
            if order_code:
                code = order_code.group(1)  
                logging.info(f"Mã đơn hàng: {code}")
                print(f"Mã đơn hàng: {code}")
                return code
            else:
                raise ValueError("Không tìm thấy mã đơn hàng trong chuỗi")
        except Exception as e:
            logging.error(f"An error occurred while getting order code text: {e}")
            raise

    def click_back_home(self):
        try:
            self.click_element(LocatorOrderCod.back_home_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking back home button: {e}")
            raise

    def click_btn_payment_expression(self):
        try:
            self.click_element(LocatorOrderCod.payment_expression_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking payment expression button: {e}")
            raise
    
    def get_text_payment_expression(self):
        try:
            payment_expression = self.get_text_element(LocatorOrderCod.text_payment_expression)
            return payment_expression
        except Exception as e:
            logging.error(f"An error occurred while getting payment expression text: {e}")
            raise
    
    def click_back_icon(self):
        try:
            self.click_element(LocatorOrderCod.back_icon_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking back icon: {e}")
            raise

    