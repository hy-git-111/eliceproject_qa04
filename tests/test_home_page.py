import pytest
import logging
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.utils.helpers import WebUtils
from src.utils.directory_util import Directories
from src.pages.home_page import HomePage


# 로그 설정
logger = logging.getLogger(__name__)
if not logger.handlers:  # 중복 방지
    logger.setLevel(logging.INFO)
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    log_file = Directories().logs_path("test_home_page.log")
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)


@pytest.mark.usefixtures("driver")
class TestHomePage(Directories):
    header_title_css_selector = "header span.text-title"
    
    def test_home_001(self, driver: WebDriver):
        try:
            logger.info("테스트 시작: HOME-001")

            self.open_url()
            self.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.header_title_css_selector))
            )

            header_title = driver.find_element(By.CSS_SELECTOR, self.header_title_css_selector)
            assert "오늘 뭐 먹지 ?" == header_title.text.strip()

            time.sleep(15)
            logger.info("✅ HOME-001 테스트 성공")

        except AssertionError:
            screenshot_path = self.screenshots_path("HOME-001 실패_AssertionError.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"🚨 [ERROR] AssertionError 발생 - 스크린샷 저장: {screenshot_path}")

        except TimeoutException:
            screenshot_path = self.screenshots_path("HOME-001 실패_Timeout.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"⏳ [ERROR] Timeout 발생 - 스크린샷 저장: {screenshot_path}", exc_info=True)

        except NoSuchElementException:
            screenshot_path = self.screenshots_path("HOME-001 실패_NoSuchElement.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"🔍 [ERROR] 요소 없음 - 스크린샷 저장: {screenshot_path}", exc_info=True)

        except Exception:
            screenshot_path = self.screenshots_path("HOME-001 실패_Others.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"❗ [ERROR] 알 수 없는 예외 발생 - 스크린샷 저장: {screenshot_path}", exc_info=True)