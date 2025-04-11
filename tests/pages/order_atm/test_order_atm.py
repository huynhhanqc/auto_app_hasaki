import os
from dotenv import load_dotenv
import pytest
from requests import request
import logging
from src.pages.home_page.home_page import HomePageAndroid
from src.pages.product_detail_order_page.product_detail_order import ProductDetailOrderPageAndroid
from src.pages.cart_page.shopping_cart_page import ShoppingCartPage
from src.pages.order_confirmation_page.order_confirmation_page import OrderConfirmationPage
from src.pages.form_of_payment_page.form_of_payment_page import FormOfPaymentPage
from src.pages.form_of_payment_page.atm_payment_page import AtmPaymentPage
from src.pages.order_success_page.order_success_page import OrderSuccessPage
from src.utils.excel_handler import ExcelHandler
from tests.conftest import log_capture, logged_in_session_driver
from src.data_base.database_connect import DatabaseConnector

load_dotenv()
card_success = os.getenv("CARD_SUCCESS")
card_name = os.getenv("CARD_NAME")
card_expired_date = os.getenv("CARD_EXPIRED_DATE")
card_otp = os.getenv("CARD_OTP")
card_locked = os.getenv("CARD_LOCKED")
card_enough_money = os.getenv("CARD_ENOUGH_MONEY")
card_limit = os.getenv("CARD_LIMIT")
card_not_registerd = os.getenv("CARD_NOT_REGISTERD")

@pytest.fixture
def db():
    db_connector = DatabaseConnector()
    db_connector.connect()
    yield db_connector
    db_connector.disconnect()

logging = logging.getLogger(__name__)
excel_handler = ExcelHandler("/Users/mac/Downloads/Order_Atm.xlsx")
@pytest.mark.parametrize("tc_id,description,steps,expected_result", 
    excel_handler.read_test_data()
)

