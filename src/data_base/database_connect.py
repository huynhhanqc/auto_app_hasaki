import logging
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

class DatabaseConnector:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USERNAME")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_DATABASE")
        self.port = os.getenv("DB_PORT")
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Kết nối MySQL thành công")
            else:
                raise Exception("Kết nối không thành công")
        except Error as e:
            print(f"Lỗi kết nối: {e}")
            raise  

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            if self.cursor:
                self.cursor.close()
            self.connection.close()
            print("Đã ngắt kết nối MySQL")
        else:
            print("Không có kết nối để đóng")

    def execute(self, query, params=None):
        if not self.connection or not self.connection.is_connected():
            raise Exception("Chưa kết nối tới cơ sở dữ liệu")
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
        except Error as e:
            self.connection.rollback()
            raise Exception(f"Lỗi truy vấn: {e}")

    def fetch_one(self, query, params=None):
        if not self.connection or not self.connection.is_connected():
            raise Exception("Chưa kết nối tới cơ sở dữ liệu")
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchone()
        except Error as e:
            print(f"Lỗi truy vấn: {e}")
            raise
    
    def fetch_all(self, query, params=None):
        if not self.connection or not self.connection.is_connected():
            raise Exception("Chưa kết nối tới cơ sở dữ liệu")
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except Error as e:
            raise Exception(f"Lỗi truy vấn: {e}")
        
    def insert_data(self, data):
        """Insert data into the table, assuming id is auto-increment."""
        if not self.connection or not self.connection.is_connected():
            raise Exception("Database connection is not established")
        
        query = """
            INSERT INTO vendor_staff_schedule (
                vendor_id ,vendor_staff_id, staff_name, work_type ,shift_id, shift_time, location_id, work_date, status
            ) VALUES (%s,%s, %s, %s, %s, %s, %s,%s, %s)
        """
        try:
            self.cursor.executemany(query, data)    
            self.connection.commit()
            last_id = self.cursor.lastrowid
            return list(range(last_id - len(data) + 1, last_id + 1)) if last_id else []
        except Error as e:
            self.connection.rollback()
            logging.error(f"An error occurred while inserting data: {e}")
            raise

    def delete_data_cart(self, user_id):
        if not self.connection or not self.connection.is_connected():
            raise Exception("Database connection is not established")
        query = "DELETE FROM hasaki_carts WHERE user_id = %s AND order_id = 0"
        try:
            self.cursor.execute(query, (user_id,))
            affected_rows = self.cursor.rowcount 
            self.connection.commit()
            if affected_rows == 0:
                logging.info(f"Không có bản ghi nào để xóa trong 'hasaki_carts' cho user_id: {user_id}")
            else:
                logging.info(f"Đã xóa {affected_rows} bản ghi trong 'hasaki_carts' cho user_id: {user_id}")
            return affected_rows
        except Error as e:
            self.connection.rollback()
            logging.error(f"An error occurred while deleting data for user_id {user_id}: {e}")
            raise