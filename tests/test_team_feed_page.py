import time
import pytest
from src.utils.helpers import WebUtils
from src.pages.team_feed_page import TeamFeed
from src.utils.log_util import LogUtils
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestTeamFeedPage:
    #@pytest.mark.skip(reason="tested > passed")
    def test_team_001(self, driver:WebDriver):      # 팀 피드 진입 확인하기
        try:
            # Settings & Precondition & Steps - 테스트를 위한 세팅 및 팀 피드 진입 실행
            team_feed = TeamFeed(driver)
            team_feed.into_team_feed()

            # Expected Result - 팀 피드 페이지 정상 진입 확인 (페이지 타이틀, 콤보박스 - 팀 명 확인)
            assert "팀 피드" == driver.find_element(By.CSS_SELECTOR, ".font-bold.text-white.text-title").text, "❌ 페이지 타이틀이 올바르지 않습니다."
            print("✅ 페이지 타이틀이 올바르게 제공되었습니다.")

            assert "디자인 1팀" == driver.find_element(By.CSS_SELECTOR, "[style='pointer-events: none;']").text, "❌ 현재 팀 명이 내 팀명과 일치하지 않습니다."
            print("✅ 현재 팀 명이 내 팀명과 일치합니다.")
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    #@pytest.mark.skip(reason="tested > passed")
    def test_team_002(self, driver:WebDriver):      # 팀 피드 진입 후 뒤로가기 시 메인(홈)페이지로 이동 확인
       try:
            # Settings & Precondition & Steps - 테스트를 위한 세팅 및 팀 피드 진입 실행
            team_feed = TeamFeed(driver)
            webutils = WebUtils(driver)
            team_feed.into_team_feed()
            
            # Steps - 팀 피드 진입 상태에서 '뒤로 가기' 선택
            webutils.click_back()

            # Expected Result - 메인 페이지로 이동 확인
            assert "https://kdt-pt-1-pj-2-team03.elicecoding.com/" == driver.current_url, f"❌ 뒤로가기 시 올바른 URL로 이동되지 않았습니다.{driver.current_url}"
            print("✅ 뒤로가기 시 메인 페이지로 정상 이동되었습니다.")
            
            LogUtils.log_success()

       except Exception as e:
           LogUtils.log_error(e, driver)
           raise
      
    #@pytest.mark.skip(reason="tested > failed")
    def test_team_003(self, driver:WebDriver):      # 팀 피드 진입 후 팀 변경 > 뒤로 가기 시 내 팀 정보 제공되는지 확인
        try:
            # Settings - 테스트를 위한 세팅
            webutils = WebUtils(driver)
            team_feed = TeamFeed(driver)
        
            # Preconditions - 팀 피드 진입 후 내 팀 외 다른 팀 진입 (개발 1팀)
            team_feed.into_team_feed()
            ori_profile_team_name = driver.find_element(By.CSS_SELECTOR, ".px-2.py-1.rounded-lg.bg-sub-2").find_element(By.CLASS_NAME, "text-white").text
            ori_combo_team_name = driver.find_element(By.CSS_SELECTOR, "[style='pointer-events: none;']").text
            team_feed.open_team_combobox()
            team_feed.select_team_combobox(0)
            ws(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex.flex-col.w-full.gap-3")))            
            
            # Steps - 뒤로가기 실행
            webutils.click_back()
            
            # Expected Result - 프로필 / 콤보박스의 팀 이름이 원래대로 변경되었는지 검증
            cur_profile_team_name = driver.find_element(By.CSS_SELECTOR, ".px-2.py-1.rounded-lg.bg-sub-2").find_element(By.CLASS_NAME, "text-white").text
            cur_combo_team_name = driver.find_element(By.CSS_SELECTOR, "[style='pointer-events: none;']").text
            
            assert ori_profile_team_name == cur_profile_team_name, "❌ 프로필 영역의 팀 이름이 원래대로 변경되지 않았습니다."
            print("✅ 프로필 영역의 팀 이름이 원래대로 변경되었습니다.")

            assert ori_combo_team_name == cur_combo_team_name, "❌ 콤보박스의 팀 이름이 변경되지 않았습니다."
            print("✅ 콤보박스의 팀 이름이 원래대로 변경되었습니다.")
            
            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    #@pytest.mark.skip(reason="tested > passed")
    def test_team_005(self, driver:WebDriver):      # 내 팀 외 다른 팀(개발 1팀) 진입 시에 프로필 편집 버튼 미제공 확인
        try:
            # Settings & Precondition & Steps - 테스트를 위한 세팅 및 팀 피드 진입 실행
            team_feed = TeamFeed(driver)

            team_feed.into_team_feed()

            # Steps - 내 팀 외 다른 팀 진입 (개발 1팀)
            team_feed.open_team_combobox()
            team_feed.select_team_combobox(0)
            ws(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flex.flex-col.w-full.gap-3")))
            
            # Expected Results - 프로필 영역에 프로필 편집 버튼이 존재하지 않는지 확인하기
            profile_modi_button = driver.find_element(By.CSS_SELECTOR, ".flex.items-center.justify-between.text-subbody").find_elements(By.CLASS_NAME, "cursor-pointer")
            assert len(profile_modi_button) == 0, "❌ 프로필 편집 버튼이 존재합니다."
            print("✅ 프로필 편집 버튼이 존재하지 않습니다.")
            
            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    #@pytest.mark.skip(reason="tested > passed")
    def test_team_006(self, driver:WebDriver):      # 내 팀 선택 상태에서 프로필 수정 버튼 제공 확인
        try:
            # Settings - 테스트를 위한 세팅
            team_feed = TeamFeed(driver)
            webutils = WebUtils(driver)
            
            # Preconditions & Steps - 팀 피드 페이지 진입
            team_feed.into_team_feed()
            webutils.wait_for_element_presence(By.CSS_SELECTOR, ".flex.flex-col.gap-3") # 팀 프로필 영역 로드 대기
            
            # Expected Result - 프로필 수정 버튼 제공 확인 및 버튼 선택 시 팀 프로필 수정 모달 제공 확인
            assert driver.find_elements(By.CLASS_NAME, "cursor-pointer")[1] is not None, "❌ 프로필 편집 버튼이 존재하지 않습니다."
            print("✅ 프로필 편집 버튼이 정상 제공 되었습니다.")
            
            team_feed.click_modify_team_profile_icon()
            webutils.wait_for_element_presence(By.CSS_SELECTOR, ".text-main-black.font-semibold")
            assert "프로필 정보 수정" == driver.find_element(By.ID, "modal-root").find_element(By.CSS_SELECTOR, "span.text-main-black.font-semibold").text
            print("✅ 프로필 정보 수정 모달이 정상 제공되었습니다.")
            
            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    #@pytest.mark.skip(reason="tested > passed")
    def test_team_007(self, driver:WebDriver):      # 내 팀 외 다른 팀(개발 1팀) 진입 시에 팀이 먹은 메뉴 추가 버튼 미제공 확인
        try:
            # Settings - 테스트를 위한 세팅
            team_feed = TeamFeed(driver)
            webutils = WebUtils(driver)

            # precondition - 팀 피드 진입 상태
            team_feed.into_team_feed()

            # Steps
            # 내 팀 외 다른 팀 (개발 1팀) 진입
            team_feed.open_team_combobox()
            team_feed.select_team_combobox(0)
            
            # 팀이 먹은 메뉴 존재하는 위치로 스크롤
            webutils.scroll_to_element(By.XPATH, "//*[@id='root']/div[1]/main/section/section/div[2]/canvas")


            # Expected Result - 팀이 먹은 메뉴 추가 버튼 미제공 확인
            teams_menu_title_area = driver.find_element(By.CSS_SELECTOR, "div.flex.items-center.gap-4")
            assert len(teams_menu_title_area.find_elements(By.TAG_NAME, "button")) == 0, "❌ 팀이 먹은 메뉴 추가 버튼이 제공되었습니다."
            print("✅ 팀이 먹은 메뉴 추가 버튼이 제공되지 않았습니다.")

            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    #@pytest.mark.skip(reason="tested > passed")
    def test_team_008(self, driver:WebDriver):      # 내 팀 선택 상태에서 팀이 먹는 메뉴 추가 버튼 제공 확인
        try:
            # Settings - 테스트를 위한 세팅
            team_feed = TeamFeed(driver)
            webutils = WebUtils(driver)

            # Preconditions & Steps - 팀 피드 진입하여 팀이 먹은 메뉴 영역 확인
            team_feed.into_team_feed()
            webutils.wait_for_element_presence(By.CSS_SELECTOR, ".flex.flex-col.w-full.gap-3")  # 팀 프로필 영역 로드 대기
            driver.execute_script("window.scrollTo(0,600);")
            webutils.wait_for_element_presence(By.CSS_SELECTOR, ".flex.items-center.gap-4") # 팀이 먹은 메뉴 타이틀 영역 로드 대기
            webutils.wait_for_element_presence(By.CSS_SELECTOR, '.flex.w-full.gap-6.p-4.shadow-md.rounded-2xl')    # 팀이 먹은 메뉴 리스트 영역 로드 대기
            
            # Expected Result - 팀이 먹은 메뉴 추가 버튼 제공 확인
            assert driver.find_element(By.CSS_SELECTOR, ".flex.items-center.gap-4").find_element(By.CLASS_NAME,"cursor-pointer") is not None, "❌ 추가 버튼이 존재하지 않습니다."
        
            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    #@pytest.mark.skip(reason="tested > passed")
    def test_team_010(self, driver:WebDriver):      # 리뷰 32자 이상일 시 접기/펼치기 제공 여부 확인
        try:
            # Settings - 테스트를 위한 세팅
            team_feed = TeamFeed(driver)
            webutils = WebUtils(driver)
            actions = ActionChains(driver)

            # Preconditon - 팀 피드 진입
            team_feed.into_team_feed() 
            webutils.wait_for_element_presence(By.CSS_SELECTOR, ".flex.flex-col.w-full.gap-3")  # 팀 프로필 로드까지 대기
            
            # Steps
            # 1. 후기 텍스트 28자 초과 첫 후기 위치로 스크롤 및 요소 추출
            driver.execute_script("window.scrollTo(0,1500);")
            over_28_comment_area = driver.find_element(By.CSS_SELECTOR, "div.relative.cursor-pointer")
            
            # 2. 위에서 찾은 후기 코멘트 영역 요소 및 보여지고 있는 텍스트 추출 > 보여지는거보다 1글자 더 추출되고 있음
            over_28_folded_comment = over_28_comment_area.find_element(By.TAG_NAME, "p")
            folded_comment = driver.execute_script("""
                const element = arguments[0];
                const computedStyle = window.getComputedStyle(element);
                const text = element.innerText;

                // 캔버스 초기화
                const canvas = document.createElement('canvas');
                const context = canvas.getContext('2d');
                context.font = computedStyle.font;

                // 현재 요소의 너비 확인
                const elementWidth = element.getBoundingClientRect().width;

                // 텍스트 계산
                let visibleText = '';
                for (let i = 0; i < text.length; i++) {
                    const slice = text.slice(0, i + 1);
                    const textWidth = context.measureText(slice).width;

                    if (textWidth > elementWidth) {
                        break;  // 요소 너비를 초과하면 중단
                    }

                    visibleText = slice;
                }

                return visibleText.trim(); // 보이는 텍스트 반환
            """, over_28_folded_comment)

            # Expected Result - 접힘 상태에서 32자보다 글자 수 더 보여지지 않는지 / 코멘트 영역 클릭 시 전체 내용 제공되는 지 확인
            assert len(folded_comment) <= 33, "❌ 리뷰 텍스트가 접힘 상태에서 32자보다 더 보여지고 있습니다."
            print("✅ 리뷰 텍스트가 접힘 상태에서 32자 이하로 보여지고 있습니다.")

            actions.move_to_element(over_28_folded_comment).click().perform()
            webutils.wait_for_element_presence(By.CSS_SELECTOR, "p.pr-3.text-description")
            over_28_opened_comment = over_28_comment_area.find_element(By.CSS_SELECTOR, "p.pr-3.text-description")
            opened_comment = driver.execute_script("return arguments[0].innerText;", over_28_opened_comment)
            assert opened_comment == over_28_opened_comment.text, "❌ 리뷰 전체 내용과 펼치기 상태에서 보여지는 내용이 상이합니다."
            print("✅ 리뷰 전체 내용과 펼치기 상태에서 보여지는 내용이 동일합니다.")
            
            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    #@pytest.mark.skip(reason="tested > passed")
    def test_team_018(self, driver:WebDriver):      # 팀 프로필 수정 내용 저장 시 프로필 영역 반영되는 지 확인
        try:
            # Settings - 테스트 실행을 위한 세팅
            team_feed = TeamFeed(driver)
            webutils = WebUtils(driver)

            # Precondition - 팀 피드 진입 후 프로필 수정 아이콘 선택하여 프로필 수정 모달 진입
            team_feed.into_team_feed()
            team_feed.click_modify_team_profile_icon()

            # Steps
            webutils.wait_for_element_presence(By.TAG_NAME, "form") # 모달 내 정보 수정 폼 나타날 때까지 대기

            # 모달 슬라이더 영역 정의
            in_modal_slider_area = driver.find_element(By.ID, "modal-root").find_element(By.CLASS_NAME, "space-y-6")

            webutils.slider_sweet() # 단 맛 : 2.5 설정
            webutils.slider_salty() # 짠 맛 : 2.5 설정
            webutils.slider_hot()   # 매운 맛 : 2.5 설정 

            # 값 비교를 위한 프로필 수정 영역 내용 추출 및 정의
            in_modal_sweet = in_modal_slider_area.find_elements(By.CSS_SELECTOR, ".w-8.text-right.text-gray-500.text-subbody")[0].text
            in_modal_salty = in_modal_slider_area.find_elements(By.CSS_SELECTOR, ".w-8.text-right.text-gray-500.text-subbody")[1].text
            in_modal_hot = in_modal_slider_area.find_elements(By.CSS_SELECTOR, ".w-8.text-right.text-gray-500.text-subbody")[2].text
            in_modal_favor_text = "한식 양식 중식 일식 매운거 안 매운거 밥이나 면이나 아니면 떡"
            in_modal_hate_text = "너무 한쪽으로 맛이 치우쳐서 자극적인 건 좋아하지 않습니다."

            # 이런 음식은 좋아요 / 이런 음식은 싫어요 텍스트 입력
            team_feed.modify_team_favorite_text(in_modal_favor_text)
            team_feed.modify_team_hate_text(in_modal_hate_text)
            time.sleep(1)

            # 프로필 수정 완료 버튼 클릭
            team_feed.click_team_profile_modify_done()
            time.sleep(1)

            # 팀 프로필 정보 영역 정의
            team_profile_area = driver.find_element(By.CSS_SELECTOR, ".flex.flex-col.w-full.gap-3")

            # 팀 프로필 변경 후 내용 추출
            changed_sweet = team_profile_area.find_elements(By.CSS_SELECTOR, ".w-8.text-right.text-gray-500.text-subbody")[0].text
            changed_salty = team_profile_area.find_elements(By.CSS_SELECTOR, ".w-8.text-right.text-gray-500.text-subbody")[1].text
            changed_hot = team_profile_area.find_elements(By.CSS_SELECTOR, ".w-8.text-right.text-gray-500.text-subbody")[2].text
            changed_favor_text = team_profile_area.find_elements(By.TAG_NAME, "p")[0].text
            changed_hate_text = team_profile_area.find_elements(By.TAG_NAME, "p")[1].text

            # Expected Results - 모달 내에서 편집한 내용대로 팀 프로필 영역에 반영되어 있어야 함
            assert in_modal_sweet == changed_sweet, "❌ 단 맛 변경 내용이 반영되지 않았습니다."
            print("✅ 단 맛 변경 내용이 정상 반영되었습니다.")
            assert in_modal_salty == changed_salty, "❌ 짠 맛 변경 내용이 반영되지 않았습니다."
            print("✅ 짠 맛 변경 내용이 정상 반영되었습니다.")
            assert in_modal_hot   == changed_hot,   "❌ 매운 맛 변경 내용이 반영되지 않았습니다."
            print("✅ 매운 맛 변경 내용이 정상 반영되었습니다.")
            assert in_modal_favor_text == changed_favor_text, "❌ '이런 음식은 좋아요' 텍스트 변경 내용이 반영되지 않았습니다."
            print("✅ '이런 음식은 좋아요' 텍스트 변경 내용이 정상 반영되었습니다.")
            assert in_modal_hate_text == changed_hate_text, "❌ '이런 음식은 싫어요' 텍스트 변경 내용이 반영되지 않았습니다."
            print("✅ '이런 음식은 싫어요' 텍스트 변경 내용이 정상 반영되었습니다.")

            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    #@pytest.mark.skip(reason="tested > passed")
    def test_team_020(self, driver:WebDriver):    # 선호 텍스트 10자 미만일 때 저장 시도 시 Error Alert Text 제공하는지 확인
        try:
            # Settings - 테스트를 위한 세팅
            team_feed = TeamFeed(driver)
            webutils = WebUtils(driver)

            # Precondition - 팀 피드 진입하여 팀 프로필 수정 모달 진입
            team_feed.into_team_feed()
            team_feed.click_modify_team_profile_icon()

            # 모달 내 정보 수정 폼 나타날 때까지 대기
            webutils.wait_for_element_presence(By.TAG_NAME, "form")

            # Steps
            # 선호 텍스트 입력
            in_modal_favor_text = "면이나 떡"
            team_feed.modify_team_favorite_text(in_modal_favor_text)

            # 프로필 수정 완료 버튼 클릭
            team_feed.click_team_profile_modify_done()
            webutils.wait_for_element_presence(By.TAG_NAME, "p")    # 선호 텍스트 Error Alert Text 나타날때까지 대기

            # Expected Results - 저장 시도 시 선호 텍스트 입력 영역 하단에 Error Alert Text 제공되어야 함 (10자 이상 입력해주세요)
            error_alert_text = driver.find_element(By.ID, "modal-root").find_element(By.TAG_NAME, "p")

            assert error_alert_text.is_displayed, "❌ 선호 텍스트 - Error Alert Text가 제공되지 않았습니다."
            print("✅ 선호 텍스트 - Error Alert Text가 정상 제공되었습니다.")
            
            assert error_alert_text.text == "10자 이상 입력해주세요" , "❌ 선호 텍스트 - Error Alert Text의 문구가 스펙과 다르게 제공되었습니다."
            print("✅ 선호 텍스트 - Error Alert Text 문구가 스펙과 일치합니다.")

            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    #@pytest.mark.skip(reason="tested > passed")
    def test_team_021(self, driver:WebDriver):    # 비선호 텍스트 10자 미만일 때 저장 시도 시 Error Alert Text 제공하는지 확인
        try:
            # Settings - 테스트를 위한 세팅
            team_feed = TeamFeed(driver)
            webutils = WebUtils(driver)

            # Precondition - 팀 피드 진입하여 팀 프로필 수정 모달 진입
            team_feed.into_team_feed()
            team_feed.click_modify_team_profile_icon()

            webutils.wait_for_element_presence(By.TAG_NAME, "form")  # 모달 내 정보 수정 폼 나타날 때까지 대기

            # Steps
            # 비선호 텍스트 입력
            in_modal_hate_text = "양식 중식 싫어요"
            team_feed.modify_team_hate_text(in_modal_hate_text)   
            
            # 프로필 수정 완료 버튼 클릭
            team_feed.click_team_profile_modify_done()
            webutils.wait_for_element_presence(By.TAG_NAME, "p")    # 비선호 텍스트 Error Alert Text 나타날때까지 대기

            # Expected Results - 저장 시도 시 선호 텍스트 입력 영역 하단에 Error Alert Text 제공되어야 함 (10자 이상 입력해주세요)
            error_alert_text = driver.find_element(By.ID, "modal-root").find_element(By.TAG_NAME, "p")
            assert error_alert_text.is_displayed, "❌ 비선호 텍스트 - Error Alert Text가 제공되지 않았습니다."
            print("✅ 비선호 텍스트 - Error Alert Text가 정상 제공되었습니다.")
            assert error_alert_text.text == "10자 이상 입력해주세요" , "❌ 비선호 텍스트 - Error Alert Text의 문구가 스펙과 다르게 제공되었습니다."
            print("✅ 비선호 텍스트 - Error Alert Text 문구가 스펙과 일치합니다.")

            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    #@pytest.mark.skip(reason="tested > passed")
    def test_team_022(self, driver:WebDriver):    # 선호 / 비선호 텍스트 모두 10자 미만일 때 저장 시도 시 Error Alert Text 제공하는지 확인
        try:
            # Settings - 테스트를 위한 세팅
            team_feed = TeamFeed(driver)
            webutils = WebUtils(driver)

            # Preconditions - 팀 피드 진입 후 팀 프로필 수정 모달 진입
            team_feed.into_team_feed()
            team_feed.click_modify_team_profile_icon()

            webutils.wait_for_element_presence(By.TAG_NAME, "form") # 모달 내 정보 수정 폼 나타날 때까지 대기

            # Steps
            # 선호 / 비선호 텍스트 영역에 10자 미만 텍스트 입력
            in_modal_favor_text = "면이나 떡"
            in_modal_hate_text = "양식 중식 NO"
            team_feed.modify_team_favorite_text(in_modal_favor_text)
            team_feed.modify_team_hate_text(in_modal_hate_text)

            # 프로필 수정 완료 버튼 클릭
            team_feed.click_team_profile_modify_done()
            webutils.wait_for_element_presence(By.TAG_NAME, "p")    # Error Alert Text 나타날때까지 대기

            # Expected Results - 선호 / 비선호 텍스트 10자 미만일 때 저장 시도 시 각 입력란 하단에 Error Alert Text 제공되어야 함
            alerts = driver.find_element(By.ID, "modal-root").find_elements(By.CSS_SELECTOR, ".text-description")
            favor_alerts = alerts[0]
            hate_alerts = alerts[1]

            assert favor_alerts.is_displayed, "❌ 선호 텍스트 - Error Alert Text가 제공되지 않았습니다."
            print("✅ 선호 텍스트 - Error Alert Text가 정상 제공되었습니다.")
            
            assert favor_alerts.text == "10자 이상 입력해주세요" , "❌ 비선호 텍스트 - Error Alert Text의 문구가 스펙과 다르게 제공되었습니다."
            print("✅ 선호 텍스트 - Error Alert Text 문구가 스펙과 일치합니다.")
            
            assert hate_alerts.is_displayed, "❌ 비선호 텍스트 - Error Alert Text가 제공되지 않았습니다."
            print("✅ 비선호 텍스트 - Error Alert Text가 정상 제공되었습니다.")
            
            assert hate_alerts.text == "10자 이상 입력해주세요" , "❌ 비선호 텍스트 - Error Alert Text의 문구가 스펙과 다르게 제공되었습니다."
            print("✅ 비선호 텍스트 - Error Alert Text 문구가 스펙과 일치합니다.")

            LogUtils.log_success()

        except Exception as e:
           LogUtils.log_error(e, driver)
           raise

    def test_team_028(self,driver:WebDriver):   # 같이 먹은 메뉴 리스트 > 같은 메뉴 먹기 선택하여 또 먹은 후기 등록
        # Setting - 테스트를 위한 세팅
        team_feed = TeamFeed(driver)
        webutils = WebUtils(driver)

        # Precondition - 팀 피드 진입 및 팀이 먹은 메뉴 리스트 위치로 이동 > 같은 메뉴 먹기 선택하여 '또 먹은 후기 등록하기' 모달 진입입
        team_feed.into_team_feed()
        webutils.scroll_to_element(By.XPATH, "//*[@id='root']/div[1]/main/section/section/div[2]/canvas")
        time.sleep(1)
        webutils.wait_for_element_presence(By.CSS_SELECTOR, ".flex.w-full.gap-6.p-4.shadow-md.rounded-2xl")
        
        # 같은 메뉴 먹기 선택한 항목 값 추출
        selected_area = driver.find_element(By.CSS_SELECTOR, "div.flex.w-full.gap-6.p-4.shadow-md.rounded-2xl")
        selected_type = selected_area.find_element(By.CSS_SELECTOR, "div.inline-flex.inline-flex.items-center.px-2.py-1.rounded-full.text-xs.font-medium.bg-main.text-white").text
        selected_category = selected_area.find_element(By.CSS_SELECTOR, "div.inline-flex.items-center.px-2.py-1.rounded-full.text-xs.font-medium.bg-sub.text-white").text
        selected_menu = selected_area.find_element(By.CSS_SELECTOR, "div.font-bold").text

        driver.find_element(By.XPATH, "//*[@id='root']/div[1]/main/section/section/div[3]/div[2]/div[1]/div[2]/button").click()
        
        # 모달 내에 불러와진 수정 불가 값 추출
        modal = driver.find_element(By.ID, "modal-root")
        modal_selected_type = modal.find_element(By.CSS_SELECTOR, "button[role='radio'][aria-checked='true']").get_attribute("id")
        modal_selected_menu = modal.find_element(By.XPATH, "//*[@id='modal-root']/div/div[2]/section/form/div[4]/input").get_attribute("value")
        modal_selected_category = driver.find_element(By.CSS_SELECTOR, "#modal-root > div > div.flex-1.overflow-auto > section > form > div:nth-child(5) > button > span").text

        # 선택 항목과 모달 내의 내용 일치하는지 검증
        assert selected_type == modal_selected_type, "❌ 선택한 항목과 식사 유형이 상이합니다."
        print("✅ 선택한 항목과 식사 유형이 일치합니다.")
        assert selected_menu == modal_selected_menu, "❌ 선택한 항목과 메뉴명이 상이합니다."
        print("✅ 선택한 항목과 메뉴명이 일치합니다.")
        # assert selected_category == modal_selected_category, "❌ 선택한 항목과 카테고리명이 상이합니다."
        # print("✅ 선택한 항목과 카테고리명이 일치합니다.")

        # Steps
        # 1. 수정 가능 항목 수정하기
        webutils.ate_party()
        webutils.review_image_upload()
        driver.find_element(By.NAME, "comment").clear()
        webutils.review_comment_write("영업 종료하고\n레오니다스 사장님이랑 같이 참치회 먹었어요~\n완전 신선했는데 초장이랑 간장이랑만 먹어서 아쉽")
        webutils.star_review_four_click()

        # 2. 후기 작성 완료 버튼 선택
        webutils.review_completed()
        
        # Expected Result - 등록한 내용대로 후기 정상 작성완료되어야 함
        
# ==================================================== 여기부터 데모용 TC 코드입니다 ====================================================

    def for_demo_songyi(self,driver:WebDriver):   # 같이 먹은 메뉴 리스트 > 같은 메뉴 먹기 선택하여 또 먹은 후기 등록
        # Setting - 테스트를 위한 세팅
        team_feed = TeamFeed(driver)
        webutils = WebUtils(driver)

        # Precondition - 팀 피드 진입 및 팀이 먹은 메뉴 리스트 위치로 이동 > 같은 메뉴 먹기 선택하여 '또 먹은 후기 등록하기' 모달 진입입
        team_feed.into_team_feed()
        webutils.scroll_to_element(By.XPATH, "//*[@id='root']/div[1]/main/section/section/div[2]/canvas")
        time.sleep(1)
        webutils.wait_for_element_presence(By.CSS_SELECTOR, ".flex.w-full.gap-6.p-4.shadow-md.rounded-2xl")
        
        # 같은 메뉴 먹기 선택한 항목 값 추출
        selected_area = driver.find_element(By.CSS_SELECTOR, "div.flex.w-full.gap-6.p-4.shadow-md.rounded-2xl")
        selected_type = selected_area.find_element(By.CSS_SELECTOR, "div.inline-flex.inline-flex.items-center.px-2.py-1.rounded-full.text-xs.font-medium.bg-main.text-white").text
        selected_category = selected_area.find_element(By.CSS_SELECTOR, "div.inline-flex.items-center.px-2.py-1.rounded-full.text-xs.font-medium.bg-sub.text-white").text
        selected_menu = selected_area.find_element(By.CSS_SELECTOR, "div.font-bold").text

        driver.find_element(By.XPATH, "//*[@id='root']/div[1]/main/section/section/div[3]/div[2]/div[1]/div[2]/button").click()
        
        # 모달 내에 불러와진 수정 불가 값 추출
        modal = driver.find_element(By.ID, "modal-root")
        modal_selected_type = modal.find_element(By.CSS_SELECTOR, "button[role='radio'][aria-checked='true']").get_attribute("id")
        modal_selected_menu = modal.find_element(By.XPATH, "//*[@id='modal-root']/div/div[2]/section/form/div[4]/input").get_attribute("value")

        # 선택 항목과 모달 내의 내용 일치하는지 검증
        assert selected_type == modal_selected_type, "❌ 선택한 항목과 식사 유형이 상이합니다."
        print("✅ 선택한 항목과 식사 유형이 일치합니다.")
        assert selected_menu == modal_selected_menu, "❌ 선택한 항목과 메뉴명이 상이합니다."
        print("✅ 선택한 항목과 메뉴명이 일치합니다.")

        # Steps
        # 1. 수정 가능 항목 수정하기
        webutils.ate_party()
        webutils.review_image_upload()
        driver.find_element(By.NAME, "comment").clear()
        webutils.review_comment_write("영업 종료하고\n레오니다스 사장님이랑 같이 참치회 먹었어요~\n완전 신선했는데 초장이랑 간장이랑만 먹어서 아쉽")
        webutils.star_review_four_click()

        # 2. 후기 작성 완료 버튼 선택
        webutils.review_completed()

# ==================================================== 여기까지 데모 코드입니다. ====================================================