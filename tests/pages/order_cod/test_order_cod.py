import pytest
from requests import request
import logging
from src.pages.home_page.home_page import HomePageAndroid
from src.pages.product_detail_order_page.product_detail_order import ProductDetailOrderPageAndroid
from src.pages.cart_page.shopping_cart_page import ShoppingCartPage
from src.pages.order_confirmation_page.order_confirmation_page import OrderConfirmationPage
from src.pages.form_of_payment_page.form_of_payment_page import FormOfPaymentPage
from src.pages.order_success_page.order_success_page import OrderSuccessPage
from src.utils.excel_handler import ExcelHandler
from tests.conftest import log_capture, logged_in_session_driver
from src.data_base.database_connect import DatabaseConnector


@pytest.fixture
def db():
    db_connector = DatabaseConnector()
    db_connector.connect()
    yield db_connector
    db_connector.disconnect()

logging = logging.getLogger(__name__)
excel_handler = ExcelHandler("/Users/mac/Downloads/OrderCod.xlsx")
@pytest.mark.parametrize("tc_id,description,steps,expected_result", 
    excel_handler.read_test_data()
)
class TestOrderCOD:

    @pytest.mark.parametrize("user_id", [654555])
    def test_order_cod_001(self, db: DatabaseConnector,order_success:OrderSuccessPage,cart:ShoppingCartPage,confirm_mation:OrderConfirmationPage,form_of_payment:FormOfPaymentPage, user_id, logged_in_session_driver, tc_id, description,steps, expected_result,request):
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
            home.click_accept_product()
            product_detail_order.click_buy_product()
            product_detail_order.click_btn_cart()
            cart.click_btn_proceed_to_order()
            confirm_mation.click_payment_expression_button()
            form_of_payment.click_btn_payment_cod()
            confirm_mation.click_order_button()
            order_success.get_text_order_code()
            order_success.click_home_btn()
            status = "Pass"
            logging.info(f"=== Kết thúc testcase {tc_id}: {description} ===")
        except Exception as e:
            logging.error(f"Testcase {tc_id} failed: {e}")
            log_capture(driver, f"{tc_id}_Fail")
            status = "Fail"
            raise
        finally:
            excel_handler.update_test_result(tc_id, status)
        
    @pytest.mark.parametrize("user_id", [654555])
    def test_order_cod_002(self,db: DatabaseConnector,order_success:OrderSuccessPage,cart:ShoppingCartPage,confirm_mation:OrderConfirmationPage,form_of_payment:FormOfPaymentPage , user_id, logged_in_session_driver, tc_id, description,steps, expected_result,request):
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
            home.sendkeys_search(100230069)
            home.click_accept_product()
            product_detail_order.click_buy_product()
            product_detail_order.click_btn_cart()
            cart.click_btn_proceed_to_order()
            confirm_mation.click_payment_expression_button()
            form_of_payment.click_btn_payment_cod()
            confirm_mation.click_order_button()
            order_success.get_text_order_code()
            order_success.click_home_btn()
            status = "Pass"
            logging.info(f"=== Kết thúc testcase {tc_id}: {description} ===")
        except Exception as e:
            logging.error(f"Testcase {tc_id} failed: {e}")
            log_capture(driver, f"{tc_id}_Fail")
            status = "Fail"
            raise
        finally:
            excel_handler.update_test_result(tc_id, status)
    
    