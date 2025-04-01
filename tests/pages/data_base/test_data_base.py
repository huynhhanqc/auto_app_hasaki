import pytest
from src.data_base.database_connect import DatabaseConnector
import logging

@pytest.fixture
def db():
    db_connector = DatabaseConnector()
    db_connector.connect()
    yield db_connector
    db_connector.disconnect()

class TestDataBase:
    
    def test_db_connection(self,db: DatabaseConnector):
        assert db.connection.is_connected() == True, "Không thể kết nối tới cơ sở dữ liệu"

    @pytest.mark.parametrize("user_id", [654555])
    def test_delete_all_data(self, db: DatabaseConnector, user_id):
        deleted_rows = db.delete_data_cart(user_id)
        assert deleted_rows >= 0, f"Không thể xóa dữ liệu trong bảng cart cho user_id: {user_id}"
        if deleted_rows > 0:
            logging.info(f"Đã xóa {deleted_rows} bản ghi trong bảng cart cho user_id: {user_id}")
        else:
            logging.info(f"Không có bản ghi nào để xóa trong bảng cart cho user_id: {user_id}")