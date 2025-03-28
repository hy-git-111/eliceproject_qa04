import datetime
import logging
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.utils.helpers import WebUtils
from src.pages.home_page import HomePage, SelectOptionPage, RecommendationPage
from src.utils.directory_util import Directories


# 로그 설정
logger = logging.getLogger(__name__)
if not logger.handlers:  # 로그 파일 중복 생성 방지
    logger.setLevel(logging.INFO)
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    log_file = Directories().logs_path("test_home_page.log")
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)


# 예외 처리
def handle_exception(driver: WebDriver, exception: Exception, request):
    test_name = request.node.name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = Directories().screenshots_path(f"{test_name}_Fail_{timestamp}_{exception.__class__.__name__}.png")
    driver.save_screenshot(screenshot_path)
    
    if isinstance(exception, AssertionError):
        logger.error(f"🚨 [ERROR] AssertionError 발생 - 스크린샷 저장: {screenshot_path}", exc_info=True)
    elif isinstance(exception, TimeoutException):
        logger.error(f"⏳ [ERROR] Timeout 발생 - 스크린샷 저장: {screenshot_path}", exc_info=True)
    elif isinstance(exception, NoSuchElementException):
        logger.error(f"🔍 [ERROR] 요소 없음 - 스크린샷 저장: {screenshot_path}", exc_info=True)
    else:
        logger.error(f"❗ [ERROR] 알 수 없는 예외 발생 - 스크린샷 저장: {screenshot_path}", exc_info=True)

    logger.error(f"❌ {test_name} 테스트 실패")


# 로그 기록
@pytest.fixture(autouse=True)
def log_test_start_and_end(request):
    test_name = request.node.name
    logger.info(f"➡️ {test_name} 테스트 시작")
    
    try:
        yield
    except Exception as e:
        handle_exception(request.node.driver, e, test_name)
    finally:
        outcome = request.node._store.get("outcome", None)  # 실행 결과 가져오기
        if outcome and outcome.failed:
            return
        logger.info(f"✅ {test_name} 테스트 성공")


# 테스트 시작
@pytest.mark.usefixtures("driver")
class TestHomePage(Directories):
    header_title_css_selector = "header span.text-title"
    
    @pytest.mark.skip
    def test_home_001(self, driver: WebDriver, request):
        try:
            web_utils = WebUtils(driver)

            web_utils.open_url()
            web_utils.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.header_title_css_selector))
            )

            header_title = driver.find_element(By.CSS_SELECTOR, self.header_title_css_selector)
            assert "오늘 뭐먹지 ?" == header_title.text.strip()
            print("HOME-001 UI 검증 1/12 성공")

            # ui 전부 추가 필요 & UI 검증하는 TC 002, 006, 011, 017, 022, 026 추가 필요

        except Exception as e:
            handle_exception(driver, e, request)
            raise e


    @pytest.mark.skip
    def test_home_003(self, driver: WebDriver, request):
        try:
            web_utils = WebUtils(driver)
            home = HomePage(driver)

            web_utils.open_url()
            web_utils.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.header_title_css_selector))
            )

            home.open_eat_alone()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.rounded-full.cursor-pointer'))
            )

            web_utils.click_back()
            assert "https://kdt-pt-1-pj-2-team03.elicecoding.com/" == driver.current_url
            print("HOME-003 뒤로 가기 버튼 검증 성공")

        except Exception as e:
            handle_exception(driver, e, request)
            raise e
        

    def test_home_004(self, driver: WebDriver, request):
        try:
            web_utils = WebUtils(driver)
            home = HomePage(driver)
            option = SelectOptionPage(driver)

            web_utils.open_url()
            web_utils.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_alone_btn_css_selector))
            )

            home.open_eat_alone()
            ws(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, option.dropdown_css_selector))
            )

            option.click_category_dropdown()
            options = driver.find_elements(By.CSS_SELECTOR, option.options_css_selector)

            expected_options = ["한식", "중식", "양식", "일식", "분식", "아시안", "패스트푸드", "기타"]
            actual_options = [opt.text.strip() for opt in options]
            print("actual_options:", actual_options)  # 디버깅용

            assert set(expected_options) == set(actual_options), f"드롭다운 옵션 불일치: {actual_options}"
            print("HOME-004 드롭다운 옵션 검증 성공")

        except Exception as e:
            handle_exception(driver, e, request)
            raise e
        
    
    def test_home_005(self, driver: WebDriver, request):
        try:
            web_utils = WebUtils(driver)
            home = HomePage(driver)
            option = SelectOptionPage(driver)

            web_utils.open_url()
            web_utils.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_alone_btn_css_selector))
            )

            home.open_eat_alone()
            ws(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, option.dropdown_css_selector))
            )

            option.click_category_dropdown()
            selected_option = option.click_category_dropdown_option_randomly()

            # 여기부터 수정 필요
            dropdown_button = driver.find_element(By.CSS_SELECTOR, option.dropdown_css_selector)
            selected_span = dropdown_button.find_element(By.CSS_SELECTOR, "span")
            displayed_text = selected_span.text.strip()

            assert selected_option == displayed_text, f"선택된 옵션 불일치: {selected_option} != {displayed_text}"
            print("HOME-005 드롭다운 옵션 선택 검증 성공")

            done_button = driver.find_element(By.XPATH, option.done_btn_xpath)
            assert done_button.is_enabled, "선택 완료 버튼 비활성화"
            print("HOME-005 선택 완료 버튼 활성화 검증 성공")

        except Exception as e:
            handle_exception(driver, e, request)
            raise e