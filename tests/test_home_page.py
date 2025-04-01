import random
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.utils.helpers import WebUtils, VerifyHelpers
from src.utils.locators import LOCATORS
from src.utils.log_util import LogUtils
from src.resources.testdata.user_data import login_data
from src.pages.home_page import HomePage, SelectOptionPage, RecommendationPage


@pytest.mark.usefixtures("driver")
class TestHomePage:

    # [홈 페이지] UI 확인
    def test_home_001(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
        
            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("header_text"))
            
            # Expected Result
            assert verify.get_elem_text(*LOCATORS.get("header_text")) == "오늘 뭐먹지 ?"
            assert verify.get_elem_text(*LOCATORS.get("ai_recommendation_text")) == "💻 AI를 통해 음식 메뉴를 추천 받아 보세요!"
            assert verify.get_elem_text(*LOCATORS.get("eat_alone_btn")) == "혼자 먹기"
            assert verify.get_elem_text(*LOCATORS.get("eat_together_text")) == "같이 먹기"
            assert verify.get_elem_text(*LOCATORS.get("eat_team_text")) == "회식 하기"
            assert verify.get_elem_text(*LOCATORS.get("employee_preference_text")) == "🍽️ 직원들이 가장 선호하는 음식 종류는 무엇일까요?"
            assert driver.find_element(*LOCATORS.get("preference_analysis_chart")).is_displayed()
            assert verify.get_elem_text(*LOCATORS.get("menu_suggestion_text")) == "메뉴 추천"
            assert verify.get_elem_text(*LOCATORS.get("menu_suggestion_subtext")) == "오늘은 이런 메뉴는 어떠세요?"
            assert verify.get_elem_text(*LOCATORS.get("my_preference_text")) == "💁🏻‍♂️ 나의 취향 분석"
            assert verify.get_elem_text(*LOCATORS.get("my_preference_subtext")) == "AI가 분석한 취향 데이터입니다."
            assert driver.find_element(*LOCATORS.get("navigation_bar")).is_displayed()
            assert driver.find_element(*LOCATORS.get("navigation_home_icon")).value_of_css_property("color") == "rgba(255, 77, 77, 1)"
            assert driver.find_element(*LOCATORS.get("navigation_home_text")).value_of_css_property("color") == "rgba(255, 77, 77, 1)"
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    # [혼자 먹기] [추천 옵션 선택 페이지] 진입하여 UI 확인
    def test_home_002(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            
            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_alone_btn"))

            # Steps
            home.open_eat_alone()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')
            
            # Expected Result
            assert verify.get_elem_text(*LOCATORS.get("header_text")) == "추천 옵션 선택"
            assert verify.get_elem_text(*LOCATORS.get("select_category_text")) == "🍽️ 추천 받고자하는 음식 카테고리"
            assert verify.get_elem_text(*LOCATORS.get("dropdown_text")) == "음식 카테고리를 설정해주세요"
            assert verify.get_elem_text(*LOCATORS.get("eating_people_text")) == "🙌 먹는 인원"
            assert driver.find_element(*LOCATORS.get("profile_image")).is_displayed()
            assert driver.find_element(*LOCATORS.get("profile_name")).is_displayed()
            assert driver.find_element(*LOCATORS.get("profile_team")).is_displayed()
            assert driver.find_element(*LOCATORS.get("done_btn")).get_attribute("disabled") is not None
            assert driver.find_element(*LOCATORS.get("navigation_bar")).is_displayed()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    # [혼자 먹기] [추천 옵션 선택 페이지] 뒤로 가기 확인
    def test_home_003(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_alone_btn"))
            home.open_eat_alone()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')

            # Steps
            util.click_back()

            # Expected Result
            assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com"
            assert driver.find_element(*LOCATORS.get("eat_alone_btn")).is_displayed()
            assert driver.find_element(*LOCATORS.get("eat_together_btn")).is_displayed()
            assert driver.find_element(*LOCATORS.get("eat_team_btn")).is_displayed()
            assert driver.find_element(*LOCATORS.get("navigation_home_icon")).value_of_css_property("color") == "rgba(255, 77, 77, 1)"
            assert driver.find_element(*LOCATORS.get("navigation_home_text")).value_of_css_property("color") == "rgba(255, 77, 77, 1)"

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
        
    # [혼자 먹기] [추천 옵션 선택 페이지]의 음식 카테고리 드롭다운 확인
    def test_home_004(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_alone_btn"))
            home.open_eat_alone()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            # Steps
            select_option.click_category_dropdown()
            options = driver.find_elements(*LOCATORS.get("options"))
            actual_options = [opt.text.strip() for opt in options]
            expected_options = ["한식", "중식", "양식", "일식", "분식", "아시안", "패스트푸드", "기타"]
            
            # Expected Result
            assert len(options) > 0
            assert set(actual_options) == set(expected_options), f"드롭다운 옵션 불일치: {actual_options}"
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
        
    # [혼자 먹기] [추천 옵션 선택 페이지]의 음식 카테고리 드롭다운 선택
    def test_home_005(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_alone_btn"))
            home.open_eat_alone()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            # Steps
            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            selected_option_text = driver.find_element(*LOCATORS.get("selected_option_text"))
            dropdown_text = driver.find_element(*LOCATORS.get("dropdown_text")).text.strip()
            
            # Expected Result
            assert dropdown_text == selected_option_text
            assert driver.find_element(*LOCATORS.get("done_btn")).is_enabled()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    # [혼자 먹기] [메뉴 추천 페이지] 진입하여 UI 확인 - 맛집 리스트 출력
    def test_home_006(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            menu_rcm = RecommendationPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_alone_btn"))
            home.open_eat_alone()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))
            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            select_option.click_done_button()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')

            # Steps
            menu_rcm_text = verify.get_elem_text(*LOCATORS.get("menu_recommendation_text"))
            menu_text = verify.get_elem_text(*LOCATORS.get("menu_text"))
            percentage = float(verify.get_elem_text(*LOCATORS.get("ai_analysis_percentage")).replace("%", ""))
            restaurant_list = driver.find_elements(*LOCATORS.get("restaurant_list"))

            # Expected Result
            assert verify.get_elem_text(*LOCATORS.get("header_text")) == "메뉴 추천"
            assert menu_rcm_text == f"오늘 메뉴는 {menu_text} 어떠세요?"
            assert driver.find_element(*LOCATORS.get("food_image")).is_displayed()
            assert verify.get_elem_text(*LOCATORS.get("ai_analysis_text")) == "💻 AI가 분석한 취향 적합률"
            assert driver.find_element(*LOCATORS.get("ai_analysis_percentage")).is_displayed()
            assert 0 < percentage < 100
            assert verify.get_elem_text(*LOCATORS.get("restaurant_list_text")) == f"🍽️ {menu_text}에 해당하는 맛집 리스트"
            assert len(restaurant_list) > 0
            assert driver.find_element(*LOCATORS.get("refresh_recommendation_btn")).is_enabled()
            assert driver.find_element(*LOCATORS.get("accept_recommendation_btn")).is_enabled()
            assert driver.find_element(*LOCATORS.get("navigation_bar")).is_displayed()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    # [혼자 먹기] [메뉴 추천 페이지] 진입하여 UI 확인 - 검색 결과 없음
    def test_home_007(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            menu_rcm = RecommendationPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_alone_btn"))
            home.open_eat_alone()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))
            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            select_option.click_done_button()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')

            # Steps
            menu_rcm_text = verify.get_elem_text(*LOCATORS.get("menu_recommendation_text"))
            menu_text = verify.get_elem_text(*LOCATORS.get("menu_text"))
            percentage = float(verify.get_elem_text(*LOCATORS.get("ai_analysis_percentage")).replace("%", ""))

            # Expected Result
            assert verify.get_elem_text(*LOCATORS.get("header_text")) == "메뉴 추천"
            assert menu_rcm_text == f"오늘 메뉴는 {menu_text} 어떠세요?"
            assert driver.find_element(*LOCATORS.get("food_image")).is_displayed()
            assert verify.get_elem_text(*LOCATORS.get("ai_analysis_text")) == "💻 AI가 분석한 취향 적합률"
            assert driver.find_element(*LOCATORS.get("ai_analysis_percentage")).is_displayed()
            assert 0 < percentage < 100
            assert verify.get_elem_text(*LOCATORS.get("restaurant_list_text")) == f"🍽️ {menu_text}에 해당하는 맛집 리스트"
            assert driver.find_element(*LOCATORS.get("no_search_result_section")).is_displayed()
            assert verify.get_elem_text(*LOCATORS.get("no_search_result_text")) == "검색 결과가 없습니다!"
            assert driver.find_element(*LOCATORS.get("no_search_result_image")).is_displayed()

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    # [혼자 먹기] [메뉴 추천 페이지] 뒤로 가기 확인
    def test_home_008(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_alone_btn"))
            home.open_eat_alone()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))
            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            select_option.click_done_button()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')

            # Steps
            util.click_back()

            # Expected Result
            assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone"
            assert verify.get_elem_text(*LOCATORS.get("dropdown_text")) == "음식 카테고리를 설정해주세요"
            assert driver.find_element(*LOCATORS.get("done_btn")).get_attribute("disabled") is not None

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    # [혼자 먹기] [메뉴 추천 페이지] 메뉴 다시 추천 받기 확인
    def test_home_009(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            menu_rcm = RecommendationPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_alone_btn"))
            home.open_eat_alone()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))
            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            select_option.click_done_button()
            util.wait_for_element_presence(*LOCATORS.get("food_image"))

            # Steps
            previous_menu = driver.find_element(*LOCATORS.get("menu_text")).text.strip()
            util.scroll_to_element(*LOCATORS.get("refresh_recommendation_btn"))
            util.click_element(*LOCATORS.get("refresh_recommendation_btn"))
            driver.execute_script("window.scrollTo(0, 0);")
            new_menu = driver.find_element(*LOCATORS.get("menu_text")).text.strip()

            # Expected Result
            assert previous_menu != new_menu

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    # [혼자 먹기] [메뉴 추천 페이지] 추천 받은 메뉴 수락 확인
    def test_home_010(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            menu_rcm = RecommendationPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_alone_btn"))
            home.open_eat_alone()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))
            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            selected_option_text = driver.find_element(By.CSS_SELECTOR, "span[style='pointer-events: none;']").text.strip()
            select_option.click_done_button()
            util.wait_for_element_presence(*LOCATORS.get("food_image"))

            # Steps
            menu = verify.get_elem_text(*LOCATORS.get("menu_text"))
            food_image = driver.find_element(*LOCATORS.get("food_image")).get_attribute("src")
            util.scroll_to_element(*LOCATORS.get("accept_recommendation_btn"))
            util.click_element(*LOCATORS.get("accept_recommendation_btn"))
            util.wait_for_element_presence(*LOCATORS.get("history_food_image"))
            driver.execute_script("window.scrollTo(0, 0);")

            # Expected Result
            assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/history"
            assert driver.find_element(*LOCATORS.get("history_food_image")).get_attribute("src") == food_image
            assert verify.get_elem_text(*LOCATORS.get("history_tag"))[0] == "혼밥"
            assert verify.get_elem_text(*LOCATORS.get("history_tag"))[1] == selected_option_text
            assert verify.get_elem_text(*LOCATORS.get("history_menu_text")) == menu

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    # [혼자 먹기] [메뉴 추천 페이지] [추천 히스토리 페이지] 뒤로 가기 확인
    def test_home_011(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            menu_rcm = RecommendationPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_alone_btn"))
            home.open_eat_alone()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))
            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            select_option.click_done_button()
            util.wait_for_element_presence(*LOCATORS.get("food_image"))
            util.scroll_to_element(*LOCATORS.get("accept_recommendation_btn"))
            menu_rcm.click_accept_recommendation_button()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')

            # Steps
            util.click_back()

            # Expected Result
            assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/recommendation"
            assert driver.find_element(*LOCATORS.get("refresh_recommendation_btn")).is_enabled()
            assert driver.find_element(*LOCATORS.get("accept_recommendation_btn")).is_enabled()

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    # [같이 먹기] [추천 옵션 선택 페이지] 진입하여 UI 확인
    def test_home_012(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_together_btn"))

            # Steps
            home.open_eat_together()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(*LOCATORS.get("user_list"))
            random_user = random.choice(user_list)
            
            # Expected Result
            assert verify.get_elem_text(*LOCATORS.get("header_text")) == "추천 옵션 선택"
            assert verify.get_elem_text(*LOCATORS.get("select_category_text")) == "🍽️ 추천 받고자하는 음식 카테고리"
            assert verify.get_elem_text(*LOCATORS.get("dropdown_text")) == "음식 카테고리를 설정해주세요"
            assert verify.get_elem_text(*LOCATORS.get("eating_people_text")) == "🙌 먹는 인원"
            assert driver.find_element(*LOCATORS.get("division")).is_displayed()
            assert driver.find_element(*LOCATORS.get("search_field")).is_displayed()
            assert len(user_list) > 0
            assert random_user.find_element(*LOCATORS.get("profile_image")).is_displayed()
            assert random_user.find_element(*LOCATORS.get("profile_name")).is_displayed()
            assert random_user.find_element(*LOCATORS.get("profile_team")).is_displayed()
            assert random_user.find_element(*LOCATORS.get("profile_checkbox")).is_displayed()
            assert driver.find_element(*LOCATORS.get("done_btn")).get_attribute("disabled") is not None
            assert driver.find_element(*LOCATORS.get("navigation_bar")).is_displayed()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_013(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_together_btn"))

            home.open_eat_together()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')

            util.click_back()
            assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/"
            assert driver.find_element(*LOCATORS.get("eat_alone_btn")).is_displayed()
            assert driver.find_element(*LOCATORS.get("eat_together_btn")).is_displayed()
            assert driver.find_element(*LOCATORS.get("eat_team_btn")).is_displayed()
            navigation_home_icon_color = driver.find_element(*LOCATORS.get("navigation_home_icon")).value_of_css_property("color")
            navigation_home_text_color = driver.find_element(*LOCATORS.get("navigation_home_text")).value_of_css_property("color")
            assert navigation_home_icon_color == "rgba(255, 77, 77, 1)"
            assert navigation_home_text_color == "rgba(255, 77, 77, 1)"

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
        

    def test_home_014(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_together_btn"))

            home.open_eat_together()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            options = driver.find_elements(*LOCATORS.get("options"))

            actual_options = [opt.text.strip() for opt in options]
            expected_options = ["한식", "중식", "양식", "일식", "분식", "아시안", "패스트푸드", "기타"]

            assert set(actual_options) == set(expected_options), f"드롭다운 옵션 불일치: {actual_options}"
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
        
    
    def test_home_015(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_together_btn"))

            home.open_eat_together()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            
            selected_option_text = driver.find_element(By.CSS_SELECTOR, "span[style='pointer-events: none;']").text.strip()
            dropdown_text = driver.find_element(*LOCATORS.get("dropdown_text")).text.strip()
            
            assert selected_option_text == dropdown_text
            assert driver.find_element(*LOCATORS.get("done_btn")).get_attribute("disabled") is not None
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_016(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_together_btn"))

            home.open_eat_together()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(*LOCATORS.get("user_list"))
            random_user = random.choice(user_list)
            random_user = wait(driver, 10).until(
                EC.element_to_be_clickable(random_user)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", random_user)
            driver.execute_script("arguments[0].click();", random_user)
            
            assert driver.find_element(*LOCATORS.get("profile_image")).is_displayed()
            assert driver.find_element(*LOCATORS.get("profile_name")).is_displayed()
            assert driver.find_element(*LOCATORS.get("profile_team")).is_displayed()
            assert driver.find_element(*LOCATORS.get("profile_cancel_btn")).is_displayed()

            assert driver.find_element(*LOCATORS.get("done_btn")).is_enabled()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_017(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_together_btn"))

            home.open_eat_together()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(*LOCATORS.get("user_list"))
            random_user_name = random.choice(user_list).find_element(*LOCATORS.get("profile_name")).text.strip()
            
            driver.find_element(*LOCATORS.get("search_field")).send_keys(random_user_name)
            assert driver.find_element(*LOCATORS.get("searched_user")).is_displayed()
            assert driver.find_element(*LOCATORS.get("searched_profile_image")).is_displayed()
            assert driver.find_element(*LOCATORS.get("searched_profile_name")).text == random_user_name
            assert driver.find_element(*LOCATORS.get("searched_profile_team")).is_displayed()
            
            util.click_element(*LOCATORS.get("searched_user_first_one"))
            assert driver.find_element(*LOCATORS.get("profile_image")).is_displayed()
            assert driver.find_element(*LOCATORS.get("profile_name")).text == random_user_name
            assert driver.find_element(*LOCATORS.get("profile_team")).is_displayed()
            assert driver.find_element(*LOCATORS.get("profile_cancel_btn")).is_displayed()

            assert driver.find_element(*LOCATORS.get("search_field")).get_attribute("value") == ""
            
            assert driver.find_element(*LOCATORS.get("done_btn")).is_enabled()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_018(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_together_btn"))

            home.open_eat_together()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(*LOCATORS.get("user_list"))
            random_user = random.choice(user_list)
            random_user = wait(driver, 10).until(
                EC.element_to_be_clickable(random_user)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", random_user)
            driver.execute_script("arguments[0].click();", random_user)
            
            driver.execute_script("window.scrollTo(0, 0);")
            util.click_element(*LOCATORS.get("profile_cancel_btn"))

            util.wait_for_element_invisible(*LOCATORS.get("eating_people_profie_image"))

            assert driver.find_element(*LOCATORS.get("done_btn")).get_attribute("disabled") is not None
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    
    def test_home_019(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            menu_rcm = RecommendationPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_together_btn"))

            home.open_eat_together()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(*LOCATORS.get("user_list"))
            random_user = random.choice(user_list)
            random_user = wait(driver, 10).until(
                EC.element_to_be_clickable(random_user)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", random_user)
            driver.execute_script("arguments[0].click();", random_user)

            select_option.click_done_button()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')

            header_text = driver.find_element(*LOCATORS.get("header_text")).text.strip()
            assert header_text == "메뉴 추천"
            
            menu_rcm_text = driver.find_element(*LOCATORS.get("menu_recommendation_text")).text.strip()
            menu_text = driver.find_element(*LOCATORS.get("menu_text")).text.strip()
            assert menu_rcm_text == f"오늘 메뉴는 {menu_text} 어떠세요?"

            assert driver.find_element(*LOCATORS.get("food_image")).is_displayed()

            ai_analysis_text = driver.find_element(*LOCATORS.get("ai_analysis_text")).text.strip()
            assert ai_analysis_text == "💻 AI가 분석한 취향 적합률"

            percentage = driver.find_element(*LOCATORS.get("ai_analysis_percentage"))
            assert percentage.is_displayed()
            
            percentage = float(percentage.text.strip().replace("%", ""))
            assert 0 < percentage < 100

            restaurant_list_text = driver.find_element(*LOCATORS.get("restaurant_list_text")).text.strip()
            assert restaurant_list_text == f"🍽️ {menu_text}에 해당하는 맛집 리스트"
            
            if len(driver.find_elements(*LOCATORS.get("no_search_result_section"))) > 0:
                assert driver.find_element(*LOCATORS.get("no_search_result_text")).text.strip() == "검색 결과가 없습니다!"
                assert driver.find_element(*LOCATORS.get("no_search_result_image")).is_displayed()
            else:
                restaurant_list = driver.find_elements(*LOCATORS.get("restaurant_list"))
                assert len(restaurant_list) > 0
                assert driver.find_element(*LOCATORS.get("restaurant_list_page")).is_displayed()
            
            assert driver.find_element(*LOCATORS.get("refresh_recommendation_btn")).is_enabled()

            assert driver.find_element(*LOCATORS.get("accept_recommendation_btn")).is_enabled()

            assert driver.find_element(*LOCATORS.get("navigation_bar")).is_displayed()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    #20


    def test_home_021(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_together_btn"))

            home.open_eat_together()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(*LOCATORS.get("user_list"))
            random_user = random.choice(user_list)
            random_user = wait(driver, 10).until(
                EC.element_to_be_clickable(random_user)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", random_user)
            driver.execute_script("arguments[0].click();", random_user)

            select_option.click_done_button()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')

            util.click_back()
            assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/together"

            dropdown_text = driver.find_element(*LOCATORS.get("dropdown_text")).text.strip()
            assert dropdown_text == "음식 카테고리를 설정해주세요"

            util.wait_for_element_invisible(*LOCATORS.get("eating_people_profie_image"))

            assert driver.find_element(*LOCATORS.get("done_btn")).get_attribute("disabled") is not None

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_022(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            menu_rcm = RecommendationPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_together_btn"))

            home.open_eat_together()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(*LOCATORS.get("user_list"))
            random_user = random.choice(user_list)
            random_user = wait(driver, 10).until(
                EC.element_to_be_clickable(random_user)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", random_user)
            driver.execute_script("arguments[0].click();", random_user)

            select_option.click_done_button()
            util.wait_for_element_presence(*LOCATORS.get("food_image"))

            previous_menu = driver.find_element(*LOCATORS.get("menu_text")).text.strip()
            util.scroll_to_element(*LOCATORS.get("refresh_recommendation_btn"))
            util.click_element(*LOCATORS.get("refresh_recommendation_btn"))
            util.wait_for_element_presence(*LOCATORS.get("food_image"))

            driver.execute_script("window.scrollTo(0, 0);")
            new_menu = driver.find_element(*LOCATORS.get("menu_text")).text.strip()

            assert previous_menu != new_menu

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    
    def test_home_023(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            menu_rcm = RecommendationPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_together_btn"))

            home.open_eat_together()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            selected_option_text = driver.find_element(By.CSS_SELECTOR, "span[style='pointer-events: none;']").text.strip()

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(*LOCATORS.get("user_list"))
            random_user = random.choice(user_list)
            random_user = wait(driver, 10).until(
                EC.element_to_be_clickable(random_user)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", random_user)
            driver.execute_script("arguments[0].click();", random_user)

            select_option.click_done_button()
            util.wait_for_element_presence(*LOCATORS.get("food_image"))

            menu = driver.find_element(*LOCATORS.get("menu_text")).text.strip()
            food_image = driver.find_element(*LOCATORS.get("food_image")).get_attribute("src")
            percentage = float(driver.find_element(*LOCATORS.get("ai_analysis_percentage")).text.strip().replace("%", ""))
            if percentage % 1 >= 0.5:
                percentage = int(percentage) + 1
            else:
                percentage = int(percentage)
            percentage = float(percentage)

            util.scroll_to_element(*LOCATORS.get("accept_recommendation_btn"))
            util.click_element(*LOCATORS.get("accept_recommendation_btn"))
            wait(driver, 5).until(
                lambda d: d.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/history"
            )

            driver.execute_script("window.scrollTo(0, 0);")
            assert driver.find_element(*LOCATORS.get("history_food_image")).get_attribute("src") == food_image
            assert driver.find_elements(*LOCATORS.get("history_tag"))[0].text.strip() == "그룹"
            assert driver.find_elements(*LOCATORS.get("history_tag"))[1].text.strip() == selected_option_text
            assert driver.find_element(*LOCATORS.get("history_menu_text")).text.strip() == menu
            assert float(driver.find_element(*LOCATORS.get("history_percentage")).text.strip().replace("%", "")) == percentage

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_024(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            menu_rcm = RecommendationPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_together_btn"))

            home.open_eat_together()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(*LOCATORS.get("user_list"))
            random_user = random.choice(user_list)
            random_user = wait(driver, 10).until(
                EC.element_to_be_clickable(random_user)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", random_user)
            driver.execute_script("arguments[0].click();", random_user)

            select_option.click_done_button()
            util.wait_for_element_presence(*LOCATORS.get("food_image"))

            util.scroll_to_element(*LOCATORS.get("refresh_recommendation_btn"))
            util.click_element(*LOCATORS.get("refresh_recommendation_btn"))
            util.wait_for_element_presence(*LOCATORS.get("food_image"))

            util.scroll_to_element(*LOCATORS.get("accept_recommendation_btn"))
            menu_rcm.click_accept_recommendation_button()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')

            util.click_back()
            assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/recommendation"
            assert driver.find_element(*LOCATORS.get("refresh_recommendation_btn")).is_enabled()
            assert driver.find_element(*LOCATORS.get("accept_recommendation_btn")).is_enabled()

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_025(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_team_btn"))

            home.open_eat_team()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')
            
            header_text = driver.find_element(*LOCATORS.get("header_text")).text.strip()
            assert header_text == "추천 옵션 선택"
            
            select_category_text = driver.find_element(*LOCATORS.get("select_category_text")).text.strip()
            assert select_category_text == "🍽️ 추천 받고자하는 음식 카테고리"

            dropdown_text = driver.find_element(*LOCATORS.get("dropdown_text")).text.strip()
            assert dropdown_text == "음식 카테고리를 설정해주세요"

            eating_people_text = driver.find_element(*LOCATORS.get("eating_people_text")).text.strip()
            assert eating_people_text == "🙌 먹는 인원"

            assert driver.find_element(*LOCATORS.get("team")).is_displayed()

            assert driver.find_element(*LOCATORS.get("done_btn")).get_attribute("disabled") is not None
            
            assert driver.find_element(*LOCATORS.get("navigation_bar")).is_displayed()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_026(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_team_btn"))

            home.open_eat_team()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')

            util.click_back()
            assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/"
            assert driver.find_element(*LOCATORS.get("eat_alone_btn")).is_displayed()
            assert driver.find_element(*LOCATORS.get("eat_together_btn")).is_displayed()
            assert driver.find_element(*LOCATORS.get("eat_team_btn")).is_displayed()
            navigation_home_icon_color = driver.find_element(*LOCATORS.get("navigation_home_icon")).value_of_css_property("color")
            navigation_home_text_color = driver.find_element(*LOCATORS.get("navigation_home_text")).value_of_css_property("color")
            assert navigation_home_icon_color == "rgba(255, 77, 77, 1)"
            assert navigation_home_text_color == "rgba(255, 77, 77, 1)"

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
        

    def test_home_027(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_team_btn"))

            home.open_eat_team()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            options = driver.find_elements(*LOCATORS.get("options"))

            actual_options = [opt.text.strip() for opt in options]
            expected_options = ["한식", "중식", "양식", "일식", "분식", "아시안", "패스트푸드", "기타"]

            assert set(actual_options) == set(expected_options), f"드롭다운 옵션 불일치: {actual_options}"
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
        
    
    def test_home_028(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_team_btn"))

            home.open_eat_team()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            
            selected_option_text = driver.find_element(By.CSS_SELECTOR, "span[style='pointer-events: none;']").text.strip()
            dropdown_text = driver.find_element(*LOCATORS.get("dropdown_text")).text.strip()
            
            assert selected_option_text == dropdown_text
            assert driver.find_element(*LOCATORS.get("done_btn")).is_enabled()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_029(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            menu_rcm = RecommendationPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_team_btn"))

            home.open_eat_team()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            select_option.click_done_button()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')

            header_text = driver.find_element(*LOCATORS.get("header_text")).text.strip()
            assert header_text == "메뉴 추천"
            
            menu_rcm_text = driver.find_element(*LOCATORS.get("menu_recommendation_text")).text.strip()
            menu_text = driver.find_element(*LOCATORS.get("menu_text")).text.strip()
            assert menu_rcm_text == f"오늘 메뉴는 {menu_text} 어떠세요?"

            assert driver.find_element(*LOCATORS.get("food_image")).is_displayed()

            ai_analysis_text = driver.find_element(*LOCATORS.get("ai_analysis_text")).text.strip()
            assert ai_analysis_text == "💻 AI가 분석한 취향 적합률"

            percentage = driver.find_element(*LOCATORS.get("ai_analysis_percentage"))
            assert percentage.is_displayed()
            
            percentage = float(percentage.text.strip().replace("%", ""))
            assert 0 < percentage < 100

            restaurant_list_text = driver.find_element(*LOCATORS.get("restaurant_list_text")).text.strip()
            assert restaurant_list_text == f"🍽️ {menu_text}에 해당하는 맛집 리스트"
            
            if len(driver.find_elements(*LOCATORS.get("no_search_result_section"))) > 0:
                assert driver.find_element(*LOCATORS.get("no_search_result_text")).text.strip() == "검색 결과가 없습니다!"
                assert driver.find_element(*LOCATORS.get("no_search_result_image")).is_displayed()
            else:
                restaurant_list = driver.find_elements(*LOCATORS.get("restaurant_list"))
                assert len(restaurant_list) > 0
                assert driver.find_element(*LOCATORS.get("restaurant_list_page")).is_displayed()
            
            assert driver.find_element(*LOCATORS.get("refresh_recommendation_btn")).is_enabled()

            assert driver.find_element(*LOCATORS.get("accept_recommendation_btn")).is_enabled()

            assert driver.find_element(*LOCATORS.get("navigation_bar")).is_displayed()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    
    def test_home_030(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_team_btn"))

            home.open_eat_team()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            select_option.click_done_button()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')

            util.click_back()
            assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"

            dropdown_text = driver.find_element(*LOCATORS.get("dropdown_text")).text.strip()
            assert dropdown_text == "음식 카테고리를 설정해주세요"

            assert driver.find_element(*LOCATORS.get("done_btn")).get_attribute("disabled") is not None

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_031(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            menu_rcm = RecommendationPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_team_btn"))

            home.open_eat_team()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            select_option.click_done_button()
            util.wait_for_element_presence(*LOCATORS.get("food_image"))

            previous_menu = driver.find_element(*LOCATORS.get("menu_text")).text.strip()
            util.scroll_to_element(*LOCATORS.get("refresh_recommendation_btn"))
            util.click_element(*LOCATORS.get("refresh_recommendation_btn"))
            util.wait_for_element_presence(*LOCATORS.get("food_image"))

            driver.execute_script("window.scrollTo(0, 0);")
            new_menu = driver.find_element(*LOCATORS.get("menu_text")).text.strip()

            assert previous_menu != new_menu

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    
    def test_home_032(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            menu_rcm = RecommendationPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_team_btn"))

            home.open_eat_team()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            selected_option_text = driver.find_element(By.CSS_SELECTOR, "span[style='pointer-events: none;']").text.strip()
            select_option.click_done_button()
            util.wait_for_element_presence(*LOCATORS.get("food_image"))

            menu = driver.find_element(*LOCATORS.get("menu_text")).text.strip()
            food_image = driver.find_element(*LOCATORS.get("food_image")).get_attribute("src")
            percentage = float(driver.find_element(*LOCATORS.get("ai_analysis_percentage")).text.strip().replace("%", ""))
            if percentage % 1 >= 0.5:
                percentage = int(percentage) + 1
            else:
                percentage = int(percentage)
            percentage = float(percentage)

            util.scroll_to_element(*LOCATORS.get("accept_recommendation_btn"))
            util.click_element(*LOCATORS.get("accept_recommendation_btn"))
            wait(driver, 5).until(
                lambda d: d.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/history"
            )

            driver.execute_script("window.scrollTo(0, 0);")
            assert driver.find_element(*LOCATORS.get("history_food_image")).get_attribute("src") == food_image
            assert driver.find_elements(*LOCATORS.get("history_tag"))[0].text.strip() == "회식"
            assert driver.find_elements(*LOCATORS.get("history_tag"))[1].text.strip() == selected_option_text
            assert driver.find_element(*LOCATORS.get("history_menu_text")).text.strip() == menu
            assert float(driver.find_element(*LOCATORS.get("history_percentage")).text.strip().replace("%", "")) == percentage

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_033(self, driver: WebDriver):
        try:
            # Settings
            util = WebUtils(driver)
            verify = VerifyHelpers(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)
            menu_rcm = RecommendationPage(driver)

            # Precondition
            util.open_url()
            util.login(login_data["no_review_email"], login_data["password"])
            util.wait_for_element_presence(*LOCATORS.get("eat_team_btn"))

            home.open_eat_team()
            util.wait_for_element_presence(*LOCATORS.get("dropdown"))

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            select_option.click_done_button()
            util.wait_for_element_presence(*LOCATORS.get("food_image"))

            util.scroll_to_element(*LOCATORS.get("accept_recommendation_btn"))
            menu_rcm.click_accept_recommendation_button()
            util.wait_for_element_presence(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')

            util.click_back()
            assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/recommendation"
            assert driver.find_element(*LOCATORS.get("refresh_recommendation_btn")).is_enabled()
            assert driver.find_element(*LOCATORS.get("accept_recommendation_btn")).is_enabled()

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise