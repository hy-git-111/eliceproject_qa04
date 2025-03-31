import time
import pytest
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from src.utils.helpers import WebUtils, VerifyHelpers
from src.pages.login_page import LoginPage
from src.resources.testdata.expected_texts import EXPECTED_TEXTS
from src.utils.locators import LOCATORS
from src.resources.testdata.user_data import login_data, signin_data

from src.utils.log_util import LogUtils

@pytest.mark.usefixtures("driver")
class TestHistoryPage:
# [히스토리 페이지] 헤더 영역 UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_history_001(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            btn_key = ["history_pg_btn_back"]
            title_key = ["history_pg_title"]

            web_utils.open_url()
            web_utils.login(login_data["empty_email"], login_data["password"])

            web_utils.click_tab_history()

            btn_elem = verify_helpers.check_existence(btn_key)

            title_elem = verify_helpers.check_existence(title_key)
            title = verify_helpers.get_elems_texts(title_elem)

            expected_title = verify_helpers.get_expected_texts(title_key)

            assert btn_elem != None
            assert list(title[0])[-len(expected_title[0]):] == list(expected_title[0])

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [히스토리 페이지] 수락한 메뉴가 없을때 추천 메뉴 영역 UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_history_002(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            title_key = ["history_pg_subtitle"]
            food_list_key = ["history_pg_list"]

            web_utils.open_url()
            web_utils.login(login_data["empty_email"], login_data["password"])

            web_utils.click_tab_history()

            title_elem = verify_helpers.check_existence(title_key)
            title = verify_helpers.get_elems_texts(title_elem)

            expected_title = verify_helpers.get_expected_texts(title_key)

            with pytest.raises(TimeoutException):
                verify_helpers.check_existence(food_list_key)

            assert list(title[0])[-len(expected_title[0]):] == list(expected_title[0])

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [히스토리 페이지] 후기 등록 전 추천 메뉴 영역 UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_history_003(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            before_review_btn_key = ["history_pg_btn_before_review"]
            title_key = ["history_pg_subtitle"]
            food_list_key = ["history_pg_list"]

            web_utils.open_url()
            web_utils.login("test@elice.com", "xptmxmrlagP0!")  # 임시용
            # web_utils.login(login_data["no_review_email"], login_data["password"])    데이터 세팅 불가로 주석처리

            web_utils.click_tab_history()

            before_review_btn_elems = verify_helpers.check_existence(before_review_btn_key)
            if before_review_btn_elems == None:
                try:
                    web_utils.scroll_to_element(*LOCATORS.get(before_review_btn_key))
                    before_review_btn_elems = verify_helpers.check_existence(before_review_btn_key)
                    time.sleep(2)
                    
                except TimeoutException:
                    web_utils.scroll_to_element(*LOCATORS.get(before_review_btn_key))
                    before_review_btn_elems = verify_helpers.check_existence(before_review_btn_key)
                    time.sleep(2)           
            btn_text = verify_helpers.get_elems_texts(before_review_btn_elems)            

            title_elem = verify_helpers.check_existence(title_key)
            title = verify_helpers.get_elems_texts(title_elem)

            food_list_elem = verify_helpers.check_existence(food_list_key)

            expected_title = verify_helpers.get_expected_texts(title_key)
            expected_btn_text = verify_helpers.get_expected_texts(before_review_btn_key)
            
            assert food_list_elem != None
            assert list(title[0])[-len(expected_title[0]):] == list(expected_title[0])
            assert btn_text == expected_btn_text

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [히스토리 페이지] 후기 등록 후 추천 메뉴 영역 UI 확인
    @pytest.mark.skip(reason="test pass")
    def test_history_004(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            after_review_btn_key = ["history_pg_btn_after_review"]
            title_key = ["history_pg_subtitle"]
            food_list_key = ["history_pg_list"]

            web_utils.open_url()
            web_utils.login("test@elice.com", "xptmxmrlagP0!")  # 임시용
            # web_utils.login(login_data["no_review_email"], login_data["password"])    데이터 세팅 불가로 주석처리

            web_utils.click_tab_history()



            # 리뷰 등록 코드 추가
            # 리뷰 등록 코드 추가
            # 리뷰 등록 코드 추가
            # 리뷰 등록 코드 추가


            after_review_btn_elems = verify_helpers.check_existence(after_review_btn_key)
            if after_review_btn_elems == None:
                try:
                    web_utils.scroll_to_element(*LOCATORS.get(after_review_btn_key))
                    after_review_btn_elems = verify_helpers.check_existence(after_review_btn_key)
                    time.sleep(2)
                    
                except TimeoutException:
                    web_utils.scroll_to_element(*LOCATORS.get(after_review_btn_key))
                    after_review_btn_elems = verify_helpers.check_existence(after_review_btn_key)
                    time.sleep(2)           
            btn_text = verify_helpers.get_elems_texts(after_review_btn_elems)            

            title_elem = verify_helpers.check_existence(title_key)
            title = verify_helpers.get_elems_texts(title_elem)

            food_list_elem = verify_helpers.check_existence(food_list_key)

            expected_title = verify_helpers.get_expected_texts(title_key)
            expected_btn_text = verify_helpers.get_expected_texts(after_review_btn_key)
            
            assert food_list_elem != None
            assert list(title[0])[-len(expected_title[0]):] == list(expected_title[0])
            assert btn_text == expected_btn_text

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [히스토리 페이지] 진입 확인
    @pytest.mark.skip(reason="test pass")
    def test_history_005(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            subtitle_key = ["history_pg_subtitle"]

            web_utils.open_url()
            web_utils.login(login_data["empty_email"], login_data["password"])

            web_utils.click_tab_history()

            subtitle_elem = verify_helpers.check_existence(subtitle_key)
            subtitle_text = verify_helpers.get_elems_texts(subtitle_elem)

            expected_texts = verify_helpers.get_expected_texts(subtitle_key)

            assert "history" in driver.current_url
            assert subtitle_text != expected_texts

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [히스토리 페이지] "뒤로가기 버튼" 확인
    @pytest.mark.skip(reason="test pass")
    def test_history_006(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            title_key = ["home_pg_subtitle"]

            web_utils.open_url()
            web_utils.login("test@elice.com", "xptmxmrlagP0!")  # 임시용
            # web_utils.login(login_data["no_review_email"], login_data["password"])    데이터 세팅 불가로 주석처리

            web_utils.click_tab_history()
            web_utils.click_element(*LOCATORS.get("history_pg_btn_back"))

            title_elem = verify_helpers.check_existence(title_key)
            title = verify_helpers.get_elems_texts(title_elem)

            expected_title = verify_helpers.get_expected_texts(title_key)
            
            assert not "history" in driver.current_url
            assert list(title[0])[-len(expected_title[0]):] == list(expected_title[0])

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# 1번 리스트의 그룹, 유형, 메뉴명 비교하는 코드 작성하기
# [히스토리 페이지] 추천받은 메뉴 기록 확인
    @pytest.mark.skip(reason="미완성")
    def test_history_007(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            first_food_list = ["history_pg_list_1"] 

            web_utils.open_url()
            web_utils.login("test@elice.com", "xptmxmrlagP0!")  # 임시용
            # web_utils.login(login_data["no_review_email"], login_data["password"])    데이터 세팅 불가로 주석처리


            ## 추천받기 어디서 떼오자
            ## 추천받기 어디서 떼오자
            ## 추천받기 어디서 떼오자
            ## 추천받기 어디서 떼오자



            web_utils.click_tab_history()
            web_utils.click_element(*LOCATORS.get("history_pg_btn_back"))

            title_elem = verify_helpers.check_existence(title_key)
            title = verify_helpers.get_elems_texts(title_elem)

            expected_title = verify_helpers.get_expected_texts(title_key)
            
            assert not "history" in driver.current_url
            assert list(title[0])[-len(expected_title[0]):] == list(expected_title[0])

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise




# [히스토리 페이지] 무한 스크롤 확인
    @pytest.mark.skip(reason="test pass")
    def test_history_008(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            food_list_key = "history_pg_list"

            web_utils.open_url()
            web_utils.login("test@elice.com", "xptmxmrlagP0!")  # 임시용
            # web_utils.login(login_data["no_review_email"], login_data["password"])    데이터 세팅 불가로 주석처리

            web_utils.click_tab_history()

            cnt_list_before = verify_helpers.cnt_elements(food_list_key)

            web_utils.scroll_to_element(*LOCATORS.get("history_pg_list_10"))
            time.sleep(3)   # 없으면 오류남

            cnt_list_after = verify_helpers.cnt_elements(food_list_key)
            
            assert cnt_list_before == 10
            assert cnt_list_after == 20

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [히스토리 페이지] "추천 후기 등록하기 버튼" 확인
    @pytest.mark.skip(reason="test pass")
    def test_history_009(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            before_review_btn_key = ["history_pg_btn_before_review"]
            exit_btn_key = ["review_pg_btn_exit"]

            web_utils.open_url()
            web_utils.login("test@elice.com", "xptmxmrlagP0!")  # 임시용
            # web_utils.login(login_data["no_review_email"], login_data["password"])    데이터 세팅 불가로 주석처리

            web_utils.click_tab_history()

            list_elements = verify_helpers.check_existence(before_review_btn_key)
            for element in list_elements:
                element.click()
                time.sleep(2)
                return
            
            upload_btn_elem = verify_helpers.check_existence(exit_btn_key)
            
            assert upload_btn_elem != None

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [히스토리 페이지] 후기 등록
    @pytest.mark.skip(reason="미완성")
    def test_history_010(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            before_review_btn_key = ["history_pg_btn_before_review"]
            after_review_btn_key = ["history_pg_btn_after_review"]
 
            web_utils.open_url()
            web_utils.login("test@elice.com", "xptmxmrlagP0!")  # 임시용
            # web_utils.login(login_data["no_review_email"], login_data["password"])    데이터 세팅 불가로 주석처리

            web_utils.click_tab_history()

            before_review_btn_elems = verify_helpers.check_existence(before_review_btn_key)
            if before_review_btn_elems == None:
                try:
                    web_utils.scroll_to_element(*LOCATORS.get(before_review_btn_key))
                    before_review_btn_elems = verify_helpers.check_existence(before_review_btn_key)
                    time.sleep(2)
                    
                except TimeoutException:
                    web_utils.scroll_to_element(*LOCATORS.get(before_review_btn_key))
                    before_review_btn_elems = verify_helpers.check_existence(before_review_btn_key)
                    time.sleep(2)              
                
            for elem in before_review_btn_elems:
                driver.execute_script("arguments[0].click();", elem)
                return elem
            
            # 진입까지 완료
            # 후기 등록 추가 필요
            # 토스트팝업도 검증할건지 생각해보기

            
            after_review_btn_elem = elem.find_element(By.TAG_NAME, "button")
            after_review_btn_text = verify_helpers.get_elems_texts(after_review_btn_elem)
            
            expected_text = verify_helpers.get_expected_texts(after_review_btn_key)

            assert after_review_btn_text == expected_text

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [히스토리 페이지] "후기 등록 완료 버튼" 확인
    @pytest.mark.skip(reason="pass")
    def test_history_011(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            exit_btn_key = ["review_pg_btn_exit"]
            after_review_btn_key = ["history_pg_btn_after_review"]

            web_utils.open_url()
            web_utils.login("test@elice.com", "xptmxmrlagP0!")  # 임시용
            # web_utils.login(login_data["no_review_email"], login_data["password"])    데이터 세팅 불가로 주석처리

            web_utils.click_tab_history()

            after_review_btns_elems = verify_helpers.check_existence(after_review_btn_key)
            time.sleep(2)
            if after_review_btns_elems == None:
                try:
                    web_utils.scroll_to_element(*LOCATORS.get(after_review_btn_key))
                    after_review_btns_elems = verify_helpers.check_existence(after_review_btn_key)
                    time.sleep(2)
                    
                except TimeoutException:
                    web_utils.scroll_to_element(*LOCATORS.get(after_review_btn_key))
                    after_review_btns_elems = verify_helpers.check_existence(after_review_btn_key)
                    time.sleep(2)              
                
            for elem in after_review_btns_elems:
                driver.execute_script("arguments[0].click();", elem)

            with pytest.raises(TimeoutException):
                verify_helpers.check_existence(exit_btn_key)

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
