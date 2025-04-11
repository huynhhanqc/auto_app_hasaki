from datetime import datetime
import logging
import os
import time
import pytest
from src.utils.driver_setup import setup_driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.pages.login_page.login_page import LoginPageAndroid


_session_logged_in = False
@pytest.fixture(scope='session')
def appium_driver_session(request):
    driver = None
    logging.info("--- [Session Scope - Fixture appium_driver_session] Starting ---")
    try:
        driver = setup_driver()
        driver.implicitly_wait(10)
        logging.info("--- [Session Scope - Fixture appium_driver_session] Driver is ready ---")

        def session_finalizer():
            logging.info("--- [Session Scope - Fixture appium_driver_session] Teardown starting ---")
            if driver:
                try:
                    logging.info("Executing driver.quit()...")
                    driver.quit()
                    logging.info("Driver closed and session deleted successfully.")
                except Exception as e:
                    logging.error(f"Error during driver.quit(): {e}", exc_info=True)
            logging.info("--- [Session Scope - Fixture appium_driver_session] Teardown finished ---")
        request.addfinalizer(session_finalizer)
        yield driver
    except Exception as e:
        logging.error(f"--- [Session Scope - Fixture appium_driver_session] CRITICAL ERROR during driver initialization: {e}", exc_info=True)
        if driver:
            try: driver.quit()
            except: pass
        pytest.fail(f"Could not initialize driver for session: {e}", pytrace=False)

@pytest.fixture(scope='session')
def logged_in_session_driver( appium_driver_session ):
    global _session_logged_in
    driver = appium_driver_session 
    logging.info("--- [Session Scope - Fixture logged_in_session_driver] Starting ---")
    login_android = LoginPageAndroid(driver)
    if not _session_logged_in:
        logging.info("Session status: Not logged in. Proceeding with check/login.")
        try:
            # Kiểm tra sự tồn tại của nút login
            login_android.click_icon_nar_drawer()
            login_button = (AppiumBy.ID, 'vn.hasaki.buyer:id/tvBtnLogin')
            is_login_button_present = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(login_button)
            )
            if is_login_button_present:
                logging.info("==> Login button detected. User is not logged in.")
                login_android.login_server_android()
                logging.info("==> Login successful.")
                _session_logged_in = True
            else:
                logging.info("==> Login button not detected. User is already logged in.")
                _session_logged_in = True
        except TimeoutException:
            logging.info("==> Login button not detected within timeout. User is already logged in.")
            login_android.click_btn_home()
            _session_logged_in = True
        except Exception as login_err:
            logging.error(f"ERROR during login process: {login_err}", exc_info=True)
            pytest.fail(f"Login failed, cannot continue session: {login_err}", pytrace=False)
    else:
        logging.info("Session status: Already logged in (checked by fixture).")
    yield driver
    logging.info("--- [Session Scope - Fixture logged_in_session_driver] Finished ---")

#Config report
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        report_dir = "reporthtml"
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)  
        report_path = os.path.join(report_dir, f"report_{timestamp}.html")
        config.option.htmlpath = report_path
        logger = logging.getLogger(__name__)
        logger.info(f"Configured HTML report path: {report_path}")
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(f"Failed to configure HTML report: {e}")
        raise

def pytest_addoption(parser):
    parser.addoption(
        "--tcid", action="store", default=None, help="Chỉ định TC_ID để chạy test cụ thể"
    )

@pytest.fixture
def request_tcid(request):
    return request.config.getoption("--tcid")

def log_capture(driver, test_name):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")  
    filename = f"screenshots/{test_name}_{timestamp}.png"
    driver.save_screenshot(filename) 
    logging.info(f"📸 Đã chụp ảnh lỗi: {filename}")



