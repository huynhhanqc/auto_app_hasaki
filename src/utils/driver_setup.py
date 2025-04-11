import json
import os
from appium import webdriver
import logging
from appium.webdriver.webdriver import AppiumOptions

logging.basicConfig(filename="logs/test_log.log", level=logging.ERROR)

def setup_driver():
    config_path = os.path.join(os.path.dirname(__file__), "../config/config.json")
    logging.info(f"Reading config file from: {config_path}")
    if not os.path.exists(config_path):
        logging.error(f"Config file config.json does not exist at: {config_path}")
        raise FileNotFoundError(f"Config file config.json does not exist at: {config_path}")
    if not os.access(config_path, os.R_OK):
        logging.error(f"No read permission for config file config.json at: {config_path}")
        raise PermissionError(f"No read permission for config file config.json at: {config_path}")
    try:
        with open(config_path, "r") as file:
            content = file.read().strip()
            logging.info(f"Content of config.json file: {content}")
            desired_caps = json.loads(content)
        if desired_caps is None or not isinstance(desired_caps, dict):
            logging.error(f"Invalid desired_caps: {desired_caps}, type: {type(desired_caps)}")
            raise ValueError(f"Invalid desired_caps: {desired_caps}")
        required_keys = ["platformName", "appium:udid", "appium:appPackage"]
        missing_keys = [key for key in required_keys if key not in desired_caps]
        if missing_keys:
            logging.error(f"Missing required keys in config.json: {missing_keys}")
            raise ValueError(f"Missing required keys: {missing_keys}")
        logging.info(f"Configuration loaded: {desired_caps}")
        appium_options = AppiumOptions()
        appium_options.load_capabilities(desired_caps)
        driver = webdriver.Remote("http://localhost:4723", options=appium_options)
        logging.info("Driver initialized successfully with UDID: %s", desired_caps.get("udid"))
        return driver
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error in config.json: {e}, Content: {content}")
        raise
    except Exception as e:
        logging.error(f"Error connecting driver: {e}")
        raise
