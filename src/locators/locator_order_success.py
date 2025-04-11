from abc import ABC, abstractmethod
from typing import Tuple
from appium.webdriver.common.appiumby import AppiumBy

class AbstractOrderSuccessLocator(ABC):
    @abstractmethod
    def text_order_success(self) -> Tuple:pass
    
    @abstractmethod
    def text_order_code(self) -> Tuple:pass
    
    @abstractmethod    
    def back_icon_button(self) -> Tuple:pass
    
    @abstractmethod
    def purchased_order_button(self) -> Tuple:pass
    
    @abstractmethod
    def home_btn(self) -> Tuple:pass
    
    @abstractmethod
    def back_icon_button(self) -> Tuple:pass
    
    
class OrderSuccessLocatorAndroid(AbstractOrderSuccessLocator):
    
    def text_order_success(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Đặt hàng thành công")')
    
    def text_order_code(self) -> Tuple[str, str]:
        return (AppiumBy.ID, "vn.hasaki.buyer:id/tvOrderIncrementId")
    
    def back_icon_button(self) -> Tuple[str, str]:
        return (AppiumBy.ID, 'vn.hasaki.buyer:id/ivBack')
    
    def purchased_order_button(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Đơn mua")')
    
    def home_btn(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Trang chủ")')
    
    def back_icon_button(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("vn.hasaki.buyer:id/ivBack")')
    
    
class OrderSuccessLocatorIOS(AbstractOrderSuccessLocator):

    def text_order_success(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_PREDICATE, 'name == "Đặt hàng thành công" AND label == "Đặt hàng thành công" AND type == "XCUIElementTypeStaticText"')
    
    def text_order_code(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_PREDICATE, 'name == "Mã đơn hàng:" AND label == "Mã đơn hàng:" AND type == "XCUIElementTypeStaticText"')
    
    def back_icon_button(self) -> Tuple[str, str]:
        return (AppiumBy.ACCESSIBILITY_ID, 'back')
    
    def purchased_order_button(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_PREDICATE, 'name == "Đơn mua" AND label == "Đơn mua" AND type == "XCUIElementTypeButton"')
    
    def home_btn(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_PREDICATE, 'name == "Trang chủ" AND label == "Trang chủ" AND value == "Trang chủ"')