from abc import ABC, abstractmethod
from typing import Tuple
from appium.webdriver.common.appiumby import AppiumBy


class AbstractOrderConfirmMationLocator(ABC):
    @abstractmethod
    def change_address_button(self) -> Tuple: pass

    @abstractmethod
    def payment_expression_button(self) -> Tuple: pass

    @abstractmethod
    def discount_code_button(self) -> Tuple: pass

    @abstractmethod
    def voucher_button(self) -> Tuple: pass

    @abstractmethod
    def order_button(self) -> Tuple: pass


class OrderConfirmationPageAndroid(AbstractOrderConfirmMationLocator):

    def change_address_button(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("vn.hasaki.buyer:id/ivArrow").instance(0)')
    
    def payment_expression_button(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("vn.hasaki.buyer:id/ivArrow").instance(1)')
    
    def discount_code_button(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("vn.hasaki.buyer:id/ivArrow").instance(3)')
    
    def voucher_button(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("vn.hasaki.buyer:id/ivArrow").instance(2)')
    
    def order_button(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Đặt hàng")')
    

class OrderConfirmationPageIOS(AbstractOrderConfirmMationLocator):

    def change_address_button(self) -> Tuple:
        return (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "arrowLeft"`][1]')
    
    def payment_expression_button(self) -> Tuple:
        return (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeButton[1]')
    
    def discount_code_button(self) -> Tuple:
        return (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "arrowLeft"`][3]')
    
    def voucher_button(self) -> Tuple:
        return (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "arrowLeft"`][4]')
    
    def order_button(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'name == "Đặt hàng" AND label == "Đặt hàng" AND value == "Đặt hàng"')