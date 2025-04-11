from src.pages.login_page.login_page import LoginPageIOS, LoginPageAndroid
import logging
from tests.conftest import logged_in_session_driver

logging = logging.getLogger(__name__)

class TestLogin:
    def test_login_success(self, logged_in_session_driver):
        driver = logged_in_session_driver  
        login_android = LoginPageAndroid(driver)
        try:
            login_android.click_icon_account()
            login_android.click_login_button()
            login_android.enter_text_account("0332333444")
            login_android.enter_text_password("123456")
            login_android.click_btn_submit()
        except Exception as e:
            logging.error(f"An error occurred while test: {e}")
            assert False
 

   
