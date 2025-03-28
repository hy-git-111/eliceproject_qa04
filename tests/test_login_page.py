from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementNotSelectableException
from selenium import webdriver
from src.utils.helpers import WebUtils
from src.pages.login_page import LoginPage
from src.utils.directory_util import Directories
from src.resources.testdata.locators import LOCATORS, EXPECTED_TEXTS
from functools import wraps

import time
import pytest
import logging
import datetime
import os


class TestLoginPage:
    # 로그 레벨 DEBUG: 10 / INFO: 20 / WARNING: 30 / ERROR: 40 / CRITICAL: 50
    # 로그파일 설정
    dir_util = Directories()
    file_name = datetime.date.today().strftime("%Y%m%d") + ".txt"
    log_file = dir_util.logs_path(file_name)
    log_dir = dir_util.logs_path("")

    # 루트로거대신 myTestLogger 생성
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger("myTestLogger")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s : %(levelname)s - %(message)s")   # 핸들러를 사용하기 위한 포메터

    fh = logging.FileHandler(log_file, mode="a", encoding="utf-8")  # 파일핸들러 : 로깅 출력을 디스크 파일로 보냄
    fh.setFormatter(formatter)

    ch = logging.StreamHandler()    # 소켓 핸들러 : 로깅 출력을 네트워크 소켓에 보냄
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    # 래퍼함수
    def action_exception(test_func):
        func_name = test_func.__name__  # wraper 실행 시 내부 wrapper에 의해 name 속성이 변경되므로, wraper함수 호출 전에 메서드명을 정의

        @wraps(test_func)
        def wrapper(self, **kwargs):
            try:
                logger = logging.getLogger("myTestLogger")
                driver = kwargs.get("driver", None)
                logger.info(f"{func_name} - 테스트 완료")
                return test_func(self, **kwargs)
# 시간나면 중복코드 최소화하기
            except AssertionError as e:
                driver.save_screenshot(self.dir_util.screenshots_path(f"{func_name}_AssertionError.png"))
                print(driver.current_url)
                logger.error(f"{func_name} - {e}")
                raise

            except NoSuchElementException as e:
                driver.save_screenshot(self.dir_util.screenshots_path(f"{func_name}_NoSuchElementException.png"))
                logger.error(f"{func_name} - {e}")
                raise

            except TimeoutException as e:
                driver.save_screenshot(self.dir_util.screenshots_path(f"{func_name}_TimeoutException.png"))
                logger.error(f"{func_name} - {e}")
                raise

            except StaleElementReferenceException as e:
                driver.save_screenshot(self.dir_util.screenshots_path(f"{func_name}_InvalidElementStateException.png"))
                logger.error(f"{func_name} - StaleElementReferenceException")
                raise

            except ElementNotSelectableException as e:
                driver.save_screenshot(self.dir_util.screenshots_path(f"{func_name}_ElementNotSelectableException.png"))
                logger.error(f"{func_name} - {e}")
                raise

            except Exception as e:
                driver.save_screenshot(self.dir_util.screenshots_path(f"{func_name}_Other_Exception.png"))
                logger.error(f"{func_name} - Other Exception: {e}")
                raise

        return wrapper
    
    # 헬퍼함수 / elems = [d,d,d,d] 선언하고 사용
    def check_elem_exist(self, driver, elems):
        elements = []
        for elem in elems:
            locator = LOCATORS.get(elem)
            element = driver.find_element(*locator)
            elements.append(element)
        return elements
        
    def extract_elem_text(self, title_elems):
        texts = []
        for elem in title_elems:
            texts.append(elem.text)
        return texts

    def extract_expected_text(self, keys):
        titles = []
        for key in keys:
            text = EXPECTED_TEXTS.get(key)
            titles.append(text)
            print(titles)
        return titles
        

# [로그인 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    @action_exception
    def test_login_001(self, driver):
        web_utils = WebUtils(driver)
        web_utils.open_url()    # 웹사이트 진입

        confirm_titles = ["login_pg_title", "login_pg_title_sub"]   # 타이틀 확인
        title_elems = self.check_elem_exist(driver, confirm_titles)
        titles = self.extract_elem_text(title_elems)
        expected_titles = self.extract_expected_text(confirm_titles)

        assert titles == expected_titles
       
        confirm_btns = ["login_pg_login_btn", "login_pg_signin_btn"] # 버튼 확인
        btn_elems = self.check_elem_exist(driver, confirm_btns)

        assert btn_elems != None

