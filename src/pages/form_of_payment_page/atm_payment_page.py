from time import sleep
import logging
from appium.webdriver.common.appiumby import AppiumBy
from src.locators.locator_atm_payment import AbstractAtmPaymentLocator
from src.pages.base_page import BasePage

class AtmPaymentPage(BasePage):
    
    def __init__(self, driver, locator_factory: AbstractAtmPaymentLocator):
        super().__init__(driver)
        self.locators = locator_factory

    def input_card_number_field(self, card_number):
        max_retries = 3
        for _ in range(max_retries):
            try:
                self.click_element(self.locators.card_number_field)
                self.send_keys_element(self.locators.card_number_field, card_number)
                sleep(2)
                break
            except Exception as e:
                if _ == max_retries - 1:
                    logging.error(f"An error occurred while inputting card number: {e}")
                    raise
        
    def input_card_full_name(self, card_full_name):
        max_retries = 3
        for _ in range(max_retries):
            try:
                self.click_element(self.locators.card_full_name_field)
                self.send_keys_element(self.locators.card_full_name_field, card_full_name)
                sleep(2)
                break
            except Exception as e:
                if _ == max_retries - 1:
                    logging.error(f"An error occurred while inputting card full name: {e}")
                    raise
    
    def input_card_expired_date(self, expired_date):
        max_retries = 3
        for _ in range(max_retries):
            try:
                self.click_element(self.locators.card_expired_date)
                self.send_keys_element(self.locators.card_expired_date, expired_date)
                sleep(1)
                self.click_element(self.locators.continue_button1)
                sleep(4)
                break
            except Exception as e:
                if _ == max_retries - 1:
                    logging.error(f"An error occurred while inputting expired date: {e}")
                    raise

    def input_otp_field(self, otp):
        try:
            self.send_keys_element(self.locators.otp_field, otp)
            sleep(2)
            self.click_element(self.locators.continue_button2)
            sleep(5)
        except Exception as e:
            logging.error(f"An error occurred while inputting otp: {e}")
            raise
    
    def get_error_payment_fail(self):
        try:
            return self.get_text_element(self.locators.error_payment_fail)
        except Exception as e:
            logging.error(f"An error occurred while getting text payment atm fail: {e}")
            raise
    