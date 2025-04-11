import logging
import pytest
from src.pages.form_of_payment_page.atm_payment_page import AtmPaymentPage
from src.locators.locator_atm_payment import AbstractAtmPaymentLocator, AtmPaymentPageAndroid, AtmPaymentPageIOS


def get_international_payment_page(driver_instance) -> AbstractAtmPaymentLocator:
    platform = driver_instance.capabilities.get('platformName', '').lower()
    logging.debug(f"Determining login locator factory for platform: {platform}")
    if platform == 'android':
        return AtmPaymentPageAndroid()
    elif platform == 'ios':
        return AtmPaymentPageIOS()
    else:
        raise ValueError(f"Platform '{platform}' is not supported by login locator factories.")
    
@pytest.fixture(scope="function")
def atm_payment(logged_in_session_driver):
    driver = logged_in_session_driver
    locator_factory = get_international_payment_page(driver)
    page = AtmPaymentPage(driver, locator_factory)
    yield page
