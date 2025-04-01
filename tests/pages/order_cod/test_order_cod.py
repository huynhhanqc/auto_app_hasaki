import pytest
from requests import request
import logging
from src.pages.order_cod_page.order_cod_page import OrderCodPage
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
    def test_order_cod_001(self,db: DatabaseConnector,user_id, logged_in_session_driver, tc_id, description,steps, expected_result,request):
        db.delete_data_cart(user_id)
        if tc_id != "TC_001":
            pytest.skip(f"Bỏ qua TC_ID {tc_id} vì chỉ chạy TC_001")
            return
        driver = logged_in_session_driver  
        order = OrderCodPage(driver)
        status = ""
        try:
            logging.info(f"Running testcase {tc_id}: {description}")
            order.sendkeys_search(201600074)
            order.click_btn_search()
            order.click_accept_product()
            order.click_buy_product()
            order.click_btn_cart()
            order.click_btn_proceed_to_order()
            order.click_btn_order_cod()
            order.click_back_home()
            status = "Pass"
            logging.info(f"=== Kết thúc testcase {tc_id}: {description} ===")
        except Exception as e:
            logging.error(f"Testcase {tc_id} failed: {e}")
            log_capture(driver, f"{tc_id}_Fail")
            status = "Fail"
            raise
        finally:
            excel_handler.update_test_result(tc_id, status)
    
    