import time
import pytest
from src.utils.helpers import WebUtils, VerifyHelpers
from src.pages.login_page import LoginPage
from src.pages.team_feed_page import TeamFeed
from src.utils.locators import LOCATORS
from src.resources.testdata.user_data import login_data, signin_data, unique_email
from src.utils.log_util import LogUtils

@pytest.mark.usefixtures("driver")
class TestLoginPage:
# [로그인 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_001(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            titles_keys = ["login_pg_title", "login_pg_subtitle"]
            btns_keys = ["login_pg_login_btn", "login_pg_signin_btn"]

            web_utils.open_url()    # 웹사이트 진입

            titles_elems = verify_helpers.check_existence(titles_keys)
            titles_texts = verify_helpers.get_elems_texts(titles_elems)
            btns_elemss = verify_helpers.check_existence(btns_keys)

            expected_texts = verify_helpers.get_expected_texts(titles_keys)

            assert titles_texts == expected_texts
            assert btns_elemss != None
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 정보 입력 페이지] UI확인
    @pytest.mark.skip(reason="test pass")
    def test_login_002(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            titles_keys = ["login_input_pg_title", "login_input_pg_subtitle"]
            input_boxes_keys = ["login_input_pg_input_email", "login_input_pg_input_pwd"]
            placeholders_keys = ["login_input_pg_placeholder_email", "login_input_pg_placeholder_pwd"]

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # 로그인 버튼 클릭

            titles_elems = verify_helpers.check_existence(titles_keys)
            titles = verify_helpers.get_elems_texts(titles_elems)

            input_boxes_elems = verify_helpers.check_existence(input_boxes_keys)

            placeholders_elems = verify_helpers.check_existence(placeholders_keys)
            placeholders = verify_helpers.get_elems_texts(placeholders_elems)

            expected_titles = verify_helpers.get_expected_texts(titles_keys)
            expected_placeholders = verify_helpers.get_expected_texts(placeholders_keys)

            assert titles == expected_titles
            assert input_boxes_elems != None
            assert placeholders == expected_placeholders
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [비밀번호 초기화 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_003(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            titles_keys = ["pwd_reset_pg_title", "pwd_reset_pg_subtitle"]
            input_box_key = ["pwd_reset_pg_placeholder_email"]
            placeholder_key = ["pwd_reset_pg_placeholder_email"]
            btns_keys = ["pwd_reset_pg_btn_continue", "pwd_reset_pg_link_login"]

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # "로그인 하기 버튼" 클릭
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    # '비밀번호를 잊으셨나요? 링크' 클릭

            titles_elems = verify_helpers.check_existence(titles_keys)
            titles = verify_helpers.get_elems_texts(titles_elems)

            input_boxes_elems = verify_helpers.check_existence(input_box_key)

            placeholders_elems = verify_helpers.check_existence(placeholder_key)
            placeholders = verify_helpers.get_elems_texts(placeholders_elems)

            btns_elems = verify_helpers.check_existence(btns_keys)

            expected_titles = verify_helpers.get_expected_texts(titles_keys)
            expected_placeholders = verify_helpers.get_expected_texts(placeholder_key)

            assert titles == expected_titles
            assert input_boxes_elems != None
            assert placeholders == expected_placeholders
            assert btns_elems != None
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [이메일 전송 완료 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_004(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            titles_keys = ["send_mail_pg_title", "send_mail_pg_subtitle"]
            btn_key = ["send_mail_pg_btn_resend"]

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # "로그인 하기 버튼" 클릭
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    # '비밀번호를 잊으셨나요? 링크' 클릭

            login_page.input_email(*LOCATORS.get("pwd_reset_pg_input_email"), login_data["valid_email"])
            web_utils.click_element(*LOCATORS.get("pwd_reset_pg_btn_continue"))    # 이메일 전송

            titles_elems = verify_helpers.check_existence(titles_keys)
            titles = verify_helpers.get_elems_texts(titles_elems)
            expected_titles = verify_helpers.get_expected_texts(titles_keys)

            btns_elems = verify_helpers.check_existence(btn_key)

            assert titles == expected_titles
            assert btns_elems != None
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [회원가입 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_006(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            titles_keys = ["signin_pg_title", "signin_pg_subtitle"]   # 타이틀 확인
            input_boxes_keys = ["signin_pg_input_email", "signin_pg_input_pwd"]  # input box 확인
            placeholders_keys = ["signin_pg_placeholder_email", "signin_pg_placeholder_pwd"]   # placeholder 확인
            btns_keys = ["signin_pg_pg_btn_continue", "signin_pg_link_login"]

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   # "회원가입 버튼" 클릭

            titles_elems = verify_helpers.check_existence(titles_keys)
            titles = verify_helpers.get_elems_texts(titles_elems)

            input_boxes_elems = verify_helpers.check_existence(input_boxes_keys)

            placeholders_elems = verify_helpers.check_existence(placeholders_keys)
            placeholders = verify_helpers.get_elems_texts(placeholders_elems)

            btns_elems = verify_helpers.check_existence(btns_keys)

            expected_placeholders = verify_helpers.get_expected_texts(placeholders_keys)
            expected_titles = verify_helpers.get_expected_texts(titles_keys)
            
            assert titles == expected_titles
            assert input_boxes_elems != None
            assert placeholders == expected_placeholders
            assert btns_elems != None
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [권한 요청 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_007(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)
            signin_email = unique_email()

            title_key = ["authorize_pg_title"]   # 타이틀 확인
            form_key = "authorize_pg_form"
            texts_keys = ["authorize_pg_subtitle", "authorize_pg_requested_authorize"]# "authorize_pg_email",
            btns_keys = ["authorize_pg_btn_accept", "authorize_pg_btn_decline"]
            
            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   # "회원가입 버튼" 클릭

            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_email)    # 이메일 입력

            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  # 비밀번호 입력
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue"))# "계속하기 버튼" 클릭


            titles_elems = verify_helpers.check_existence(title_key)
            title = verify_helpers.get_elems_texts(titles_elems)

            texts = verify_helpers.get_children_text(form_key, texts_keys)

            btns_elems = verify_helpers.check_children_existence(form_key, btns_keys)

            expected_title = verify_helpers.get_expected_texts(title_key)
            expected_texts = verify_helpers.get_expected_texts(texts_keys)
            
            assert title == expected_title
            assert texts == expected_texts
            assert btns_elems != None
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 오류 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_008(self, driver):
        try:

            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)
            signin_email = unique_email()

            titles_keys = ["error_pg_title", "error_pg_subtitle"]
            btn_key = ["error_pg_btn_retry"]
            
            web_utils.open_url()    # 웹사이트 진입
            
            ## 원래 코드
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   # "회원가입 버튼" 클릭
            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_email)    # 이메일 입력
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  # 비밀번호 입력
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue"))# "계속하기 버튼" 클릭

            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_decline"))  # "거절 버튼" 클릭

            titles_elems = verify_helpers.check_existence(titles_keys)
            titles = verify_helpers.get_elems_texts(titles_elems)

            btn_elem = verify_helpers.check_existence(btn_key)

            expected_titles = verify_helpers.get_expected_texts(titles_keys)

            assert titles == expected_titles
            assert btn_elem != None
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [프로필 입력 페이지] UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_009(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)
            signin_email = unique_email()

            titles_keys = ["profile_pg_title", "profile_pg_name_title", "profile_pg_team_title", 
                         "profile_pg_taste_title", "profile_pg_preference_title", 
                         "profile_pg_like_title", "profile_pg_dislike_title"]
            placeholder_key = ["profile_pg_name_placeholder"]
            drop_down_key = ["profile_pg_team_dropdown"]
            input_boxes_keys = ["profile_pg_name_input", "profile_pg_like_input", "profile_pg_dislike_input"]
            sliders_keys = ["profile_pg_taste_slider_sweetness", "profile_pg_taste_slider_salty", 
                            "profile_pg_taste_slider_spicy"]
            btn_key = ["profile_pg_btn_submit"]

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   # "회원가입 버튼" 클릭
            
            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_email)    # 이메일 입력
            time.sleep(2)
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  # 비밀번호 입력
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue")) # "계속하기 버튼" 클릭

            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_accept"))  # "승인 버튼" 클릭

            titles_elems = verify_helpers.check_existence(titles_keys)
            title = verify_helpers.get_elems_texts(titles_elems)

            placeholder_elem = verify_helpers.check_existence(placeholder_key)
            placeholder = placeholder_elem[0].get_attribute("placeholder")

            drop_down_elem = verify_helpers.check_existence(drop_down_key)
            input_boxes_elems = verify_helpers.check_existence(input_boxes_keys)
            sliders_elems = verify_helpers.check_existence(sliders_keys)
            btn_elem = verify_helpers.check_existence(btn_key)

            expected_title = verify_helpers.get_expected_texts(titles_keys)
            expected_placeholder = verify_helpers.get_expected_texts(placeholder_key)[0]

            index_num = 0
            for key in titles_keys:
                expected_chars = list(expected_title[index_num])
                title_chars = list(title[index_num])[-len(expected_title[index_num]):]

                assert title_chars == expected_chars
                index_num += 1
            
            assert placeholder == expected_placeholder
            assert drop_down_elem != None
            assert input_boxes_elems != None
            assert sliders_elems != None
            assert btn_elem != None
            LogUtils.log_success()
            
        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_010(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            subtitle_key = ["login_pg_subtitle"]

            web_utils.open_url()    # 웹사이트 진입
            subtitle_elem = verify_helpers.check_existence(subtitle_key)
            subtitle = verify_helpers.get_elems_texts(subtitle_elem)

            expected_subtitle = verify_helpers.get_expected_texts(subtitle_key)
            
            time.sleep(1)   # 없으면 에러남
            assert "signin" in driver.current_url
            assert subtitle == expected_subtitle
            LogUtils.log_success()
            
        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_011(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            subtitle_key = ["login_input_pg_subtitle"]

            web_utils.open_url()    # 웹사이트 진입
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   # 로그인 버튼 클릭

            subtitle_elem = verify_helpers.check_existence(subtitle_key)
            subtitle = verify_helpers.get_elems_texts(subtitle_elem)

            expected_subtitle = verify_helpers.get_expected_texts(subtitle_key)

            time.sleep(1)   # 없으면 오류남
            assert "login?" in driver.current_url
            assert subtitle == expected_subtitle
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 정보 입력 페이지] 로그인
    @pytest.mark.skip(reason="test pass")
    def test_login_014(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            subtitle_key = ["home_pg_subtitle_2"]

            web_utils.open_url()    # 웹사이트 진입
            
            web_utils.login(login_data["valid_email"], login_data["password"])   # 로그인
            subtitle_elem = verify_helpers.check_existence(subtitle_key)
            subtitle = verify_helpers.get_elems_texts(subtitle_elem)

            expected_subtitle = verify_helpers.get_expected_texts(subtitle_key)

            index_num = 0
            for key in subtitle_key:
                expected_chars = list(expected_subtitle[index_num])
                title_chars = list(subtitle[index_num])[-len(expected_subtitle[index_num]):]

                assert title_chars == expected_chars
                index_num += 1

            assert not "login" in driver.current_url and not "signin" in driver.current_url
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise                 

# [비밀번호 초기화 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_015(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            subtitle_key = ["pwd_reset_pg_subtitle"]
            
            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    

            subtitle_elem = verify_helpers.check_existence(subtitle_key)
            subtitle = verify_helpers.get_elems_texts(subtitle_elem)

            expected_subtitle = verify_helpers.get_expected_texts(subtitle_key)

            assert subtitle == expected_subtitle
            assert "reset-password/request" in driver.current_url
            LogUtils.log_success()
        
        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [비밀번호 초기화 페이지] 비밀번호 초기화
    @pytest.mark.skip(reason="test pass")
    def test_login_016(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            title_key = ["send_mail_pg_title"]
            
            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    

            login_page.input_email(*LOCATORS.get("pwd_reset_pg_input_email"), login_data["valid_email"])   
            web_utils.click_element(*LOCATORS.get("pwd_reset_pg_btn_continue"))    # "계속 버튼" 클릭

            title_elem = verify_helpers.check_existence(title_key)
            title = verify_helpers.get_elems_texts(title_elem)

            expected_title = verify_helpers.get_expected_texts(title_key)

            assert title == expected_title
            LogUtils.log_success()
        
        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# 이메일 재 전송
    @pytest.mark.skip(reason="test fail")
    def test_login_017(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            subtitle_key = ["pwd_reset_pg_subtitle"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    

            login_page.input_email(*LOCATORS.get("pwd_reset_pg_input_email"), login_data["valid_email"])   
            web_utils.click_element(*LOCATORS.get("pwd_reset_pg_btn_continue"))    # "계속 버튼" 클릭
            
            web_utils.click_element(*LOCATORS.get("send_mail_pg_btn_resend"))   # 이메일 재 전송

            input_boxes_keys_value = driver.find_element(*LOCATORS.get("pwd_reset_pg_input_email")).get_attribute("value")

            subtitle_elem = verify_helpers.check_existence(subtitle_key)
            subtitle = verify_helpers.get_elems_texts(subtitle_elem)

            expected_subtitle = verify_helpers.get_expected_texts(subtitle_key)

            assert input_boxes_keys_value == ""
            assert subtitle == expected_subtitle
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# TC LOGIN-018 ~ LOGIN-019 누락

# [비밀번호 초기화 페이지]에서 [로그인 정보 입력 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_020(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            subtitle_key = ["login_input_pg_subtitle"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   
            time.sleep(1)
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    
            
            web_utils.click_element(*LOCATORS.get("pwd_reset_pg_link_login"))   #  '로그인 화면으로 돌아가기 링크' 클릭
            time.sleep(1)
            subtitle_elem = verify_helpers.check_existence(subtitle_key)
            subtitle = verify_helpers.get_elems_texts(subtitle_elem)

            expected_subtitle = verify_helpers.get_expected_texts(subtitle_key)

            assert "login?" in driver.current_url
            assert subtitle == expected_subtitle
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 정보 입력 페이지]에서 [회원가입 페이지]로 이동 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_021(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            subtitle_key = ["signin_pg_subtitle"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_signin"))    # '회원가입 링크' 클릭

            subtitle_elem = verify_helpers.check_existence(subtitle_key)
            subtitle = verify_helpers.get_elems_texts(subtitle_elem)

            expected_subtitle = verify_helpers.get_expected_texts(subtitle_key)

            time.sleep(1)   # 없으면 에러남
            assert "signup?" in driver.current_url
            assert subtitle == expected_subtitle
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 페이지]에서 [회원가입 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_022(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            subtitle_key = ["signin_pg_subtitle"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            subtitle_elem = verify_helpers.check_existence(subtitle_key)
            subtitle = verify_helpers.get_elems_texts(subtitle_elem)

            expected_subtitle = verify_helpers.get_expected_texts(subtitle_key)

            time.sleep(1)   # 없으면 에러남
            assert "signup?" in driver.current_url
            assert subtitle == expected_subtitle
            LogUtils.log_success()
            
        except Exception as e:
                LogUtils.log_error(e, driver)
                raise

# [회원가입 페이지] 비밀번호 입력
    @pytest.mark.skip(reason="test pass")
    def test_login_025(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            text_section_key = "signin_pg_pw_rule_section"
            rules_keys = ["signin_pg_pw_rule_title", "signin_pg_pw_rule_char_num", "signin_pg_pw_rule_following", 
                          "signin_pg_pw_rule_following_Lower_letters", "signin_pg_pw_rule_following_upper_letters",
                          "signin_pg_pw_rule_following_num", "signin_pg_pw_rule_following_special_char"]
            
            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  

            rules = verify_helpers.get_children_text(text_section_key, rules_keys)

            expected_rules = verify_helpers.get_expected_texts(rules_keys)

            assert rules == expected_rules
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [권한 요청 페이지] 진입
    @pytest.mark.skip(reason="test pass")
    def test_login_026(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)
            signin_email = unique_email()

            form_key = "authorize_pg_form"
            btns_keys = ["authorize_pg_btn_accept", "authorize_pg_btn_decline"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_email)    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue"))

            btns_elems = verify_helpers.check_children_existence(form_key, btns_keys)

            assert "consent?" in driver.current_url
            assert btns_elems != None
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 오류 페이지] 진입
    @pytest.mark.skip(reason="test pass")
    def test_login_027(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)
            signin_email = unique_email()

            btn_key = ["error_pg_btn_retry"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_email)    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue")) 

            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_decline"))  

            btn_elems = verify_helpers.check_existence(btn_key)

            assert "signin" in driver.current_url
            assert btn_elems != None
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# "다시 시도하기 버튼" 동작 확인
    @pytest.mark.skip(reason="test pass")
    def test_login_028(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)
            signin_email = unique_email()

            subtitle_key = ["login_pg_subtitle"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_email)    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue")) 

            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_decline"))  

            web_utils.click_element(*LOCATORS.get("error_pg_btn_retry"))    # "다시 시도하기 버튼" 클릭

            text_elem = verify_helpers.check_existence(subtitle_key)
            text = verify_helpers.get_elems_texts(text_elem)

            expected_text = verify_helpers.get_expected_texts(subtitle_key)

            assert "signin" in driver.current_url
            assert text == expected_text
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [권한 요청 페이지] 재 진입
    @pytest.mark.skip(reason="test pass")
    def test_login_029(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)
            signin_email = unique_email()

            form_key = "authorize_pg_form"
            btns_keys = ["authorize_pg_btn_accept", "authorize_pg_btn_decline"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_email)    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue")) 

            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_decline"))  

            web_utils.click_element(*LOCATORS.get("error_pg_btn_retry"))    # "다시 시도하기 버튼" 클릭

            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))    

            btns_elems = verify_helpers.check_children_existence(form_key, btns_keys)

            assert "consent?" in driver.current_url
            assert btns_elems != None
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [권한 요청 페이지] 재 진입
    @pytest.mark.skip(reason="test pass")
    def test_login_030(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)
            signin_email = unique_email()

            form_key = "authorize_pg_form"
            btns_keys = ["authorize_pg_btn_accept", "authorize_pg_btn_decline"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_email)    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue")) 

            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_decline"))  

            web_utils.click_element(*LOCATORS.get("error_pg_btn_retry"))    # "다시 시도하기 버튼" 클릭

            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))    # "로그인하기 버튼" 클릭

            btns_elems = verify_helpers.check_children_existence(form_key, btns_keys)

            assert "consent?" in driver.current_url
            assert btns_elems != None
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [권한 요청 페이지] 권한 요청 승인
    @pytest.mark.skip(reason="test pass")
    def test_login_031(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)
            signin_email = unique_email()

            title_key = ["profile_pg_title"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   
            time.sleep(2)
            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_email)    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue")) 
            time.sleep(2)   # 없으면 오류남

            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_accept"))  # "승인 버튼" 클릭
            time.sleep(2)   # 없으면 오류남

            title_elem = verify_helpers.check_existence(title_key)
            title = verify_helpers.get_elems_texts(title_elem)

            expected_title = verify_helpers.get_expected_texts(title_key)

            assert "welcome" in driver.current_url
            assert list(expected_title[0]) == list(title[0])[2:]
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [프로필 입력 페이지] 데이터 입력 미완료 상태에서 제출 시도
    @pytest.mark.skip(reason="test pass")
    def test_login_032(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)
            signin_email = unique_email()

            err_msgs_keys = ["profile_pg_error_name", "profile_pg_error_team", 
                           "profile_pg_error_sweetness", "profile_pg_error_salty", "profile_pg_error_spicy",
                           "profile_pg_error_like", "profile_pg_error_dislike"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   
            time.sleep(2)
            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_email)    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue")) 
            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_accept"))  # "승인 버튼" 클릭

            web_utils.click_element(*LOCATORS.get("profile_pg_btn_submit")) # "제출하기 버튼" 클릭
            time.sleep(1)

            err_msgs_elems = verify_helpers.check_existence(err_msgs_keys)
            err_msgs = verify_helpers.get_elems_texts(err_msgs_elems)

            expected_errors = verify_helpers.get_expected_texts(err_msgs_keys)

            index_num = 0
            for key in err_msgs_keys:
                expected_chars = list(expected_errors[index_num])
                error_chars = list(err_msgs[index_num])[-len(expected_errors[index_num]):]

                assert error_chars == expected_chars
                index_num += 1
                
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [프로필 입력 페이지] 제출
    @pytest.mark.skip(reason="test pass")
    def test_login_033(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)
            team_feed = TeamFeed(driver)
            signin_email = unique_email()

            subtitle_key = ["home_pg_subtitle_2"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   
            time.sleep(2)
            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_email)    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue")) 

            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_accept"))  # "승인 버튼" 클릭
      

            login_page.input_text(*LOCATORS.get("profile_pg_name_input"), signin_data["name"])

            team_feed.open_team_combobox()
            team_feed.select_team_combobox(signin_data["team"])
            
            web_utils.slider_sweet()
            web_utils.slider_salty()
            web_utils.slider_hot()

            login_page.input_text(*LOCATORS.get("profile_pg_like_input"), signin_data["like"])
            login_page.input_text(*LOCATORS.get("profile_pg_dislike_input"), signin_data["dislike"])

            web_utils.click_element(*LOCATORS.get("profile_pg_team_btn_submmit")) # "제출하기 버튼" 클릭

            text_elem = verify_helpers.check_existence(subtitle_key)
            text = verify_helpers.get_elems_texts(text_elem)

            expected_text = verify_helpers.get_expected_texts(subtitle_key)

            assert not "welcome" in driver.current_url

            index_num = 0
            for key in subtitle_key:
                expected_chars = list(expected_text[index_num])
                title_chars = list(text[index_num])[-len(expected_text[index_num]):]

                assert title_chars == expected_chars
                index_num += 1

            LogUtils.log_success()
            time.sleep(1)

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise



#-----------------------------------------------------------
# 1. [로그인 페이지] 회원가입 ~ [프로필 입력 페이지] 제출
    @pytest.mark.order(1)
    def test_login_033(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)
            team_feed = TeamFeed(driver)
            signin_email = unique_email()

            subtitle_key = ["home_pg_subtitle_2"]
            # 웹페이지 진입
            web_utils.open_url()    
            # 회원가입
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   
            time.sleep(2)
            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_email)    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue")) 
            # 권한 요청 승인
            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_accept"))  # "승인 버튼" 클릭
      
            # 프로필 데이터 제출
            login_page.input_text(*LOCATORS.get("profile_pg_name_input"), signin_data["name"])

            team_feed.open_team_combobox()
            team_feed.select_team_combobox(signin_data["team"])
            
            web_utils.slider_sweet()
            web_utils.slider_salty()
            web_utils.slider_hot()

            login_page.input_text(*LOCATORS.get("profile_pg_like_input"), signin_data["like"])
            login_page.input_text(*LOCATORS.get("profile_pg_dislike_input"), signin_data["dislike"])

            web_utils.click_element(*LOCATORS.get("profile_pg_team_btn_submmit")) # "제출하기 버튼" 클릭

            text_elem = verify_helpers.check_existence(subtitle_key)
            text = verify_helpers.get_elems_texts(text_elem)

            expected_text = verify_helpers.get_expected_texts(subtitle_key)

            assert not "welcome" in driver.current_url

            index_num = 0
            for key in subtitle_key:
                expected_chars = list(expected_text[index_num])
                title_chars = list(text[index_num])[-len(expected_text[index_num]):]

                assert title_chars == expected_chars
                index_num += 1

            LogUtils.log_success()
            time.sleep(1)

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise