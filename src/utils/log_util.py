import os
import logging
import datetime
import inspect
from src.utils.directory_util import Directories

class LogUtils:
    directories = Directories()
    
    @staticmethod
    def get_log_file():
        stack = inspect.stack()
        for frame in stack:
            if "test_" in frame.filename:
                test_filename = os.path.basename(frame.filename).replace(".py", ".log")
                return LogUtils.directories.logs_path(test_filename)
        return LogUtils.directories.logs_path("default.log")
    
    @staticmethod
    def setup_logger():
        logger = logging.getLogger(__name__)  # 🔥 전역 로거 사용
        log_file = LogUtils.get_log_file()
        
        if logger.hasHandlers():  
            logger.handlers.clear()  # 🔥 기존 핸들러 삭제 (중복 방지)
        
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        return logger
    
    @staticmethod
    def log_success():
        logger = LogUtils.setup_logger()
        function_name = LogUtils.get_test_function_name()
        log_message = f"✅ {function_name} 성공"
        logger.info(log_message)
        print(log_message)
    
    @staticmethod
    def log_error(error, driver=None):
        logger = LogUtils.setup_logger()
        function_name = LogUtils.get_test_function_name()
        error_message = str(error)
        log_message = f"❌ {function_name} - {error_message}"
        logger.error(log_message)
        print(log_message)
        
        if driver:
            LogUtils.save_screenshot(driver, function_name)
    
    @staticmethod
    def save_screenshot(driver, function_name):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{function_name}_{timestamp}.png"
        screenshot_path = LogUtils.directories.screenshots_path(screenshot_name)
        driver.save_screenshot(screenshot_path)
        print(f"📸 스크린샷 저장: {screenshot_path}")
    
    @staticmethod
    def get_test_function_name():
        stack = inspect.stack()
        for frame in stack:
            if frame.function.startswith("test_"):
                return frame.function
        return "unknown_test"
