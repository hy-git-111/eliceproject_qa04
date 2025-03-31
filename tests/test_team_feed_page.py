import time
import pytest
from src.utils.helpers import WebUtils
from src.pages.team_feed_page import TeamFeed
from src.utils.log_util import LogUtils
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestTeamFeedPage:
    @pytest.mark.skip(reason="passed")
    def test_team_001(self, driver:WebDriver):
        try:
            # Settings & Precondition & Steps
            team_feed = TeamFeed(driver)
            team_feed.into_team_feed()

            # Expected Result
            assert "팀 피드" == driver.find_element(By.CSS_SELECTOR, ".font-bold.text-white.text-title").text, "❌ 페이지 타이틀이 올바르지 않습니다."
            print("✅ 페이지 타이틀이 올바르게 제공되었습니다.")

            assert "디자인 1팀" == driver.find_element(By.CSS_SELECTOR, "[style='pointer-events: none;']").text, "❌ 현재 팀 명이 내 팀명과 일치하지 않습니다."
            print("✅ 현재 팀 명이 내 팀명과 일치합니다.")
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    @pytest.mark.skip(reason="passed")
    def test_team_002(self, driver:WebDriver):
       try:
            # Settings & Precondition
            team_feed = TeamFeed(driver)
            webutils = WebUtils(driver)
            team_feed.into_team_feed()
            
            # Steps
            webutils.click_back()

            # Expected Result
            assert "https://kdt-pt-1-pj-2-team03.elicecoding.com/" == driver.current_url, f"❌ 뒤로가기 시 올바른 URL로 이동되지 않았습니다.{driver.current_url}"
            print("✅ 뒤로가기 시 메인 페이지로 정상 이동되었습니다.")
            
            LogUtils.log_success()

       except Exception as e:
           LogUtils.log_error(e, driver)
           raise

        
    @pytest.mark.skip(reason="failed")
    def test_team_003(self, driver:WebDriver):
        try:
            # Settings
            webutils = WebUtils(driver)
            team_feed = TeamFeed(driver)
        
            # Preconditions
            team_feed.into_team_feed()
            ori_profile_team_name = driver.find_element(By.CSS_SELECTOR, ".px-2.py-1.rounded-lg.bg-sub-2").find_element(By.CLASS_NAME, "text-white").text
            ori_combo_team_name = driver.find_element(By.CSS_SELECTOR, "[style='pointer-events: none;']").text
            team_feed.open_team_combobox()
            team_feed.select_team_combobox(0)   # 개발 1팀 선택
            ws(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex.flex-col.w-full.gap-3")))            
            
            # Steps
            webutils.click_back()
            cur_profile_team_name = driver.find_element(By.CSS_SELECTOR, ".px-2.py-1.rounded-lg.bg-sub-2").find_element(By.CLASS_NAME, "text-white").text
            cur_combo_team_name = driver.find_element(By.CSS_SELECTOR, "[style='pointer-events: none;']").text
            
            # Expected Result
            assert ori_profile_team_name == cur_profile_team_name, "❌ 프로필 영역의 팀 이름이 원래대로 변경되지 않았습니다."
            print("✅ 프로필 영역의 팀 이름이 원래대로 변경되었습니다.")

            assert ori_combo_team_name == cur_combo_team_name, "❌ 콤보박스의 팀 이름이 변경되지 않았습니다."
            print("✅ 콤보박스의 팀 이름이 원래대로 변경되었습니다.")
            
            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    @pytest.mark.skip(reason="postpone - 많은 요소 검증이어서 마지막에 요소별로 확인하는 코드 넣을 예정")
    def test_team_004(self, driver:WebDriver):
        try:
            # Settings
            team_feed = TeamFeed(driver)

            # Preconditions & Steps
            team_feed.into_team_feed()

            # Expected Result - 검증 요소가 너무 많아서 추후 작성 예정
            
            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    @pytest.mark.skip(reason="Pass")
    def test_team_005(self, driver:WebDriver):
        try:
            # Settings
            team_feed = TeamFeed(driver)
            
            
            # Preconditions
            team_feed.into_team_feed()
            
            # Steps
            team_feed.open_team_combobox()
            team_feed.select_team_combobox(0)
            ws(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex.flex-col.w-full.gap-3")))
            # Expected Results
            profile_modi_button = driver.find_element(By.CSS_SELECTOR, ".flex.items-center.justify-between.text-subbody").find_elements(By.CLASS_NAME, "cursor-pointer")
            assert len(profile_modi_button) == 0, "❌ 프로필 편집 버튼이 존재합니다."
            print("✅ 프로필 편집 버튼이 존재하지 않습니다.")
            
            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    @pytest.mark.skip(reason="pass")
    def test_team_006(self, driver:WebDriver):
        try:
            # Settings
            team_feed = TeamFeed(driver)
            
            # Preconditions & Steps
            team_feed.into_team_feed()
            ws(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flex.flex-col.gap-3")))   # 히스토리 존재 유무 확인
            
            # Expected Result
            assert driver.find_elements(By.CLASS_NAME, "cursor-pointer")[1] is not None, "❌ 프로필 편집 버튼이 존재하지 않습니다."
            print("✅ 프로필 편집 버튼이 정상 제공 되었습니다.")
            team_feed.select_modify_team_profile_icon()
            ws(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-main-black.font-semibold")))
            assert "프로필 정보 수정" == driver.find_element(By.ID, "modal-root").find_element(By.TAG_NAME, "span").text
            print("✅ 프로필 정보 수정 모달이 정상 제공되었습니다.")
            
            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    @pytest.mark.skip(reason="question - 요소가 없는데 있다고 나오고있어서 확인 필요")
    def test_team_007(self, driver:WebDriver):
        try:
            # Settings
            team_feed = TeamFeed(driver)
        
            # Preconditions & Steps
            team_feed.into_team_feed()
            team_feed.open_team_combobox()
            team_feed.select_team_combobox(0)
            driver.execute_script("window.scrollTo(0,600);")
            ws(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex.flex-col.w-full.gap-3")))            
            ws(driver, 5).until(EC.visibility_of_element_located, (By.CSS_SELECTOR, ".flex.items-center.gap-4"))
            ws(driver, 5).until(EC.visibility_of_element_located, (By.CSS_SELECTOR, '.flex.w-full.gap-6.p-4.shadow-md.rounded-2xl'))

            # Expected Result
            assert len(driver.find_element(By.CSS_SELECTOR, ".flex.items-center.gap-4").find_elements(By.CLASS_NAME,"cursor-pointer")) == 0, "❌ 추가 버튼이 존재합니다."
            
            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    @pytest.mark.skip(reason="pass")
    def test_team_008(self, driver:WebDriver):
        try:
            # Settings
            team_feed = TeamFeed(driver)
            
            # Preconditions & Steps
            team_feed.into_team_feed()
            ws(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex.flex-col.w-full.gap-3"))) # 팀 프로필 로드 확인
            driver.execute_script("window.scrollTo(0,600);")
            ws(driver, 5).until(EC.visibility_of_element_located, (By.CSS_SELECTOR, ".flex.items-center.gap-4"))    # 팀이 먹은 메뉴 타이틀 영역 확인
            ws(driver, 5).until(EC.visibility_of_element_located, (By.CSS_SELECTOR, '.flex.w-full.gap-6.p-4.shadow-md.rounded-2xl'))    # 팀 메뉴 히스토리 영역 제공 확인
            
            # Expected Result
            assert driver.find_element(By.CSS_SELECTOR, ".flex.items-center.gap-4").find_element(By.CLASS_NAME,"cursor-pointer") is not None, "❌ 추가 버튼이 존재하지 않습니다."
        
            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    @pytest.mark.skip(reason="making")
    def test_team_009(self, driver:WebDriver):
        try:
            # Settings & Preconditon
            team_feed = TeamFeed(driver)
            webutils = WebUtils(driver)
            team_feed.into_team_feed()
            ws(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex.flex-col.w-full.gap-3"))) # 팀 프로필 로드 확인인
            self.driver.execute_script("window.scrollTo(0,700);")    # 팀이 먹은 메뉴가 보이는 위치로 스크롤 이동
            ws(driver, 5).until(EC.visibility_of_element_located, (By.CSS_SELECTOR, '.flex.w-full.gap-6.p-4.shadow-md.rounded-2xl'))    # 팀 메뉴 히스토리 영역 제공 확인

            # Steps
            over28_comment_menu = driver.find_element(By.CSS_SELECTOR,)
            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    @pytest.mark.skip(reason="making")
    def test_team_018(self, driver:WebDriver):
        try:
            # Settings & Precondition
            team_feed = TeamFeed(driver)
            webutils = WebUtils(driver)

            team_feed.into_team_feed()
            team_feed.select_modify_team_profile_icon()

            team_feed.modify_team_sweet()
            team_feed.modify_team_salty()
            team_feed.modify_team_hot()
            time.sleep(5)

            team_feed.modify_team_favorite_text("한식 양식 중식 일식 매운거 안 매운거 밥이나 면이나 아니면 떡")
            team_feed.modify_team_hate_text("너무 한쪽으로 맛이 치우쳐서 자극적인 건 좋아하지 않습니다.")

            team_feed.click_team_profile_modify_done()
            time.sleep(2)

            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise            

    @pytest.mark.skip(reason="making")
    def test_team_024(self, driver:WebDriver):
        try:
            # Settings & Precondition
            team_feed = TeamFeed(driver)
            webutils = WebUtils(driver)

            team_feed.into_team_feed()
            ws(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex.flex-col.w-full.gap-3")))
            team_feed.click_add_team_menu()
            ws(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='modal-root']/div/div[1]/span"), "새로운 후기 등록하기"))

            webutils.ate_party()
            webutils.review_image_upload()
            webutils.review_title_write("참치회 모둠")
            webutils.category_japan_food()
            webutils.review_comment_write("무한리필이라 푸짐했고\n회가 너무 신선했어요 최고!")
            webutils.star_review_five_click()
            webutils.review_completed()
            time.sleep(10)
            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise