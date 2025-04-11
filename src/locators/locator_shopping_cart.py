from abc import ABC, abstractmethod
from typing import Tuple
from appium.webdriver.common.appiumby import AppiumBy


class AbstractShoppingCartLocator(ABC):

    @abstractmethod
    def btn_proceed_to_order(self) -> Tuple: pass


class ShoppingCartPageIOS(AbstractShoppingCartLocator):
    def btn_proceed_to_order(self) -> Tuple:
        return (AppiumBy.IOS_PREDICATE, 'name == "TIẾN HÀNH ĐẶT HÀNG" AND label == "TIẾN HÀNH ĐẶT HÀNG" AND value == "TIẾN HÀNH ĐẶT HÀNG"')
    

class ShoppingCartPageAndroid(AbstractShoppingCartLocator):
    def btn_proceed_to_order(self) -> Tuple:
        return (AppiumBy.ID, 'vn.hasaki.buyer:id/btnCheckOut')