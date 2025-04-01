import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.utils.helpers import WebUtils, VerifyHelpers
from src.pages.login_page import LoginPage
from src.pages.team_feed_page import TeamFeed
from src.utils.locators import LOCATORS
from src.resources.testdata.user_data import login_data, signin_data
from src.utils.log_util import LogUtils

@pytest.mark.usefixtures("driver")
class TestLoginPage:
# [로그인 페이지] UI 확인
    # @pytest.mark.skip(reason="test pass")
    def test_login_001(self, driver):
        try:
            # Settings & Precondition
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            # Steps
            web_utils.open_url()    

            # Expected Result
            assert verify_helpers.get_elem_text(*LOCATORS.get("login_pg_title")) == "오늘 뭐 먹지?"
            assert verify_helpers.get_elem_text(*LOCATORS.get("login_pg_subtitle")) == "오늘의 식사 메뉴를 추천해드립니다"
            assert verify_helpers.check_existence(*LOCATORS.get("login_pg_login_btn")) != None
            assert verify_helpers.check_existence(*LOCATORS.get("login_pg_signin_btn")) != None

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 정보 입력 페이지] UI확인
    # @pytest.mark.skip(reason="test pass")
    def test_login_002(self, driver):
        try:
            # Settings & Precondition
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            web_utils.open_url()    

            # Steps
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   

            # Expected Result
            assert verify_helpers.get_elem_text(*LOCATORS.get("login_input_pg_title")) == "오늘 뭐 먹지?"
            assert verify_helpers.get_elem_text(*LOCATORS.get("login_input_pg_subtitle")) == "맛있는 선택은 당신의 하루를 바꿉니다."
            assert verify_helpers.check_existence(*LOCATORS.get("login_input_pg_input_email")) != None
            assert verify_helpers.check_existence(*LOCATORS.get("login_input_pg_input_pwd")) != None
            assert verify_helpers.get_elem_text(*LOCATORS.get("login_input_pg_placeholder_email")) == "이메일 주소*"
            assert verify_helpers.get_elem_text(*LOCATORS.get("login_input_pg_placeholder_pwd")) == "비밀번호*"

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [비밀번호 초기화 페이지] UI 확인
    # @pytest.mark.skip(reason="test pass")
    def test_login_003(self, driver):
        try:
            # Settings & Precondition
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            web_utils.open_url()    

            # Steps
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    

            # Expected Result
            assert verify_helpers.get_elem_text(*LOCATORS.get("pwd_reset_pg_title")) == "비밀번호를 잊어버리셨나요?"
            assert verify_helpers.get_elem_text(*LOCATORS.get("pwd_reset_pg_subtitle")) == "이메일 주소를 입력하면 비밀번호 재설정 지침을 보내드립니다."
            assert verify_helpers.check_existence(*LOCATORS.get("pwd_reset_pg_input_email")) != None
            assert verify_helpers.get_elem_text(*LOCATORS.get("pwd_reset_pg_placeholder_email")) == "이메일 주소*"
            assert verify_helpers.check_existence(*LOCATORS.get("pwd_reset_pg_btn_continue")) != None
            assert verify_helpers.get_elem_text(*LOCATORS.get("pwd_reset_pg_link_login")) == "로그인 화면으로 돌아가기"

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [이메일 전송 완료 페이지] UI 확인
    # @pytest.mark.skip(reason="test pass")
    def test_login_004(self, driver):
        try:
            # Settings & Precondition
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    

            # Steps
            login_page.input_email(*LOCATORS.get("pwd_reset_pg_input_email"), login_data["valid_email"])    
            web_utils.click_element(*LOCATORS.get("pwd_reset_pg_btn_continue"))    

            # Expected Result
            assert verify_helpers.get_elem_text(*LOCATORS.get("send_mail_pg_title")) == "Check Your Email"
            assert verify_helpers.get_elem_text(*LOCATORS.get("send_mail_pg_subtitle")) == "Please check the email address hyeyoung.k111@gmail.com for instructions to reset your password."
            assert verify_helpers.check_existence(*LOCATORS.get("send_mail_pg_btn_resend")) != None

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# TC LOGIN-005 메뉴얼 테스트

