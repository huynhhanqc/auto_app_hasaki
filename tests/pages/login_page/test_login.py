from src.pages.login_page.login_page import LoginPage
import logging
from tests.conftest import logged_in_session_driver

logging = logging.getLogger(__name__)

class TestLogin:
    def test_login_success(self, logged_in_session_driver):
        driver = logged_in_session_driver  
        login = LoginPage(driver)
        try:
            login.click_icon_account()
            login.click_btn_login()
            login.enter_text_account("0767241506")
            login.enter_text_password("123456")
            login.click_btn_submit()
            login.logout()
        except Exception as e:
            logging.error(f"An error occurred while test: {e}")
            assert False
 

   
