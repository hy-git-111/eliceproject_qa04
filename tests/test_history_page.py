import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from src.utils.helpers import WebUtils, VerifyHelpers
from src.utils.locators import LOCATORS
from src.resources.testdata.user_data import login_data, review_data

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
            
            # 사전조건
            web_utils.open_url()
            web_utils.login(login_data["empty_email"], login_data["password"])

            web_utils.click_tab_history()

            btn_elem = verify_helpers.check_existence(btn_key)

            title_elem = verify_helpers.check_existence(title_key)
            title = verify_helpers.get_elems_texts(title_elem)

            expected_title = verify_helpers.get_expected_texts(title_key)

            assert btn_elem != None
            assert list(title[0])[-len(expected_title[0]):] == list(expected_title[0])

            LogUtils.log_success()

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

            LogUtils.log_success()

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
            web_utils.login(login_data["no_review_email"], login_data["password"])

            web_utils.click_tab_history()

            before_review_btn_elems = verify_helpers.check_existence(before_review_btn_key)
            if before_review_btn_elems == None:
                try:
                    web_utils.scroll_to_element(*LOCATORS.get(before_review_btn_key))
                    before_review_btn_elems = verify_helpers.check_existence(before_review_btn_key)
                    time.sleep(2)   # 없으면 에러남
                    
                except TimeoutException:
                    web_utils.scroll_to_element(*LOCATORS.get(before_review_btn_key))
                    before_review_btn_elems = verify_helpers.check_existence(before_review_btn_key)
                    time.sleep(2)   # 없으면 에러남

            btn_text = verify_helpers.get_elems_texts(before_review_btn_elems)            

            title_elem = verify_helpers.check_existence(title_key)
            title = verify_helpers.get_elems_texts(title_elem)

            food_list_elem = verify_helpers.check_existence(food_list_key)

            expected_title = verify_helpers.get_expected_texts(title_key)
            expected_btn_text = verify_helpers.get_expected_texts(before_review_btn_key)
            
            assert food_list_elem != None
            assert list(title[0])[-len(expected_title[0]):] == list(expected_title[0])
            assert btn_text == expected_btn_text

            LogUtils.log_success()

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
            web_utils.login(login_data["review_email"], login_data["password"])

            web_utils.click_tab_history()

            after_review_btn_elems = verify_helpers.check_existence(after_review_btn_key)
            if after_review_btn_elems == None:
                try:
                    web_utils.scroll_to_element(*LOCATORS.get(after_review_btn_key))
                    after_review_btn_elems = verify_helpers.check_existence(after_review_btn_key)
                    time.sleep(2)   # 없으면 에러남
                    
                except TimeoutException:
                    web_utils.scroll_to_element(*LOCATORS.get(after_review_btn_key))
                    after_review_btn_elems = verify_helpers.check_existence(after_review_btn_key)
                    time.sleep(2)   # 없으면 에러남

            btn_text = verify_helpers.get_elems_texts(after_review_btn_elems)            

            title_elem = verify_helpers.check_existence(title_key)
            title = verify_helpers.get_elems_texts(title_elem)

            food_list_elem = verify_helpers.check_existence(food_list_key)

            expected_title = verify_helpers.get_expected_texts(title_key)
            expected_btn_text = verify_helpers.get_expected_texts(after_review_btn_key)
            
            assert food_list_elem != None
            assert list(title[0])[-len(expected_title[0]):] == list(expected_title[0])
            assert btn_text == expected_btn_text

            LogUtils.log_success()

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

            LogUtils.log_success()

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
            web_utils.login(login_data["no_review_email"], login_data["password"])

            web_utils.click_tab_history()
            web_utils.click_element(*LOCATORS.get("history_pg_btn_back"))

            title_elem = verify_helpers.check_existence(title_key)
            title = verify_helpers.get_elems_texts(title_elem)

            expected_title = verify_helpers.get_expected_texts(title_key)
            
            assert not "history" in driver.current_url
            assert list(title[0])[-len(expected_title[0]):] == list(expected_title[0])

            LogUtils.log_success()

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
            web_utils.login(login_data["no_review_email"], login_data["password"])

            web_utils.click_tab_history()

            cnt = []
            try:
                for _ in range(3):
                    cnt_list = verify_helpers.cnt_elements(food_list_key)
                    cnt.append(cnt_list)

                    web_utils.scroll_to_element(*LOCATORS.get("history_pg_list_10"))
                    print("스크롤")
                    time.sleep(3)   # 없으면 오류남
            except:
                print("스크롤 완료")         
            
            assert cnt[0] == 10
            assert cnt[1] == 20
            assert cnt[2] <= 30

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [히스토리 페이지] "추천 후기 등록하기 버튼" 확인
    @pytest.mark.skip(reason="test pass")
    def test_history_009(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            radio_btns_keys = ["review_pg_btn_radio_alone", "review_pg_btn_radio_group", "review_pg_btn_radio_team"]
            menu_input_key = ["review_pg_input_menu"]
            category_key = ["review_pg_drop_down_category"]

            web_utils.open_url()
            web_utils.login(login_data["no_review_email"], login_data["password"])

            web_utils.click_tab_history()            
            verify_helpers.click_elem_with_infinity_scroll(By.CSS_SELECTOR, 'button.bg-main-black')
            
            radio_btns_elems = verify_helpers.check_existence(radio_btns_keys)
            menu_input_elem = verify_helpers.check_existence(menu_input_key)

            category_elem = verify_helpers.check_existence(category_key)
            category_text = verify_helpers.get_elems_texts(category_elem)

            assert radio_btns_elems[0].get_attribute("aria-checked") == "true"  or radio_btns_elems[1].get_attribute("aria-checked") =="true" or radio_btns_elems[2].get_attribute("aria-checked") == "true"
            assert menu_input_elem[0].get_attribute("value") != ""
            assert category_text != ""

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# [히스토리 페이지] 후기 등록
    @pytest.mark.skip(reason="test pass")
    def test_history_010(self, driver):
        try:
            web_utils = WebUtils(driver)
            verify_helpers = VerifyHelpers(driver)

            after_review_btn_key = ["history_pg_btn_after_review"]
 
            web_utils.open_url()
            web_utils.login(login_data["review_email"], login_data["password"])
            
            web_utils.click_tab_history()
            before_btn_index = verify_helpers.click_elem_with_infinity_scroll(By.CSS_SELECTOR, 'button.bg-main-black')    

            web_utils.review_image_upload()
            time.sleep(2)   # 없으면 에러남
            driver.find_element(By.CLASS_NAME, 'resize-none').send_keys(review_data["review"])
            web_utils.star_review_four_click()
            web_utils.review_completed()
            time.sleep(2)

            all_btns = driver.find_elements(By.TAG_NAME, "button")
            clicked_btn_elem = all_btns[before_btn_index]
            after_btn_text = clicked_btn_elem.text

            expected_text = verify_helpers.get_expected_texts(after_review_btn_key)

            assert after_btn_text == expected_text[0]
              
            LogUtils.log_success()

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

            web_utils.open_url()
            web_utils.login(login_data["review_email"], login_data["password"])

            web_utils.click_tab_history()

            time.sleep(2)

            verify_helpers.click_elem_with_infinity_scroll(By.CSS_SELECTOR, 'button.bg-main') # 로케이터 쓰면 못찾음

            with pytest.raises(TimeoutException):
                verify_helpers.check_existence(exit_btn_key)

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
