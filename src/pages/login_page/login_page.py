from time import sleep
from src.pages.base_page import BasePage
import logging
from appium.webdriver.common.appiumby import AppiumBy


class LoginPageIOS(BasePage):

    icon_account = (AppiumBy.ACCESSIBILITY_ID, "account")
    icon_login = (AppiumBy.IOS_PREDICATE, 'name == "Đăng nhập" AND label == "Đăng nhập" AND value == "Đăng nhập"')
    text_account = (AppiumBy.ACCESSIBILITY_ID, "Email/ Số điện thoại")
    txt_password = (AppiumBy.ACCESSIBILITY_ID, "Mật khẩu")
    btn_submit = (AppiumBy.IOS_PREDICATE, 'name == "ĐĂNG NHẬP" AND label == "ĐĂNG NHẬP" AND value == "ĐĂNG NHẬP"')
    btn_logout = (AppiumBy.ACCESSIBILITY_ID, 'Đăng xuất')
    popup_agree_logout = (AppiumBy.ACCESSIBILITY_ID, 'Đồng ý')
    home_button = (AppiumBy.ACCESSIBILITY_ID, 'home')

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
            self.click_element(self.popup_agree_logout)
        except Exception as e:
            logging.error(f"An error occurred while clicking agree logout: {e}")
            raise

    def click_btn_logout(self):
        try:
            self.click_element(self.btn_logout)
        except Exception as e:
            logging.error(f"An error occurred while clicking logout button: {e}")
            raise
    
    def click_btn_home(self):
        try:
            self.click_element(self.home_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking home button: {e}")
            raise

    def click_icon_account(self):
        try:
            self.click_element(self.icon_account)
        except Exception as e:
            logging.error(f"An error occurred while clicking account: {e}")
            raise

    def click_btn_login(self):
        try:
            self.click_element(self.icon_login)
        except Exception as e:
            logging.error(f"An error occurred while clicking login button: {e}")
            raise

    def enter_text_account(self, text):
        try:
            self.send_keys_element(self.text_account, text)
        except Exception as e:
            logging.error(f"An error occurred while entering account text: {e}")
            raise

    def enter_text_password(self, text):
        try:
            self.send_keys_element(self.txt_password, text)
        except Exception as e:
            logging.error(f"An error occurred while entering password text: {e}")
            raise

    def click_btn_submit(self):
        try:
            self.click_element(self.btn_submit)
        except Exception as e:
            logging.error(f"An error occurred while clicking submit button: {e}")
            raise

class LoginPageAndroid(BasePage):

    icon_nar_drawer = (AppiumBy.ID, "vn.hasaki.buyer:id/ivNarDrawer")
    login_button = (AppiumBy.ID, 'vn.hasaki.buyer:id/tvBtnLogin')
    text_account = (AppiumBy.ID, "vn.hasaki.buyer:id/edtPhoneEmail")
    txt_password = (AppiumBy.ID, "vn.hasaki.buyer:id/edtPassword")
    btn_submit = (AppiumBy.ID, 'vn.hasaki.buyer:id/btnSignIn')
    icon_account = (AppiumBy.ID, 'vn.hasaki.buyer:id/ivAccount')
    logout_button = (AppiumBy.ID, 'vn.hasaki.buyer:id/tvLogout')
    agree_logout_button = (AppiumBy.ID, 'vn.hasaki.buyer:id/tvPositiveButton')
    iv_icon_nav_drawer = (AppiumBy.ID, 'vn.hasaki.buyer:id/ivIconNavDrawer')
    home_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Trang chủ")')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_server_android(self):
        try:
            self.click_login_button()
            self.enter_text_account("0344533989")
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

    def click_icon_nar_drawer(self):
        try:
            self.click_element(self.icon_nar_drawer)
        except Exception as e:
            logging.error(f"An error occurred while clicking navigation drawer: {e}")
            raise

    def click_login_button(self):
        try:
            self.click_element(self.login_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking login button: {e}")
            raise

    def enter_text_account(self, text):
        try:
            self.send_keys_element(self.text_account, text)
        except Exception as e:
            logging.error(f"An error occurred while entering account text: {e}")
            raise

    def enter_text_password(self, text):
        try:
            self.send_keys_element(self.txt_password, text)
        except Exception as e:
            logging.error(f"An error occurred while entering password text: {e}")
            raise

    def click_btn_submit(self):
        try:
            self.click_element(self.btn_submit)
        except Exception as e:
            logging.error(f"An error occurred while clicking submit button: {e}")
            raise

    def click_icon_account(self):
        try:
            self.click_element(self.icon_account)
        except Exception as e:
            logging.error(f"An error occurred while clicking account icon: {e}")
            raise

    def click_btn_logout(self):
        try:
            self.click_element(self.logout_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking logout button: {e}")
            raise

    def click_popup_agree_logout(self):
        try:
            self.click_element(self.agree_logout_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking agree logout button: {e}")
            raise

    def click_btn_home(self):
        try:
            self.click_element(self.home_button)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking home button: {e}")
            raise

    






    