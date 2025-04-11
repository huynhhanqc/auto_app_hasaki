from abc import ABC, abstractmethod
from typing import Tuple
from appium.webdriver.common.appiumby import AppiumBy


class AbstractAtmPaymentLocator(ABC):

    @abstractmethod
    def card_number_field(self) -> Tuple: pass

    @abstractmethod
    def card_full_name_field(self) -> Tuple: pass

    @abstractmethod
    def card_expired_date(self) -> Tuple: pass

    @abstractmethod
    def continue_button1(self) -> Tuple: pass

    @abstractmethod
    def cancel_button1(self) -> Tuple: pass

    @abstractmethod
    def continue_button2(self) -> Tuple: pass

    @abstractmethod
    def cancel_button2(self) -> Tuple: pass

    @abstractmethod
    def otp_field(self) -> Tuple: pass

    @abstractmethod
    def back_button(self) -> Tuple: pass

    @abstractmethod
    def error_payment_fail(self) -> Tuple: pass

    @abstractmethod
    def back_button(self) -> Tuple: pass

class AtmPaymentPageAndroid(AbstractAtmPaymentLocator):

    def card_number_field(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("napasCardNo")')
    
    def card_full_name_field(self) -> Tuple:
        return AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("napasNameOnCard")'
    
    def card_expired_date(self) -> Tuple:   
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("napasIssueDate")')
    
    def continue_button1(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("napasProcessBtn1")')

    def cancel_button1(self):
        return  (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("napasCancelBtn1")')
    
    def otp_field(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("napasOtpCode")')
    
    def continue_button2(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("napasProcessBtn2")')
    
    def cancel_button2(self) -> Tuple:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("napasCancelBtn2")')
    
    def error_payment_fail(self):
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("napasNotificationResult")')
    
    def back_button(self) -> Tuple:
        return (AppiumBy.ID, 'vn.hasaki.buyer:id/ivBack')


class AtmPaymentPageIOS(AbstractAtmPaymentLocator):

    def card_number_field(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'name == "napasCardNo"')

    def card_full_name_field(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'name == "napasNameOnCard"')

    def card_expired_date(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'name == "napasIssueDate"')

    def continue_button1(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'name == "napasProcessBtn1"')

    def cancel_button1(self):
        return (AppiumBy.IOS_PREDICATE, 'name == "napasCancelBtn1"')

    def otp_field(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'name == "napasOtpCode"')

    def continue_button2(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'name == "napasProcessBtn2"')

    def cancel_button2(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'name == "napasCancelBtn2"')

    def error_payment_fail(self):
        return (AppiumBy.IOS_PREDICATE, 'name == "napasNotificationResult"')

    def back_button(self) -> Tuple:
        return (AppiumBy.ACCESSIBILITY_ID, 'Back')