# [로그인 정보 입력 페이지] UI확인
    @pytest.mark.skip(reason="test pass")
    @action_exception
    def test_login_002(self, driver):
        web_utils = WebUtils(driver)
        web_utils.open_url()    # 웹사이트 진입
        
        locator = LOCATORS.get("login_pg_login_btn")
        web_utils.click_element(*locator)   # 로그인 버튼 클릭

        confirm_titles = ["login_input_pg_title", "login_input_pg_title_sub"]   # 타이틀 확인
        title_elems = self.check_elem_exist(driver, confirm_titles)
        titles = self.extract_elem_text(title_elems)
        expected_titles = self.extract_expected_text(confirm_titles)

        assert titles == expected_titles

        confirm_input = ["login_input_pg_input_email", "login_input_pg_input_pwd"]  # input box 확인
        input_elems = self.check_elem_exist(driver, confirm_input)

        assert input_elems != None

        confirm_placeholders = ["login_input_pg_placeholder_email", "login_input_pg_placeholder_pwd"]   # placeholder 확인
        placeholder_elem = self.check_elem_exist(driver, confirm_placeholders)
        placeholders = self.extract_elem_text(placeholder_elem)
        expected_placeholders = self.extract_expected_text(confirm_placeholders)

        assert placeholders == expected_placeholders

# [로그인 정보 입력 페이지] UI확인
    @pytest.mark.skip(reason="test pass")
    @action_exception
    def test_login_003(self, driver):
        web_utils = WebUtils(driver)
        web_utils.open_url()    # 웹사이트 진입

        locator_btn_login = LOCATORS.get("login_pg_login_btn")
        web_utils.click_element(*locator_btn_login)   # "로그인 하기 버튼" 클릭

        locator_link_reset = LOCATORS.get("login_input_pg_link_reset_pwd")
        web_utils.click_element(*locator_link_reset)    # '비밀번호를 잊으셨나요? 링크' 클릭

        confirm_titles = ["pwd_reset_pg_title", "pwd_reset_pg_title_sub"]   # 타이틀 확인
        title_elems = self.check_elem_exist(driver, confirm_titles)
        titles = self.extract_elem_text(title_elems)
        expected_titles = self.extract_expected_text(confirm_titles)

        assert titles == expected_titles

        confirm_input = ["pwd_reset_pg_placeholder_email"]  # input box 확인
        input_elems = self.check_elem_exist(driver, confirm_input)

        assert input_elems != None

        confirm_placeholders = ["pwd_reset_pg_placeholder_email"]   # placeholder 확인
        placeholder_elem = self.check_elem_exist(driver, confirm_placeholders)
        placeholders = self.extract_elem_text(placeholder_elem)
        expected_placeholders = self.extract_expected_text(confirm_placeholders)

        assert placeholders == expected_placeholders

        confirm_btns = ["pwd_reset_pg_btn_continue", "pwd_reset_pg_link_login"] # 버튼 확인
        btn_elem = self.check_elem_exist(driver, confirm_btns)

        assert btn_elem != None
        
# [이메일 전송 완료 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    @action_exception
    def test_login_004(self, driver):
        web_utils = WebUtils(driver)
        login_page = LoginPage(driver)
        web_utils.open_url()    # 웹사이트 진입

        web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # "로그인 하기 버튼" 클릭

        web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    # '비밀번호를 잊으셨나요? 링크' 클릭

        login_page.input_email(*LOCATORS.get("pwd_reset_pg_input_email"))
        web_utils.click_element(*LOCATORS.get("pwd_reset_pg_btn_continue"))    # 이메일 전송

        confirm_titles = ["send_mail_pg_title", "send_mail_pg_title_sub"]   # 타이틀 확인
        title_elems = self.check_elem_exist(driver, confirm_titles)
        titles = self.extract_elem_text(title_elems)
        expected_titles = self.extract_expected_text(confirm_titles)

        assert titles == expected_titles

        confirm_btns = ["send_mail_pg_btn_resend"]  # 버튼 확인
        btn_elem = self.check_elem_exist(driver, confirm_btns)

        assert btn_elem != None

# TC LOGIN-005 누락

# [회원가입 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    @action_exception
    def test_login_006(self, driver):
        web_utils = WebUtils(driver)

        web_utils.open_url()    # 웹사이트 진입

        web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   # "회원가입 버튼" 클릭

        confirm_titles = ["signin_pg_title", "signin_pg_title_sub"]   # 타이틀 확인
        title_elems = self.check_elem_exist(driver, confirm_titles)
        titles = self.extract_elem_text(title_elems)
        expected_titles = self.extract_expected_text(confirm_titles)

        assert titles == expected_titles

        confirm_input = ["signin_pg_input_email", "signin_pg_input_pwd"]  # input box 확인
        input_elems = self.check_elem_exist(driver, confirm_input)

        assert input_elems != None

        confirm_placeholders = ["signin_pg_placeholder_email", "signin_pg_placeholder_pwd"]   # placeholder 확인
        placeholder_elem = self.check_elem_exist(driver, confirm_placeholders)
        placeholders = self.extract_elem_text(placeholder_elem)
        expected_placeholders = self.extract_expected_text(confirm_placeholders)

        assert placeholders == expected_placeholders

        cofirm_btns = ["signin_pg_pg_btn_continue", "signin_pg_link_login"]
        btns_elems = self.check_elem_exist(driver, cofirm_btns)
        
        assert btns_elems != None