class TestOrderAtm:
    @pytest.mark.parametrize("user_id", [654612])
    def test_order_atm_001(self,db: DatabaseConnector,order_success:OrderSuccessPage,cart:ShoppingCartPage,atm_payment:AtmPaymentPage ,confirm:OrderConfirmationPage,form_of_payment:FormOfPaymentPage, user_id, logged_in_session_driver, tc_id, description,steps, expected_result,request):
        db.delete_data_cart(user_id)
        if tc_id != "TC_001":
            pytest.skip(f"Bỏ qua TC_ID {tc_id} vì chỉ chạy TC_001")
            return
        driver = logged_in_session_driver  
        home = HomePageAndroid(driver)
        product_detail_order = ProductDetailOrderPageAndroid(driver)
        status = ""
        try:
            logging.info(f"Running testcase {tc_id}: {description}")
            home.sendkeys_search(201600074)
            product_detail_order.click_buy_product()
            product_detail_order.click_btn_cart()
            cart.click_btn_proceed_to_order()
            confirm.click_payment_expression_button()
            form_of_payment.click_btn_payment_atm()
            confirm.click_order_button()
            atm_payment.input_card_number_field(card_success)
            atm_payment.input_card_full_name(card_name)
            atm_payment.input_card_expired_date(card_expired_date)
            atm_payment.input_otp_field(card_otp)
            order_success.get_text_order_code()
            assert order_success.get_text_order_success() == 'Đặt hàng thành công'
            assert True
            status = "Pass"
            logging.info(f"=== Kết thúc testcase {tc_id}: {description} ===")
        except Exception as e:
            logging.error(f"Testcase {tc_id} failed: {e}")
            log_capture(driver, f"{tc_id}_order_atm_Fail")
            status = "Fail"
            raise
        finally:
            excel_handler.update_test_result(tc_id, status)
            order_success.click_home_btn()
    
    @pytest.mark.parametrize("user_id", [654612])
    def test_order_atm_002(self,db: DatabaseConnector,cart:ShoppingCartPage,atm_payment:AtmPaymentPage,confirm:OrderConfirmationPage,form_of_payment:FormOfPaymentPage,user_id, logged_in_session_driver, tc_id, description,steps, expected_result,request):
        db.delete_data_cart(user_id)
        if tc_id != "TC_002":
            pytest.skip(f"Bỏ qua TC_ID {tc_id} vì chỉ chạy TC_002")
            return
        driver = logged_in_session_driver  
        home = HomePageAndroid(driver)
        product_detail_order = ProductDetailOrderPageAndroid(driver)
        status = ""
        try:
            logging.info(f"Running testcase {tc_id}: {description}")
            home.sendkeys_search(201600074)
            product_detail_order.click_buy_product()
            product_detail_order.click_btn_cart()
            cart.click_btn_proceed_to_order()
            confirm.click_payment_expression_button()
            form_of_payment.click_btn_payment_atm()
            confirm.click_order_button()
            atm_payment.input_card_number_field(card_locked)
            atm_payment.input_card_full_name(card_name)
            atm_payment.input_card_expired_date(card_expired_date)
            assert atm_payment.get_error_payment_fail() == 'Giao dịch không thành công. Thẻ hoặc tài khoản của Quý khách đang bị khóa.'
            assert True
            status = "Pass"
            logging.info(f"=== Kết thúc testcase {tc_id}: {description} ===")
        except Exception as e:
            logging.error(f"Testcase {tc_id} failed: {e}")
            log_capture(driver, f"{tc_id}_order_atm_Fail")
            status = "Fail"
            raise
        finally:
            excel_handler.update_test_result(tc_id, status)
            atm_payment.click_back_button()
            atm_payment.click_back_button()
            product_detail_order.click_back_icon()
            product_detail_order.click_back_icon()
    
    @pytest.mark.parametrize("user_id", [654612])
    def test_order_atm_003(self,db: DatabaseConnector,cart:ShoppingCartPage,atm_payment:AtmPaymentPage,confirm:OrderConfirmationPage,form_of_payment:FormOfPaymentPage,user_id, logged_in_session_driver, tc_id, description,steps, expected_result,request):
        db.delete_data_cart(user_id)
        if tc_id != "TC_003":
            pytest.skip(f"Bỏ qua TC_ID {tc_id} vì chỉ chạy TC_003")
            return
        driver = logged_in_session_driver  
        home = HomePageAndroid(driver)
        product_detail_order = ProductDetailOrderPageAndroid(driver)
        status = ""
        try:
            logging.info(f"Running testcase {tc_id}: {description}")
            home.sendkeys_search(201600074)
            product_detail_order.click_buy_product()
            product_detail_order.click_btn_cart()
            cart.click_btn_proceed_to_order()
            confirm.click_payment_expression_button()
            form_of_payment.click_btn_payment_atm()
            confirm.click_order_button()
            atm_payment.input_card_number_field(card_enough_money)
            atm_payment.input_card_full_name(card_name)
            atm_payment.input_card_expired_date(card_expired_date)
            assert atm_payment.get_error_payment_fail() == 'Giao dịch không thành công, tài khoản Quý khách không đủ tiền để thanh toán.'
            assert True
            status = "Pass"
            logging.info(f"=== Kết thúc testcase {tc_id}: {description} ===")
        except Exception as e:
            logging.error(f"Testcase {tc_id} failed: {e}")
            log_capture(driver, f"{tc_id}_order_atm_Fail")
            status = "Fail"
            raise
        finally:
            excel_handler.update_test_result(tc_id, status)
            atm_payment.click_back_button()
            atm_payment.click_back_button()
            product_detail_order.click_back_icon()
            product_detail_order.click_back_icon()

    @pytest.mark.parametrize("user_id", [654612])
    def test_order_atm_004(self,db: DatabaseConnector,cart:ShoppingCartPage,atm_payment:AtmPaymentPage,confirm:OrderConfirmationPage,form_of_payment:FormOfPaymentPage ,user_id, logged_in_session_driver, tc_id, description,steps, expected_result,request):
        db.delete_data_cart(user_id)
        if tc_id != "TC_004":
            pytest.skip(f"Bỏ qua TC_ID {tc_id} vì chỉ chạy TC_004")
            return
        driver = logged_in_session_driver  
        home = HomePageAndroid(driver)
        product_detail_order = ProductDetailOrderPageAndroid(driver)
        status = ""
        try:
            logging.info(f"Running testcase {tc_id}: {description}")
            home.sendkeys_search(201600074)
            product_detail_order.click_buy_product()
            product_detail_order.click_btn_cart()
            cart.click_btn_proceed_to_order()
            confirm.click_payment_expression_button()
            form_of_payment.click_btn_payment_atm()
            confirm.click_order_button()
            atm_payment.input_card_number_field(card_limit)
            atm_payment.input_card_full_name(card_name)
            atm_payment.input_card_expired_date(card_expired_date)
            assert atm_payment.get_error_payment_fail() == 'Giao dịch không thành công. Giao dịch vượt quá hạn mức số lần giao dịch trong ngày theo quy định của ngân hàng.'
            assert True
            status = "Pass"
            logging.info(f"=== Kết thúc testcase {tc_id}: {description} ===")
        except Exception as e:
            logging.error(f"Testcase {tc_id} failed: {e}")
            log_capture(driver, f"{tc_id}_order_atm_Fail")
            status = "Fail"
            raise
        finally:
            excel_handler.update_test_result(tc_id, status)
            atm_payment.click_back_button()
            atm_payment.click_back_button()
            product_detail_order.click_back_icon()
            product_detail_order.click_back_icon()

    @pytest.mark.parametrize("user_id", [654612])
    def test_order_atm_005(self,db:DatabaseConnector,cart:ShoppingCartPage,atm_payment:AtmPaymentPage,confirm:OrderConfirmationPage,form_of_payment:FormOfPaymentPage ,user_id, logged_in_session_driver, tc_id, description,steps, expected_result,request):
        db.delete_data_cart(user_id)
        if tc_id != "TC_005":
            pytest.skip(f"Bỏ qua TC_ID {tc_id} vì chỉ chạy TC_005")
            return
        driver = logged_in_session_driver  
        home = HomePageAndroid(driver)
        product_detail_order = ProductDetailOrderPageAndroid(driver)
        status = ""
        try:
            logging.info(f"Running testcase {tc_id}: {description}")
            home.sendkeys_search(201600074)
            product_detail_order.click_buy_product()
            product_detail_order.click_btn_cart()
            cart.click_btn_proceed_to_order()
            confirm.click_payment_expression_button()
            form_of_payment.click_btn_payment_atm()
            confirm.click_order_button()
            atm_payment.input_card_number_field(card_not_registerd)
            atm_payment.input_card_full_name(card_name)
            atm_payment.input_card_expired_date(card_expired_date)
            assert atm_payment.get_error_payment_fail() == 'Quý khách chưa đăng ký dịch vụ thanh toán trực tuyến, vui lòng liên hệ với ngân hàng.'
            assert True
            status = "Pass"
            logging.info(f"=== Kết thúc testcase {tc_id}: {description} ===")
        except Exception as e:
            logging.error(f"Testcase {tc_id} failed: {e}")
            log_capture(driver, f"{tc_id}_order_atm_Fail")
            status = "Fail"
            raise
        finally:
            excel_handler.update_test_result(tc_id, status)
            atm_payment.click_back_button()
            atm_payment.click_back_button()
            product_detail_order.click_back_icon()
            product_detail_order.click_back_icon()
            
            
