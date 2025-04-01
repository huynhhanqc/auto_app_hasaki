from time import sleep
from src.utils.common import ActionElement
from src.pages.login_page.locator_login_page import LocatorLogin
import logging

class LoginPage(ActionElement):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_server(self):
        try:
            self.scroll_down()
            self.click_btn_login()
            self.enter_text_account("0767241506")
            self.enter_text_password("123456")
            self.click_btn_submit()
            self.click_btn_home()
        except Exception as e:
            logging.error(f"An error occurred during login: {e}")
            raise

    def logout(self):
        try:
            self.click_icon_account()
            self.scroll_up()
            self.scroll_down()
            self.click_btn_logout()
            self.click_popup_agree_logout()
        except Exception as e:
            logging.error(f"An error occurred during logout: {e}")
            raise

    def click_popup_agree_logout(self):
        try:
            self.click_element(LocatorLogin.popup_agree_logout)
        except Exception as e:
            logging.error(f"An error occurred while clicking agree logout: {e}")
            raise

    def click_btn_logout(self):
        try:
            self.click_element(LocatorLogin.btn_logout)
        except Exception as e:
            logging.error(f"An error occurred while clicking logout button: {e}")
            raise
    
    def click_btn_home(self):
        try:
            self.click_element(LocatorLogin.btn_home_page)
        except Exception as e:
            logging.error(f"An error occurred while clicking home button: {e}")
            raise

    def click_icon_account(self):
        try:
            self.click_element(LocatorLogin.icon_account)
        except Exception as e:
            logging.error(f"An error occurred while clicking account: {e}")
            raise

    def click_btn_login(self):
        try:
            self.click_element(LocatorLogin.icon_login)
        except Exception as e:
            logging.error(f"An error occurred while clicking login button: {e}")
            raise

    def enter_text_account(self, text):
        try:
            self.send_keys_element(LocatorLogin.text_account, text)
        except Exception as e:
            logging.error(f"An error occurred while entering account text: {e}")
            raise

    def enter_text_password(self, text):
        try:
            self.send_keys_element(LocatorLogin.txt_password, text)
        except Exception as e:
            logging.error(f"An error occurred while entering password text: {e}")
            raise

    def click_btn_submit(self):
        try:
            self.click_element(LocatorLogin.btn_submit)
        except Exception as e:
            logging.error(f"An error occurred while clicking submit button: {e}")
            raise






    