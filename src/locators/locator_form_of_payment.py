from abc import ABC, abstractmethod
from typing import Tuple
from appium.webdriver.common.appiumby import AppiumBy


class AbstractFormOfPaymentLocator(ABC):
    @abstractmethod
    def payment_cod(self) -> Tuple: pass

    @abstractmethod
    def payment_atm(self) -> Tuple: pass

    @abstractmethod
    def payment_international(self) -> Tuple: pass

    @abstractmethod
    def payment_vnpay(self) -> Tuple: pass

    @abstractmethod
    def continue_button(self) -> Tuple: pass


class FormOfPaymentPageAndroid(AbstractFormOfPaymentLocator):
    def payment_cod(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Thanh toán khi nhận hàng (COD)")')
    
    def payment_atm(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Thẻ ATM nội địa/Internet Banking (Hỗ trợ Internet Banking)")')
    
    def payment_international(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Thanh toán bằng thẻ quốc tế Visa, Master")')
    
    def payment_vnpay(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Thanh toán trực tuyến VNPAY")')
    
    def continue_button(self) -> Tuple:
        return (AppiumBy.ID, 'vn.hasaki.buyer:id/btnNext')
    

class FormOfPaymentPageIOS(AbstractFormOfPaymentLocator):
    def payment_cod(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'label == "Thanh toán khi nhận hàng (COD)"')
    
    def payment_atm(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'label == "Thẻ ATM nội địa/Internet Banking (Hỗ trợ Internet Banking)"')
    
    def payment_international(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'label == "Thanh toán bằng thẻ quốc tế Visa, Master"')
    
    def payment_vnpay(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'label == "Thanh toán trực tuyến VNPAY"')
    
    def continue_button(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'label == "Tiếp tục"')