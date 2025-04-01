import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder


class ActionElement:
    def __init__(self, driver ):
        self.driver = driver

    def find_the_element(self, locator):
        try:
            return WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(locator)
            )
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while finding the element: {e}")
            raise

    def click_element(self, locator):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while clicking the element: {e}")
            raise
    
    def send_keys_element(self, locator, value):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(locator)
            ).send_keys(value)
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while sending keys to the element: {e}")
            raise

    def scroll_to_element(self, locator):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", locator)
        except (NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException) as e:
            logging.error(f"An error occurred while scrolling to the element: {e}")
            raise
    
    def get_text_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(locator)
            )
            return element.text
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while getting text from the element: {e}")
            raise

    def get_attribute_element(self, locator, attribute):
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(locator)
            )
            return element.get_attribute(attribute)
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while getting attribute from the element: {e}")
            raise

    def scroll_up(self):
        size = self.driver.get_window_size()
        start_y = int(size['height'] * 0.8)
        end_y = int(size['height'] * 0.2)
        start_x = int(size['width'] * 0.5)
        pointer = PointerInput(interaction.POINTER_TOUCH, "touch")
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=pointer)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y).pointer_down().pause(0.5).move_to_location(start_x, end_y).pointer_up()
        actions.perform()
        logging.info("Đã cuộn màn hình lên trên")

    def scroll_down(self):
        try:
            size = self.driver.get_window_size()
            start_y = int(size['height'] * 0.2)
            end_y = int(size['height'] * 0.8)
            start_x = int(size['width'] * 0.5)
            logging.debug(f"Kích thước màn hình: {size}")
            logging.debug(f"Cuộn từ (x,y): ({start_x}, {start_y}) đến ({start_x}, {end_y})")
            pointer = PointerInput(interaction.POINTER_TOUCH, "touch")
            actions = ActionChains(self.driver)
            action_builder = ActionBuilder(self.driver, mouse=pointer)
            action_builder.pointer_action.move_to_location(start_x, start_y)
            action_builder.pointer_action.pointer_down()
            action_builder.pointer_action.pause(0.5)
            action_builder.pointer_action.move_to_location(start_x, end_y)
            action_builder.pointer_action.pointer_up()
            actions.w3c_actions = action_builder
            actions.perform()
            logging.info("Đã cuộn màn hình xuống dưới thành công.")
        except Exception as e:
            logging.error(f"Lỗi khi cuộn màn hình xuống dưới: {e}", exc_info=True)
            raise