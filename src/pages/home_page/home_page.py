import logging
from appium.webdriver.common.appiumby import AppiumBy
from src.pages.base_page import BasePage
from time import sleep


class HomePageIos(BasePage):
    home_button = (AppiumBy.ACCESSIBILITY_ID, 'home')
    search_text_field = (AppiumBy.IOS_PREDICATE, 'value == "Tìm kiếm"')
    search_button = (AppiumBy.IOS_PREDICATE, 'name == "search"')
    accept_product = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeOther')
    white_scan_home_button = (AppiumBy.ACCESSIBILITY_ID, 'whiteScanHome')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sendkeys_search(self, text):
        try:
            self.click_element(self.search_text_field)
            self.send_keys_element(self.search_text_field, text)
        except Exception as e:
            logging.error(f"An error occurred while clicking search text: {e}")
            raise

    def click_btn_search(self):
        try:
            self.click_element(self.search_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking search button: {e}")
            raise

    def click_accept_product(self):
        try:
            self.click_element(self.accept_product)
        except Exception as e:
            logging.error(f"An error occurred while clicking accept product: {e}")
            raise

class HomePageAndroid(BasePage):

    search_title_field = (AppiumBy.ID, 'vn.hasaki.buyer:id/tvSearchTitle')
    search_box_field = (AppiumBy.ID, 'vn.hasaki.buyer:id/edSearchBox')
    accept_product = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.LinearLayout").instance(10)')
    white_scan_home_button = (AppiumBy.ID, 'vn.hasaki.buyer:id/ivScanBarcode')
    home_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Trang chủ")')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_home_button(self):
        try:
            self.click_element(self.home_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking home button: {e}")
            raise
    
    def sendkeys_search(self, text):
        try:
            sleep(1)
            self.click_element(self.search_title_field)
            sleep(1)
            self.send_keys_element(self.search_box_field, text)
            self.click_accept_product()
        except Exception as e:
            logging.error(f"An error occurred while clicking search text: {e}")
            raise

    def click_accept_product(self):
        try:
            self.click_element(self.accept_product)
        except Exception as e:
            logging.error(f"An error occurred while clicking accept product: {e}")
            raise

    