# [회원가입 페이지] UI 확인
    # @pytest.mark.skip(reason="test pass")
    def test_login_006(self, driver):
        try:
            # Settings & Precondition
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)
            
            web_utils.open_url()    

            # Steps
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   
            
            # Expected Result
            assert verify_helpers.get_elem_text(*LOCATORS.get("signin_pg_title")) == "환영합니다"
            assert verify_helpers.get_elem_text(*LOCATORS.get("signin_pg_subtitle")) == "오늘 뭐 먹지? 를 사용하시려면 회원가입을 진행해주세요."
            assert verify_helpers.check_existence(*LOCATORS.get("signin_pg_input_email")) != None
            assert verify_helpers.check_existence(*LOCATORS.get("signin_pg_input_pwd")) != None
            assert verify_helpers.get_elem_text(*LOCATORS.get("signin_pg_placeholder_email")) == "이메일 주소*"
            assert verify_helpers.get_elem_text(*LOCATORS.get("signin_pg_placeholder_pwd")) == "비밀번호*"
            assert verify_helpers.check_existence(*LOCATORS.get("signin_pg_pg_btn_continue")) != None
            assert verify_helpers.get_elem_text(*LOCATORS.get("signin_pg_link_login")) == "로그인"

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [권한 요청 페이지] UI 확인
    # @pytest.mark.skip(reason="test pass")
    def test_login_007(self, driver):
        try:
            # Settings & Precondition
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            # Steps
            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_data["email"])    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue"))

            # Expected Result
            assert verify_helpers.get_elem_text(*LOCATORS.get("authorize_pg_title")) == "Authorize App"
            assert verify_helpers.get_elem_text(*LOCATORS.get("authorize_pg_email")) == f"Hi {signin_data["email"]},"
            assert verify_helpers.get_elem_text(*LOCATORS.get("authorize_pg_subtitle")) == "Assgin-front is requesting access to your dev-aqq0w41zxvftci4m account."
            assert verify_helpers.get_elem_text(*LOCATORS.get("authorize_pg_requested_authorize")) == "profile: access to your profile and email"
            assert verify_helpers.check_existence(*LOCATORS.get("authorize_pg_btn_decline")) != None
            assert verify_helpers.check_existence(*LOCATORS.get("authorize_pg_btn_accept")) != None

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 오류 페이지] UI 확인
    # @pytest.mark.skip(reason="test pass")
    def test_login_008(self, driver):
        try:
            # Settings & Precondition
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_data["email"])    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue"))
            
            # Steps
            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_decline"))  

            # Expected Result
            assert verify_helpers.get_elem_text(*LOCATORS.get("error_pg_title")) == "로그인 오류"
            assert verify_helpers.get_elem_text(*LOCATORS.get("error_pg_subtitle")) == "User did not authorize the request"
            assert verify_helpers.check_existence(*LOCATORS.get("error_pg_btn_retry")) != None

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [프로필 입력 페이지] UI 확인
    # @pytest.mark.skip(reason="test pass")
    def test_login_009(self, driver):
        try:
            # Settings & Precondition
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))
            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_data["email"])    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue")) 

            # Steps
            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_accept"))

            # Expected Result
            expected_titles = ["서비스 이용을 위해 인적사항을 작성해주세요", "이름을 입력해주세요", "본인이 속한 팀을 선택해주세요",
            "음식 성향에 대해 이야기 해주세요!", "추가적인 음식 성향을 이야기 해주세요!", "이 점은 좋아요",
            "이 점은 싫어요", "이름을 입력해주세요"]

            titles = [None] * 7
            
            titles[0] = verify_helpers.get_elem_text(*LOCATORS.get("profile_pg_title"))
            titles[1] = verify_helpers.get_elem_text(*LOCATORS.get("profile_pg_name_title"))
            titles[2] = verify_helpers.get_elem_text(*LOCATORS.get("profile_pg_team_title"))
            titles[3] = verify_helpers.get_elem_text(*LOCATORS.get("profile_pg_taste_title"))
            titles[4] = verify_helpers.get_elem_text(*LOCATORS.get("profile_pg_preference_title"))
            titles[5] = verify_helpers.get_elem_text(*LOCATORS.get("profile_pg_like_title"))
            titles[6] = verify_helpers.get_elem_text(*LOCATORS.get("profile_pg_dislike_title"))
           
            index_num = 0
            for title in titles:
                expected_chars = list(expected_titles[index_num])
                title_chars = list(titles[index_num])[-len(expected_titles[index_num]):]

                assert title_chars == expected_chars
                index_num += 1

            assert verify_helpers.check_existence(*LOCATORS.get("profile_pg_team_btn")) != None
            assert verify_helpers.check_existence(*LOCATORS.get("profile_pg_name_input")) != None
            assert verify_helpers.check_existence(*LOCATORS.get("profile_pg_like_input")) != None
            assert verify_helpers.check_existence(*LOCATORS.get("profile_pg_dislike_input")) != None
            assert verify_helpers.check_existence(*LOCATORS.get("profile_pg_taste_slider_sweetness")) != None
            assert verify_helpers.check_existence(*LOCATORS.get("profile_pg_taste_slider_salty")) != None
            assert verify_helpers.check_existence(*LOCATORS.get("profile_pg_taste_slider_spicy")) != None
            assert verify_helpers.check_existence(*LOCATORS.get("profile_pg_btn_submit")) != None

            LogUtils.log_success()
            
        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 페이지] 진입 확인
    # @pytest.mark.skip(reason="test pass")
    def test_login_010(self, driver):
        try:
            # Settings & Precondition
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            # Steps
            web_utils.open_url()    

            # Expected Result
            assert "signin" in driver.current_url
            assert verify_helpers.get_elem_text(*LOCATORS.get("login_pg_subtitle")) == "오늘의 식사 메뉴를 추천해드립니다"
            
            LogUtils.log_success()
            
        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [로그인 페이지] 진입 확인
    # @pytest.mark.skip(reason="test pass")
    def test_login_011(self, driver):
        try:
            # Settings & Precondition
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            web_utils.open_url()    

            # Steps
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   

            # Expected Result
            assert "login?" in driver.current_url
            assert verify_helpers.get_elem_text(*LOCATORS.get("login_input_pg_subtitle")) == "맛있는 선택은 당신의 하루를 바꿉니다."
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# TC LOGIN-012 ~ LOGIN-013 메뉴얼 테스트

