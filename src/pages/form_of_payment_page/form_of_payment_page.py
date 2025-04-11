from time import sleep
import logging
from src.locators.locator_form_of_payment import AbstractFormOfPaymentLocator
from src.pages.base_page import BasePage


class FormOfPaymentPage(BasePage):

    def __init__(self, driver, locator_factory: AbstractFormOfPaymentLocator ):
        super().__init__(driver)
        self.locators = locator_factory

    def click_btn_payment_cod(self):
        try:
            self.click_element(self.locators.payment_cod())
            sleep(1)
            self.click_btn_continue()
        except Exception as e:
            logging.error(f"An error occurred while clicking payment cod button: {e}")
            raise
    
    def click_btn_payment_atm(self):
        try:
            self.click_element(self.locators.payment_atm())
            sleep(1)
            self.click_btn_continue()
        except Exception as e:
            logging.error(f"An error occurred while clicking payment atm button: {e}")
            raise

    def click_btn_payment_international(self):
        try:
            self.click_element(self.locators.payment_international())
            sleep(1)
            self.click_btn_continue()
        except Exception as e:
            logging.error(f"An error occurred while clicking payment international button: {e}")
            raise
        
    def click_btn_payment_vnpay(self):
        try:
            self.click_element(self.locators.payment_vnpay())
            sleep(1)
            self.click_btn_continue()
        except Exception as e:
            logging.error(f"An error occurred while clicking payment vnpay button: {e}")
            raise

    def click_btn_continue(self):
        try:
            self.click_element(self.locators.continue_button())
        except Exception as e:
            logging.error(f"An error occurred while clicking continue button: {e}")
            raise