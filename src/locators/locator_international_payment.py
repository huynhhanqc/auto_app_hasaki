from abc import ABC, abstractmethod
from typing import Tuple
from appium.webdriver.common.appiumby import AppiumBy


class AbstractInternationalPaymentLocator(ABC):

    @abstractmethod
    def surname_field(self) -> Tuple:pass

    @abstractmethod
    def address_field(self) -> Tuple:pass

    @abstractmethod
    def city_field(self) -> Tuple:pass

    @abstractmethod
    def phone_field(self) -> Tuple:pass
    
    @abstractmethod
    def email_field(self) -> Tuple:pass
        
    @abstractmethod
    def visa_card_checkbox(self) -> Tuple:pass
        
    @abstractmethod
    def master_card_checkbox(self) -> Tuple:pass
        
    @abstractmethod
    def jcb_card_checkbox(self) -> Tuple:pass

    @abstractmethod
    def number_card_field(self) -> Tuple:pass
        
    @abstractmethod
    def expired_date_field(self) -> Tuple:pass
    
    @abstractmethod
    def option_date_field(self) -> Tuple:pass
        
    @abstractmethod
    def expired_year_field(self) -> Tuple:pass
    
    @abstractmethod
    def option_year_field(self) -> Tuple:pass

    @abstractmethod
    def cvn_field(self) -> Tuple:pass
        
    @abstractmethod
    def continue_button(self) -> Tuple:pass

    @abstractmethod
    def cancel_button(self) -> Tuple:pass

    @abstractmethod
    def pay_button(self) -> Tuple:pass

    @abstractmethod
    def come_back_button(self) -> Tuple:pass

    @abstractmethod
    def text_visa_card(self) -> Tuple:pass

    
    
class InternationalPaymentPageAndroid(AbstractInternationalPaymentLocator):
    
    def surname_field(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("vn.hasaki.buyer:id/etLastName")')
    
    def address_field(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("bill_to_address_line1")')
    
    def city_field(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("bill_to_address_city")')
    
    def phone_field(self) -> Tuple[str, str]:   
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("bill_to_phone")')
    
    def email_field(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("bill_to_email")')
    
    def visa_card_checkbox(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("card_type_001")')
    
    def master_card_checkbox(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("card_type_002")')
    
    def jcb_card_checkbox(self) -> Tuple[str, str]: 
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("card_type_007")')
    
    def number_card_field(self) -> Tuple[str, str]: 
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("card_number")')
    
    def expired_date_field(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("card_expiry_month")')
    
    def option_date_field(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ListView")')
    
    def expired_year_field(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("card_expiry_year")')
    
    def option_year_field(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ListView")')
    
    def cvn_field(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("card_cvn")')
    
    def continue_button(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Tiếp theo")')
    
    def cancel_button(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Hủy")')
    
    def come_back_button(self) -> Tuple[str, str]:
        return (AppiumBy.ID, 'vn.hasaki.buyer:id/btnBack')
    
    def text_visa_card(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Visa")')
    
    def pay_button(self) -> Tuple[str, str]:
        return (AppiumBy.XPATH, '//android.widget.Button[@text="Thanh toán"]')
    
    def back_button(self) -> Tuple[str, str]:
        return (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Quay lại")')
    


class InternationalPaymentPageIOS(AbstractInternationalPaymentLocator):

    def surname_field(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_PREDICATE, 'name == "Họ *" AND label == "Họ *" AND type == "XCUIElementTypeTextField"')
    
    def address_field(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_PREDICATE, 'name == "Địa chỉ Dòng 1 *" AND label == "Địa chỉ Dòng 1 *" AND type == "XCUIElementTypeTextField"')
    
    def city_field(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_PREDICATE, 'name == "Thành phố *" AND label == "Thành phố *" AND type == "XCUIElementTypeTextField"')
    
    def phone_field(self) -> Tuple[str, str]:   
        return (AppiumBy.IOS_PREDICATE, 'name == "Số Điện thoại *" AND label == "Số Điện thoại *" AND type == "XCUIElementTypeTextField"')
    
    def email_field(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_PREDICATE, 'name == "Email *" AND label == "Email *" AND type == "XCUIElementTypeTextField"')
    
    def visa_card_checkbox(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_PREDICATE, 'name == "Visa" AND label == "Visa" AND value == "0"')
    
    def master_card_checkbox(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_PREDICATE, 'name == "Mastercard" AND label == "Mastercard" AND value == "0"')
    
    def jcb_card_checkbox(self) -> Tuple[str, str]: 
        return (AppiumBy.IOS_PREDICATE, 'name == "JCB" AND label == "JCB" AND value == "0"')
    
    def number_card_field(self) -> Tuple[str, str]: 
        return (AppiumBy.IOS_PREDICATE, 'name == "Số Thẻ *" AND label == "Số Thẻ *" AND type == "XCUIElementTypeTextField"')
    
    def expired_date_field(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_PREDICATE, 'name == "Tháng hết hạn *" AND label == "Tháng hết hạn *" AND value == "Tháng"')
    
    def expired_year_field(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "Năm hết hạn *"`][2]')
    
    def cvn_field(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_PREDICATE, 'name == "CVN *" AND label == "CVN *" AND type == "XCUIElementTypeTextField"')
    
    def continue_button(self) -> Tuple[str, str]:   
        return (AppiumBy.ACCESSIBILITY_ID, 'Tiếp theo')
    
    def cancel_button(self) -> Tuple[str, str]:
        return (AppiumBy.ACCESSIBILITY_ID, 'Huỷ')
    
    def pay_button(self) -> Tuple[str, str]:    
        return (AppiumBy.ACCESSIBILITY_ID, 'Thanh toán')
    
    def come_back_button(self) -> Tuple[str, str]:  
        return (AppiumBy.ACCESSIBILITY_ID, 'Quay lại')
    
    def text_visa_card(self) -> Tuple[str, str]:
        return (AppiumBy.IOS_PREDICATE, '**/XCUIElementTypeStaticText[`name == "Visa"`]')
    

