from datetime import datetime
import logging
import os
import time
import pytest
from src.utils.driver_setup import setup_driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.utils.common import ActionElement
from src.pages.login_page.login_page import LoginPage


_session_logged_in = False
@pytest.fixture(scope='session')
def appium_driver_session(request):
    driver = None
    logging.info("--- [Session Scope - Fixture appium_driver_session] Bắt đầu ---")
    try:
        driver = setup_driver() 
        driver.implicitly_wait(10) 
        logging.info("--- [Session Scope - Fixture appium_driver_session] Driver đã sẵn sàng ---")

        def session_finalizer():
            logging.info("--- [Session Scope - Fixture appium_driver_session] Teardown bắt đầu ---")
            if driver:
                try:
                    logging.info("Đang thực hiện driver.quit()...")
                    driver.quit()
                    logging.info("Đã đóng driver và xóa session thành công.")
                except Exception as e:
                    logging.error(f"Lỗi khi thực hiện driver.quit(): {e}", exc_info=True)
            logging.info("--- [Session Scope - Fixture appium_driver_session] Teardown kết thúc ---")

        request.addfinalizer(session_finalizer)
        yield driver 
    except Exception as e:
        logging.error(f"--- [Session Scope - Fixture appium_driver_session] LỖI NGHIÊM TRỌNG khi khởi tạo driver: {e}", exc_info=True)
        if driver: 
            try: driver.quit()
            except: pass
        pytest.fail(f"Không thể khởi tạo driver cho session: {e}", pytrace=False)

@pytest.fixture(scope='session')
def logged_in_session_driver( appium_driver_session ):
    global _session_logged_in
    driver = appium_driver_session 
    logging.info("--- [Session Scope - Fixture logged_in_session_driver] Bắt đầu ---")
    action_element = ActionElement(driver)
    login = LoginPage(driver)

    if not _session_logged_in:
        logging.info("Trạng thái session: Chưa login. Tiến hành kiểm tra/login.")
        try:
            login.click_icon_account()
            action_element.scroll_up()
            logout_button_locator = (AppiumBy.ACCESSIBILITY_ID, 'Đăng xuất')
            logging.info(f"Kiểm tra sự tồn tại của element sau login: {logout_button_locator}")
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(logout_button_locator)
            )
            logging.info("==> Phát hiện element sau login. Session đã đăng nhập.")
            login.click_btn_home()
            _session_logged_in = True
        except (NoSuchElementException, TimeoutException):
            logging.info("==> Không tìm thấy element sau login. Thực hiện các bước đăng nhập...")
            try:
                login.login_server()
            except Exception as login_err:
                logging.error(f"LỖI trong quá trình thực hiện login: {login_err}", exc_info=True)
                pytest.fail(f"Login thất bại, không thể tiếp tục session: {login_err}", pytrace=False)
    else:
        logging.info("Trạng thái session: Đã login (kiểm tra bởi fixture).")
    yield driver
    logging.info("--- [Session Scope - Fixture logged_in_session_driver] Kết thúc ---")

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

