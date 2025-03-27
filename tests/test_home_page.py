import pytest
import logging
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


# 테스트. 추후 EXCEPTION 처리하는 공통 함수 추가 예정
@pytest.mark.usefixtures("driver")
class TestHomePage(Directories):
    header_title_css_selector = "header span.text-title"
    
    def test_home_001(self, driver: WebDriver):
        try:
            logger.info("테스트 시작: HOME-001")

            web_utils = WebUtils(driver)

            web_utils.open_url()
            web_utils.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.header_title_css_selector))
            )

            header_title = driver.find_element(By.CSS_SELECTOR, self.header_title_css_selector)
            assert "오늘 뭐 먹지 ?" == header_title.text.strip()

            # ui 전부 추가 필요

            logger.info("✅ HOME-001 테스트 성공")

        except AssertionError:
            screenshot_path = self.screenshots_path("HOME_001_Fail_AssertionError.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"🚨 [ERROR] AssertionError 발생 - 스크린샷 저장: {screenshot_path}")

        except TimeoutException:
            screenshot_path = self.screenshots_path("HOME_001_Fail_Timeout.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"⏳ [ERROR] Timeout 발생 - 스크린샷 저장: {screenshot_path}", exc_info=True)

        except NoSuchElementException:
            screenshot_path = self.screenshots_path("HOME_001_Fail_NoSuchElement.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"🔍 [ERROR] 요소 없음 - 스크린샷 저장: {screenshot_path}", exc_info=True)

        except Exception:
            screenshot_path = self.screenshots_path("HOME_001_Fail_Others.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"❗ [ERROR] 알 수 없는 예외 발생 - 스크린샷 저장: {screenshot_path}", exc_info=True)


    def test_home_003(self, driver: WebDriver):
        try:
            logger.info("테스트 시작: HOME-003")

            web_utils = WebUtils(driver)
            home = HomePage(driver)

            web_utils.open_url()
            web_utils.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, HomePage.eat_alone_btn_css_selector))
            )

            home.open_eat_alone()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/header/div/svg'))
            )

            web_utils.click_back()
            assert "https://kdt-pt-1-pj-2-team03.elicecoding.com/" == driver.current_url

            logger.info("✅ HOME-003 테스트 성공")

        except AssertionError:
            screenshot_path = self.screenshots_path("HOME_001_Fail_AssertionError.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"🚨 [ERROR] AssertionError 발생 - 스크린샷 저장: {screenshot_path}")

        except TimeoutException:
            screenshot_path = self.screenshots_path("HOME_001_Fail_Timeout.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"⏳ [ERROR] Timeout 발생 - 스크린샷 저장: {screenshot_path}", exc_info=True)

        except NoSuchElementException:
            screenshot_path = self.screenshots_path("HOME_001_Fail_NoSuchElement.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"🔍 [ERROR] 요소 없음 - 스크린샷 저장: {screenshot_path}", exc_info=True)

        except Exception:
            screenshot_path = self.screenshots_path("HOME_001_Fail_Others.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"❗ [ERROR] 알 수 없는 예외 발생 - 스크린샷 저장: {screenshot_path}", exc_info=True)