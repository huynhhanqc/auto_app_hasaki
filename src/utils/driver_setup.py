import json
import os
from appium import webdriver
import logging
from appium.webdriver.webdriver import AppiumOptions

logging.basicConfig(filename="logs/test_log.log", level=logging.ERROR)

def setup_driver():
    config_path = os.path.join(os.path.dirname(__file__), "../config/config.json")
    logging.info(f"Đang đọc file config từ: {config_path}")
    if not os.path.exists(config_path):
        logging.error(f"File config.json không tồn tại tại: {config_path}")
        raise FileNotFoundError(f"File config.json không tồn tại tại: {config_path}")
    if not os.access(config_path, os.R_OK):
        logging.error(f"Không có quyền đọc file config.json tại: {config_path}")
        raise PermissionError(f"Không có quyền đọc file config.json tại: {config_path}")
    try:
        with open(config_path, "r") as file:
            content = file.read().strip()
            logging.info(f"Nội dung file config.json: {content}")
            desired_caps = json.loads(content) 
        if desired_caps is None or not isinstance(desired_caps, dict):
            logging.error(f"desired_caps không hợp lệ: {desired_caps}, kiểu: {type(desired_caps)}")
            raise ValueError(f"desired_caps không hợp lệ: {desired_caps}")
        required_keys = ["platformName", "udid", "bundleId"]
        missing_keys = [key for key in required_keys if key not in desired_caps]
        if missing_keys:
            logging.error(f"Thiếu các khóa cần thiết trong config.json: {missing_keys}")
            raise ValueError(f"Thiếu các khóa cần thiết: {missing_keys}")
        logging.info(f"Đã tải cấu hình: {desired_caps}")
        appium_options = AppiumOptions()
        appium_options.load_capabilities(desired_caps)
        driver = webdriver.Remote("http://localhost:4723", options=appium_options)
        logging.info("Driver đã khởi tạo thành công với UDID: %s", desired_caps.get("udid"))
        return driver
    except json.JSONDecodeError as e:
        logging.error(f"Lỗi định dạng JSON trong config.json: {e}, Nội dung: {content}")
        raise
    except Exception as e:
        logging.error(f"Lỗi khi kết nối driver: {e}")
        raise