# [로그인 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    @action_exception
    def test_login_010(self, driver):
        web_utils = WebUtils(driver)

        web_utils.open_url()    # 웹사이트 진입

        time.sleep(1)   # 없으면 에러남
        assert "signin" in driver.current_url

# [로그인 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    @action_exception
    def test_login_011(self, driver):
        web_utils = WebUtils(driver)

        web_utils.open_url()    # 웹사이트 진입
        
        locator = LOCATORS.get("login_pg_login_btn")
        web_utils.click_element(*locator)   # 로그인 버튼 클릭

        time.sleep(1)   # 없으면 오류남
        assert "login?" in driver.current_url

# TC LOGIN-012 ~ LOGIN-013 누락

# [로그인 정보 입력 페이지] 로그인
    @pytest.mark.skip(reason="test pass")
    @action_exception
    def test_login_014(self, driver):
        web_utils = WebUtils(driver)
        web_utils.open_url()    # 웹사이트 진입
        
        locator = LOCATORS.get("login_pg_login_btn")
        web_utils.click_element(*locator)   # 로그인 버튼 클릭

        web_utils.login()   # 로그인
        time.sleep(1)

        assert not "login" in driver.current_url and not "signin" in driver.current_url

# [비밀번호 초기화 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    @action_exception
    def test_login_015(self, driver):
        web_utils = WebUtils(driver)
        web_utils.open_url()    # 웹사이트 진입

        locator_btn_login = LOCATORS.get("login_pg_login_btn")
        web_utils.click_element(*locator_btn_login)   # "로그인 하기 버튼" 클릭

        locator_link_reset = LOCATORS.get("login_input_pg_link_reset_pwd")
        web_utils.click_element(*locator_link_reset)    # '비밀번호를 잊으셨나요? 링크' 클릭

        assert "reset-password/request" in driver.current_url

# TC LOGIN-016 누락

# 이메일 재 전송
    @pytest.mark.skip(reason="test fail")
    @action_exception
    def test_login_017(self, driver):
        web_utils = WebUtils(driver)
        login_page = LoginPage(driver)
        web_utils.open_url()    # 웹사이트 진입

        web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # "로그인 하기 버튼" 클릭

        web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    # '비밀번호를 잊으셨나요? 링크' 클릭

        login_page.input_email(*LOCATORS.get("pwd_reset_pg_input_email"))
        web_utils.click_element(*LOCATORS.get("pwd_reset_pg_btn_continue"))    # 이메일 전송
        
        web_utils.click_element(*LOCATORS.get("send_mail_pg_btn_resend"))   # 이메일 재 전송
        time.sleep(1)

        confirm_input_value = driver.find_element(*LOCATORS.get("pwd_reset_pg_input_email")).get_attribute("value")
        
        assert confirm_input_value == ""

# TC LOGIN-018 ~ LOGIN-019 누락

# [비밀번호 초기화 페이지]에서 [로그인 정보 입력 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    @action_exception
    def test_login_020(self, driver):
        web_utils = WebUtils(driver)

        web_utils.open_url()    # 웹사이트 진입

        web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # "로그인 하기 버튼" 클릭

        web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    # '비밀번호를 잊으셨나요? 링크' 클릭

        web_utils.click_element(*LOCATORS.get("pwd_reset_pg_link_login"))   #  '로그인 화면으로 돌아가기 링크' 클릭

        time.sleep(1)   # 없으면 에러남
        assert "login?" in driver.current_url

# [로그인 정보 입력 페이지]에서 [회원가입 페이지]로 이동 확인
    @pytest.mark.skip(reason="test pass")
    @action_exception
    def test_login_021(self, driver):
        web_utils = WebUtils(driver)

        web_utils.open_url()    # 웹사이트 진입

        web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # "로그인 하기 버튼" 클릭

        web_utils.click_element(*LOCATORS.get("login_input_pg_link_signin"))    # '회원가입 링크' 클릭

        time.sleep(1)   # 없으면 에러남
        assert "signup?" in driver.current_url

# [로그인 페이지]에서 [회원가입 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    @action_exception
    def test_login_022(self, driver):
        web_utils = WebUtils(driver)

        web_utils.open_url()    # 웹사이트 진입

        web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   # "회원가입 버튼" 클릭

        time.sleep(1)   # 없으면 에러남
        assert "signup?" in driver.current_url

# [로그인 페이지]에서 [회원가입 페이지] 진입 확인 >> 미완료
    @pytest.mark.skip(reason="test pass")
    @action_exception
    def test_login_023(self, driver):
        web_utils = WebUtils(driver)
        login_page = LoginPage(driver)

        web_utils.open_url()    # 웹사이트 진입

        web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   # "회원가입 버튼" 클릭

        login_page.input_password