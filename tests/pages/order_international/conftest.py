import logging
import pytest
from src.locators.locator_form_of_payment import AbstractFormOfPaymentLocator, FormOfPaymentPageAndroid, FormOfPaymentPageIOS
from src.locators.locator_order_confirmation import AbstractOrderConfirmMationLocator, OrderConfirmationPageAndroid, OrderConfirmationPageIOS
from src.locators.locator_order_success import AbstractOrderSuccessLocator, OrderSuccessLocatorAndroid, OrderSuccessLocatorIOS
from src.locators.locator_shopping_cart import AbstractShoppingCartLocator, ShoppingCartPageAndroid, ShoppingCartPageIOS
from src.pages.cart_page.shopping_cart_page import ShoppingCartPage
from src.pages.form_of_payment_page.International_payment_page import InternationalPaymentPage
from src.locators.locator_international_payment import InternationalPaymentPageIOS, InternationalPaymentPageAndroid , AbstractInternationalPaymentLocator
from src.pages.form_of_payment_page.form_of_payment_page import FormOfPaymentPage
from src.pages.order_confirmation_page.order_confirmation_page import OrderConfirmationPage
from src.pages.order_success_page.order_success_page import OrderSuccessPage

#thanh toán thẻ quốc tế
def get_international_payment_page(driver_instance) -> AbstractInternationalPaymentLocator:
    platform = driver_instance.capabilities.get('platformName', '').lower()
    logging.debug(f"Determining login locator factory for platform: {platform}")
    if platform == 'android':
        return InternationalPaymentPageAndroid()
    elif platform == 'ios':
        return InternationalPaymentPageIOS()
    else:
        raise ValueError(f"Platform '{platform}' is not supported by login locator factories.")
    
@pytest.fixture(scope="function")
def international_payment(logged_in_session_driver):
    driver = logged_in_session_driver
    locator_factory = get_international_payment_page(driver)
    page = InternationalPaymentPage(driver, locator_factory)
    yield page
    
#trang xác nhận đơn hàng  
def get_order_confirm_mation_page(driver_instance) -> AbstractOrderConfirmMationLocator:
    platform = driver_instance.capabilities.get('platformName', '').lower()
    logging.debug(f"Determining login locator factory for platform: {platform}")
    if platform == 'android':
        return OrderConfirmationPageAndroid()
    elif platform == 'ios':
        return OrderConfirmationPageIOS()
    else:
        raise ValueError(f"Platform '{platform}' is not supported by login locator factories.")

@pytest.fixture(scope="function")
def confirm_mation(logged_in_session_driver):
    driver = logged_in_session_driver
    locator_factory = get_order_confirm_mation_page(driver)
    page = OrderConfirmationPage(driver, locator_factory)
    yield page
    
#trang chọn hình thức thanh toán
def get_form_of_payment_page(driver_instance) -> AbstractFormOfPaymentLocator:
    platform = driver_instance.capabilities.get('platformName', '').lower()
    logging.debug(f"Determining login locator factory for platform: {platform}")
    if platform == 'android':
        return FormOfPaymentPageAndroid()
    elif platform == 'ios':
        return FormOfPaymentPageIOS()
    else:
        raise ValueError(f"Platform '{platform}' is not supported by login locator factories.")

@pytest.fixture(scope="function")
def form_of_payment(logged_in_session_driver):
    driver = logged_in_session_driver
    locator_factory = get_form_of_payment_page(driver)
    page = FormOfPaymentPage(driver, locator_factory)
    yield page
    
#trang giỏ hàng
def get_cart_page(driver_instance) -> AbstractShoppingCartLocator:
    platform = driver_instance.capabilities.get('platformName', '').lower()
    logging.debug(f"Determining login locator factory for platform: {platform}")
    if platform == 'android':
        return ShoppingCartPageAndroid()
    elif platform == 'ios':
        return ShoppingCartPageIOS()
    else:
        raise ValueError(f"Platform '{platform}' is not supported by login locator factories.")

@pytest.fixture(scope="function")
def shopping_cart(logged_in_session_driver):
    driver = logged_in_session_driver
    locator_factory = get_cart_page(driver)
    page = ShoppingCartPage(driver, locator_factory)
    yield page
    
#trang thành công
def get_order_success_page(driver_instance) -> AbstractOrderSuccessLocator:
    platform = driver_instance.capabilities.get('platformName', '').lower()
    logging.debug(f"Determining login locator factory for platform: {platform}")
    if platform == 'android':
        return OrderSuccessLocatorAndroid()
    elif platform == 'ios':
        return OrderSuccessLocatorIOS()
    else:
        raise ValueError(f"Platform '{platform}' is not supported by login locator factories.")

@pytest.fixture(scope="function")
def order_success(logged_in_session_driver):
    driver = logged_in_session_driver
    locator_factory = get_order_success_page(driver)
    page = OrderSuccessPage(driver, locator_factory)
    yield page