# [로그인 정보 입력 페이지] 로그인
    ## @pytest.mark.skip(reason="test pass")
    def test_login_014(self, driver):
        try:
            # Settings & Precondition
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            web_utils.open_url()    

            # Steps
            web_utils.login(login_data["valid_email"], login_data["password"])


            assert not "login" in driver.current_url and not "signin" in driver.current_url

            assert verify_helpers.get_elem_text(*LOCATORS.get("home_pg_subtitle_2")) == "🍽️ 직원들이 가장 선호하는 음식 종류는 무엇일까요?"
            

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise                      

# [비밀번호 초기화 페이지] 진입 확인
    # @pytest.mark.skip(reason="test pass")
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
    # @pytest.mark.skip(reason="test pass")
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
    # @pytest.mark.skip(reason="test fail")
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
    # @pytest.mark.skip(reason="test pass")
    def test_login_020(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            subtitle_key = ["login_input_pg_subtitle"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_login_btn"))   
            web_utils.click_element(*LOCATORS.get("login_input_pg_link_reset_pwd"))    
            
            web_utils.click_element(*LOCATORS.get("pwd_reset_pg_link_login"))   #  '로그인 화면으로 돌아가기 링크' 클릭

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
    # @pytest.mark.skip(reason="test pass")
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
    # @pytest.mark.skip(reason="test pass")
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
    # @pytest.mark.skip(reason="test pass")
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
    # @pytest.mark.skip(reason="test pass")
    def test_login_026(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            form_key = "authorize_pg_form"
            btns_keys = ["authorize_pg_btn_accept", "authorize_pg_btn_decline"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_data["email"])    
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
    # @pytest.mark.skip(reason="test pass")
    def test_login_027(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            btn_key = ["error_pg_btn_retry"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_data["email"])    
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
    # @pytest.mark.skip(reason="test pass")
    def test_login_028(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            subtitle_key = ["login_pg_subtitle"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_data["email"])    
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
    # @pytest.mark.skip(reason="test pass")
    def test_login_029(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            form_key = "authorize_pg_form"
            btns_keys = ["authorize_pg_btn_accept", "authorize_pg_btn_decline"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_data["email"])    
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
    # @pytest.mark.skip(reason="test pass")
    def test_login_030(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            form_key = "authorize_pg_form"
            btns_keys = ["authorize_pg_btn_accept", "authorize_pg_btn_decline"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   

            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_data["email"])    
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
    # @pytest.mark.skip(reason="test pass")
    def test_login_031(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            title_key = ["profile_pg_title"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   
            time.sleep(2)
            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_data["email"])    
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
    # @pytest.mark.skip(reason="test 못함!")
    def test_login_032(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)

            err_msgs_keys = ["profile_pg_error_name", "profile_pg_error_team", 
                           "profile_pg_error_sweetness", "profile_pg_error_salty", "profile_pg_error_spicy",
                           "profile_pg_error_like", "profile_pg_error_dislike"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   
            time.sleep(2)
            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_data["email"])    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue")) 
            time.sleep(2)   # 없으면 오류남

            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_accept"))  # "승인 버튼" 클릭
            time.sleep(2)   # 없으면 오류남

            web_utils.click_element(*LOCATORS.get("profile_pg_btn_submit")) # "제출하기 버튼" 클릭
            time.sleep(1)

            err_msgs_elems = verify_helpers.check_existence(err_msgs_keys)
            err_msgs = verify_helpers.get_elems_texts(err_msgs_elems)

            expected_errors = verify_helpers.get_expected_texts(err_msgs_keys)

            test = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div > p')
            print(test.text)

            assert err_msgs == expected_errors
            LogUtils.log_success()
            time.sleep(1)

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [프로필 입력 페이지] 제출
    # @pytest.mark.skip(reason="test pass")
    def test_login_033(self, driver):
        try:
            web_utils = WebUtils(driver)
            login_page = LoginPage(driver)
            verify_helpers = VerifyHelpers(driver)
            team_feed = TeamFeed(driver)

            subtitle_key = ["home_pg_subtitle_1"]

            web_utils.open_url()    
            web_utils.click_element(*LOCATORS.get("login_pg_signin_btn"))   
            time.sleep(2)
            login_page.input_email(*LOCATORS.get("signin_pg_input_email"), signin_data["email"])    
            login_page.input_password(*LOCATORS.get("signin_pg_input_pwd"), signin_data["password"])  
            web_utils.click_element(*LOCATORS.get("signin_pg_btn_continue")) 

            web_utils.click_element(*LOCATORS.get("authorize_pg_btn_accept"))  # "승인 버튼" 클릭
      

            login_page.input_text(*LOCATORS.get("profile_pg_name_input"), signin_data["name"])

            web_utils.click_element(*LOCATORS.get("profile_pg_team_btn"))

            team_feed.open_team_combobox
            team_feed.select_team_combobox(signin_data["team"])
            
            web_utils.slider_sweet()
            web_utils.slider_salty()
            web_utils.slider_hot()

            login_page.input_text(*LOCATORS.get("profile_pg_like_input"), signin_data["like"])
            login_page.input_text(*LOCATORS.get("profile_pg_dislike_input"), signin_data["dislike"])

            web_utils.click_element(*LOCATORS.get("profile_pg_btn_submit")) # "제출하기 버튼" 클릭

            text_elem = verify_helpers.check_existence(subtitle_key)
            text = verify_helpers.get_elem_text(text_elem)

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
