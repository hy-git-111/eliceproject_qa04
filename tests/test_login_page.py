from src.utils.helpers import WebUtils, CheckElement
from src.pages.login_page import LoginPage
from src.resources.testdata.locators import LOCATORS
from src.utils.log_util import LogUtils
from functools import wraps

import time
import pytest

@pytest.mark.usefixtures("driver")
class TestLoginPage:
# [로그인 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_001(self, driver):
        try:
            web_utils = WebUtils(driver)
            check_elems = CheckElement(driver)

            titles_keys = ["login_pg_title", "login_pg_title_sub"]
            btns_keys = ["login_pg_login_btn", "login_pg_signin_btn"]

            web_utils.open_url()    # 웹사이트 진입

            titles_elems = check_elems.existence_check(driver, titles_keys)
            titles_texts = check_elems.get_elems_texts(titles_elems)
            btns_elemss = check_elems.existence_check(btns_keys)

            expected_texts = check_elems.get_expected_texts(titles_keys)

            assert titles_texts != expected_texts
            assert btns_elemss != None

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 정보 입력 페이지] UI확인
    @pytest.mark.skip(reason="test pass")
    def test_login_002(self, driver):
        try:
            web_utils = WebUtils(driver)
            check_elems = CheckElement(driver)

            titles_keys = ["login_input_pg_title", "login_input_pg_title_sub"]
            input_boxes_keys = ["login_input_pg_input_email", "login_input_pg_input_pwd"]
            placeholders_keys = ["login_input_pg_placeholder_email", "login_input_pg_placeholder_pwd"]

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # 로그인 버튼 클릭

            titles_elems = check_elems.existence_check(titles_keys)
            titles = check_elems.get_elems_texts(titles_elems)

            input_boxes_elems = check_elems.existence_check(input_boxes_keys)

            placeholders_elems = check_elems.existence_check(placeholders_keys)
            placeholders = check_elems.get_elems_texts(placeholders_elems)

            expected_titles = check_elems.get_expected_texts(titles_keys)
            expected_placeholders = check_elems.get_expected_texts(placeholders_keys)

            assert titles == expected_titles
            assert input_boxes_elems != None
            assert placeholders == expected_placeholders

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 정보 입력 페이지] UI확인
    @pytest.mark.skip(reason="test pass")
    def test_login_003(self, driver):
        try:
            web_utils = WebUtils(driver)
            check_elems = CheckElement(driver)

            titles_keys = ["pwd_reset_pg_title", "pwd_reset_pg_title_sub"]
            input_box_key = ["pwd_reset_pg_placeholder_email"]
            placeholder_key = ["pwd_reset_pg_placeholder_email"]
            btns_keys = ["pwd_reset_pg_btn_continue", "pwd_reset_pg_link_login"]

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # "로그인 하기 버튼" 클릭
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    # '비밀번호를 잊으셨나요? 링크' 클릭

            titles_elems = check_elems.existence_check(driver, titles_keys)
            titles = check_elems.get_elems_texts(titles_elems)

            input_boxes_elems = check_elems.existence_check(driver, input_box_key)

            placeholders_elems = check_elems.existence_check(driver, placeholder_key)
            placeholders = check_elems.get_elems_texts(placeholders_elems)

            btns_elems = check_elems.existence_check(driver, btns_keys)

            expected_titles = check_elems.get_expected_texts(titles_keys)
            expected_placeholders = check_elems.get_expected_texts(placeholder_key)

            assert titles == expected_titles
            assert input_boxes_elems != None
            assert placeholders == expected_placeholders
            assert btns_elems != None

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [이메일 전송 완료 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_004(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            check_elems = CheckElement(driver)

            titles_keys = ["send_mail_pg_title", "send_mail_pg_title_sub"]
            btn_key = ["send_mail_pg_btn_resend"]

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # "로그인 하기 버튼" 클릭
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    # '비밀번호를 잊으셨나요? 링크' 클릭

            login_page.input_email(*LOCATORS.get("pwd_reset_pg_input_email"))
            web_utils.click_element(*LOCATORS.get("pwd_reset_pg_btn_continue"))    # 이메일 전송

            titles_elems = check_elems.existence_check(driver, titles_keys)
            titles = check_elems.get_elems_texts(titles_elems)
            expected_titles = check_elems.get_expected_texts(titles_keys)

            btns_elems = check_elems.existence_check(driver, btn_key)

            assert titles == expected_titles
            assert btns_elems != None

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# TC LOGIN-005 누락

# [회원가입 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_006(self, driver):
        try:
            web_utils = WebUtils(driver)
            check_elems = CheckElement(driver)

            titles_keys = ["signin_pg_title", "signin_pg_title_sub"]   # 타이틀 확인
            input_boxes_keys = ["signin_pg_input_email", "signin_pg_input_pwd"]  # input box 확인
            placeholders_keys = ["signin_pg_placeholder_email", "signin_pg_placeholder_pwd"]   # placeholder 확인
            btns_keys = ["signin_pg_pg_btn_continue", "signin_pg_link_login"]

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   # "회원가입 버튼" 클릭

            titles_elems = check_elems.existence_check(driver, titles_keys)
            titles = check_elems.get_elems_texts(titles_elems)

            input_boxes_elems = check_elems.existence_check(driver, input_boxes_keys)

            placeholders_elems = check_elems.existence_check(driver, placeholders_keys)
            placeholders = check_elems.get_elems_texts(placeholders_elems)

            btns_elems = check_elems.existence_check(driver, btns_keys)

            expected_placeholders = check_elems.get_expected_texts(placeholders_keys)
            expected_titles = check_elems.get_expected_texts(titles_keys)
            
            assert titles == expected_titles
            assert input_boxes_elems != None
            assert placeholders == expected_placeholders
            assert btns_elems != None

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_010(self, driver):
        try:
            web_utils = WebUtils(driver)

            web_utils.open_url()    # 웹사이트 진입

            time.sleep(1)   # 없으면 에러남
            assert "signin" in driver.current_url
            
        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_011(self, driver):
        try:
            web_utils = WebUtils(driver)

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # 로그인 버튼 클릭

            time.sleep(1)   # 없으면 오류남
            assert "login?" in driver.current_url

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# TC LOGIN-012 ~ LOGIN-013 누락

# [로그인 정보 입력 페이지] 로그인
    @pytest.mark.skip(reason="test pass")
    def test_login_014(self, driver):
        try:
            web_utils = WebUtils(driver)

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # 로그인 버튼 클릭

            web_utils.login()   # 로그인
            time.sleep(1)

            assert not "login" in driver.current_url and not "signin" in driver.current_url   

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise                      

# [비밀번호 초기화 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_015(self, driver):
        try:
            web_utils = WebUtils(driver)

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # "로그인 하기 버튼" 클릭
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    # '비밀번호를 잊으셨나요? 링크' 클릭

            assert "reset-password/request" in driver.current_url
        
        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# TC LOGIN-016 누락

# 이메일 재 전송
    @pytest.mark.skip(reason="test fail")
    def test_login_017(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # "로그인 하기 버튼" 클릭
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    # '비밀번호를 잊으셨나요? 링크' 클릭

            login_page.input_email(*LOCATORS.get("pwd_reset_pg_input_email"))
            web_utils.click_element(*LOCATORS.get("pwd_reset_pg_btn_continue"))    # 이메일 전송
            
            web_utils.click_element(*LOCATORS.get("send_mail_pg_btn_resend"))   # 이메일 재 전송

            input_boxes_keys_value = driver.find_element(*LOCATORS.get("pwd_reset_pg_input_email")).get_attribute("value")
            
            assert input_boxes_keys_value == ""

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# TC LOGIN-018 ~ LOGIN-019 누락

# [비밀번호 초기화 페이지]에서 [로그인 정보 입력 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_020(self, driver):
        try:
            web_utils = WebUtils(driver)

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # "로그인 하기 버튼" 클릭
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    # '비밀번호를 잊으셨나요? 링크' 클릭
            
            web_utils.click_element(*LOCATORS.get("pwd_reset_pg_link_login"))   #  '로그인 화면으로 돌아가기 링크' 클릭

            time.sleep(1)   # 없으면 에러남
            assert "login?" in driver.current_url

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 정보 입력 페이지]에서 [회원가입 페이지]로 이동 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_021(self, driver):
        try:
            web_utils = WebUtils(driver)

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # "로그인 하기 버튼" 클릭
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_signin"))    # '회원가입 링크' 클릭

            time.sleep(1)   # 없으면 에러남
            assert "signup?" in driver.current_url

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 페이지]에서 [회원가입 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_022(self, driver):
        try:
            web_utils = WebUtils(driver)

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   # "회원가입 버튼" 클릭

            time.sleep(1)   # 없으면 에러남
            assert "signup?" in driver.current_url
            
        except Exception as e:
                LogUtils.log_error(e, driver)
                raise

# [회원가입 페이지] 비밀번호 입력
    @pytest.mark.skip(reason="test pass")
    def test_login_025(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            check_elems = CheckElement(driver)

            text_section_key = "signin_pg_pw_rule_section"
            rules_keys = ["signin_pg_pw_rule_title", "signin_pg_pw_rule_char_num", "signin_pg_pw_rule_following", 
                          "signin_pg_pw_rule_following_Lower_letters", "signin_pg_pw_rule_following_upper_letters",
                          "signin_pg_pw_rule_following_num", "signin_pg_pw_rule_following_special_char"]
            
            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   # "회원가입 버튼" 클릭
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"))  # 비밀번호 입력

            rules = check_elems.get_texts_for_children(text_section_key, rules_keys)
            
            expected_rules = check_elems.get_expected_texts(rules_keys)

            assert rules == expected_rules

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [회원가입 페이지] 비밀번호 입력
    #@pytest.mark.skip(reason="test pass")
    def test_login_026(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            check_elems = CheckElement(driver)

            text_section_key = "signin_pg_pw_rule_section"
            rules_keys = ["signin_pg_pw_rule_title", "signin_pg_pw_rule_char_num", "signin_pg_pw_rule_following", 
                          "signin_pg_pw_rule_following_Lower_letters", "signin_pg_pw_rule_following_upper_letters",
                          "signin_pg_pw_rule_following_num", "signin_pg_pw_rule_following_special_char"]
            
            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   # "회원가입 버튼" 클릭
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"))  # 비밀번호 입력

            rules = check_elems.get_texts_for_children(text_section_key, rules_keys)

            expected_rules = check_elems.get_expected_texts(rules_keys)

            assert rules == expected_rules

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
