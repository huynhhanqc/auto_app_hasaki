import random
from time import sleep
import logging
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from src.pages.base_page import BasePage
from src.locators.locator_international_payment import AbstractInternationalPaymentLocator
from appium.webdriver.common.appiumby import AppiumBy


class InternationalPaymentPage(BasePage):

    def __init__(self, driver, locator_factory: AbstractInternationalPaymentLocator):
        super().__init__(driver)
        self.locators = locator_factory

    def input_address_field(self, address):
        try:
            self.send_keys_element(self.locators.address_field(), address)
        except Exception as e:
            logging.error(f"An error occurred while inputting address: {e}")
            raise

    def input_city_field(self, city):
        try:
            self.send_keys_element(self.locators.city_field(), city)
        except Exception as e:
            logging.error(f"An error occurred while inputting city: {e}")
            raise

    def input_phone_field(self, phone):
        try:
            self.send_keys_element(self.locators.phone_field(), phone)
        except Exception as e:
            logging.error(f"An error occurred while inputting phone: {e}")
            raise

    def input_email_field(self, email):
        try:
            self.send_keys_element(self.locators.email_field(), email)
            self.scroll_up()
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while inputting email: {e}")
            raise

    def click_visa_card_checkbox(self):
        try:
            self.click_element(self.locators.visa_card_checkbox())
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking Visa card checkbox: {e}")
            raise
    
    def click_master_card_checkbox(self):
        try:
            self.click_element(self.locators.master_card_checkbox())
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking MasterCard checkbox: {e}")
            raise

    def click_jcb_card_checkbox(self):
        try:
            self.click_element(self.locators.jcb_card_checkbox())
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking JCB card checkbox: {e}")
            raise

    def input_number_card_field(self, number_card):
        try:
            self.click_element(self.locators.number_card_field())
            self.send_keys_element(self.locators.number_card_field(), number_card)
        except Exception as e:
            logging.error(f"An error occurred while inputting number card: {e}")
            raise

    def input_expired_date_field(self):
        try:
            self.click_element(self.locators.expired_date_field())
            sleep(1)
            option = self.get_options(self.locators.option_date_field())
            random_option = random.choice(option)
            self.click_element(random_option)
            sleep(3)
        except Exception as e:
            logging.error(f"An error occurred while inputting expired date: {e}")
            raise
        
    def input_expired_year_field(self):
        try:
            self.click_element(self.locators.expired_year_field())
            sleep(1)
            option = self.get_options(self.locators.option_year_field())
            random_option = random.choice(option)
            self.click_element(random_option)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while inputting expired date: {e}")
            raise
    
    def input_cvn_field(self, cvn):
        try:
            self.click_element(self.locators.cvn_field())
            self.send_keys_element(self.locators.cvn_field(), cvn)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while inputting CVN: {e}")
            raise

    def click_continue_button(self):    
        try:
            self.click_element(self.locators.continue_button())
            sleep(2)
        except Exception as e:
            logging.error(f"An error occurred while clicking continue button: {e}")
            raise

    def click_cancel_button(self):  
        try:
            self.click_element(self.locators.cancel_button())
        except Exception as e:
            logging.error(f"An error occurred while clicking cancel button: {e}")
            raise

    def click_pay_button(self):
        try:
            self.click_element(self.locators.pay_button())
            sleep(7)
        except Exception as e:
            logging.error(f"An error occurred while clicking pay button: {e}")
            raise
        
    
        
    




    



    
    
    



 

