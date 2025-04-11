from time import sleep
from src.pages.base_page import BasePage
import logging
from appium.webdriver.common.appiumby import AppiumBy

class ProductDetailOrderPageIOS(BasePage):
    buy_product_button = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    back_icon_button = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]')
    cart_button = (AppiumBy.ACCESSIBILITY_ID, 'cartButton')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_buy_product(self):
        try:
            self.click_element(self.buy_product_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking buy product: {e}")
            raise
    
    def click_btn_cart(self):
        try:
            self.click_element(self.cart_button)
            sleep(5)
        except Exception as e:
            logging.error(f"An error occurred while clicking cart button: {e}")
            raise
    
    def click_back_icon(self):
        try:
            self.click_element(self.back_icon_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking back icon: {e}")
            raise

class ProductDetailOrderPageAndroid(BasePage):
    buy_product_button = (AppiumBy.ID, 'vn.hasaki.buyer:id/tvAddToCart2hLabel')
    back_icon_button = (AppiumBy.ID, 'vn.hasaki.buyer:id/ivBackButton')
    cart_button = (AppiumBy.ID, 'vn.hasaki.buyer:id/ivCartButton')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_buy_product(self):
        try:
            self.click_element(self.buy_product_button)
        except Exception as e:
            logging.error(f"An error occurred while clicking buy product: {e}")
            raise
    
    def click_btn_cart(self):
        try:
            self.click_element(self.cart_button)
            sleep(5)
        except Exception as e:
            logging.error(f"An error occurred while clicking cart button: {e}")
            raise
    
    def click_back_icon(self):
        try:
            self.click_element(self.back_icon_button)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking back icon: {e}")
            raise
