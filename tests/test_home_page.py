import random
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.utils.helpers import WebUtils
from src.pages.home_page import HomePage, SelectOptionPage, RecommendationPage
from src.utils.log_util import LogUtils


@pytest.mark.usefixtures("driver")
class TestHomePage:
    header_text_css_selector = "header span.text-title"
    ai_recommendation_text_css_selector = "p.text-body"
    eat_alone_text_css_selector = "div.flex.items-center:nth-of-type(1) p"
    eat_together_text_css_selector = "div.flex.items-center:nth-of-type(2) p"
    eat_team_text_css_selector = "div.flex.items-center:nth-of-type(3) p"
    employee_preference_text_css_selector = "span.text-body"
    preference_analysis_chart_css_selector = "canvas[role='img']"
    menu_recommendation_text_css_selector = "h1.text-body.text-sub-2"
    menu_recommendation_subtext_css_selector = "div.pb-4 > h2.text-lg.text-dark-gray"
    my_preference_text_css_selector = "span.text-body.font-bold.text-sub-2:not(.py-1)"
    my_preference_subtext_xpath = "//h2[contains(text(), '취향 데이터')]"
    navigation_bar_css_selector = "div.fixed.bottom-0"
    navigation_home_icon_css_selector = "a.text-main path"
    navigation_home_text_css_selector = "a.text-main span"

    select_category_text_css_selector = "span.font-bold.text-sub-2.text-title"
    eating_people_text_xpath = "//span[contains(text(), '인원')]"
    profile_image_css_selector = "img.aspect-square"
    profile_name_css_selector = "div.font-semibold"
    profile_team_css_selector = "div.text-gray-500"
    profile_checkbox_css_selector = "input[type='checkbox']"
    profile_cancel_btn_css_selector = "svg.absolute"
    team_css_selector = "div.bg-sub-2"
    division_css_selector = "div.border-t"
    search_field_css_selector = "input[type='text']"
    user_lists_css_selector = "div.flex.items-center.justify-between"
    searched_user_css_selector = "ul.absolute"
    searched_profile_image_css_selector = "img.rounded-full"
    searched_profile_name_tag_name = "h2"
    searched_profile_team_css_selector = "h2.text-subbody"


    def test_home_001(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.header_text_css_selector))
            )
            
            header_text = driver.find_element(By.CSS_SELECTOR, self.header_text_css_selector).text.strip()
            assert header_text == "오늘 뭐먹지 ?"
            
            ai_recommendation_text = driver.find_element(By.CSS_SELECTOR, self.ai_recommendation_text_css_selector).text.strip()
            assert ai_recommendation_text == "💻 AI를 통해 음식 메뉴를 추천 받아 보세요!"

            eat_alone_text = driver.find_element(By.CSS_SELECTOR, home.eat_alone_btn_css_selector).text.strip()
            eat_together_text = driver.find_element(By.CSS_SELECTOR, home.eat_together_btn_css_selector).text.strip()
            eat_team_text = driver.find_element(By.CSS_SELECTOR, home.eat_team_btn_css_selector).text.strip()
            assert eat_alone_text == "혼자 먹기"
            assert eat_together_text == "같이 먹기"
            assert eat_team_text == "회식 하기"

            employee_preference_text = driver.find_element(By.CSS_SELECTOR, self.employee_preference_text_css_selector).text.strip()
            assert employee_preference_text == "🍽️ 직원들이 가장 선호하는 음식 종류는 무엇일까요?"
    
            preference_analysis_chart = driver.find_element(By.CSS_SELECTOR, self.preference_analysis_chart_css_selector)
            assert preference_analysis_chart.is_displayed()

            menu_recommendation_text = driver.find_element(By.CSS_SELECTOR, self.menu_recommendation_text_css_selector).text.strip()
            assert menu_recommendation_text == "메뉴 추천"

            menu_recommendation_subtext = driver.find_element(By.CSS_SELECTOR, self.menu_recommendation_subtext_css_selector).text.strip()
            assert menu_recommendation_subtext == "오늘은 이런 메뉴는 어떠세요?"
            
            my_preference_text = driver.find_element(By.CSS_SELECTOR, self.my_preference_text_css_selector).text.strip()
            assert my_preference_text == "💁🏻‍♂️ 나의 취향 분석"
            
            my_preference_subtext = driver.find_element(By.XPATH, self.my_preference_subtext_xpath).text.strip()
            assert my_preference_subtext == "AI가 분석한 취향 데이터입니다."
            
            assert driver.find_element(By.CSS_SELECTOR, self.navigation_bar_css_selector).is_displayed()

            navigation_home_icon_color = driver.find_element(By.CSS_SELECTOR, self.navigation_home_icon_css_selector).value_of_css_property("color")
            navigation_home_text_color = driver.find_element(By.CSS_SELECTOR, self.navigation_home_text_css_selector).value_of_css_property("color")
            assert navigation_home_icon_color == "rgba(255, 77, 77, 1)"
            assert navigation_home_text_color == "rgba(255, 77, 77, 1)"
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    
    def test_home_002(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_alone_btn_css_selector))
            )

            home.open_eat_alone()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.rounded-full.cursor-pointer'))
            )
            
            header_text = driver.find_element(By.CSS_SELECTOR, self.header_text_css_selector).text.strip()
            assert header_text == "추천 옵션 선택"
            
            select_category_text = driver.find_element(By.CSS_SELECTOR, self.select_category_text_css_selector).text.strip()
            assert select_category_text == "🍽️ 추천 받고자하는 음식 카테고리"

            dropdown_text = driver.find_element(By.CSS_SELECTOR, select_option.dropdown_css_selector + " span").text.strip()
            assert dropdown_text == "음식 카테고리를 설정해주세요"

            eating_people_text = driver.find_element(By.XPATH, self.eating_people_text_xpath).text.strip()
            assert eating_people_text == "🙌 먹는 인원"

            profile_image = driver.find_element(By.CSS_SELECTOR, self.profile_image_css_selector)
            profile_name = driver.find_element(By.CSS_SELECTOR, self.profile_name_css_selector)
            profile_team = driver.find_element(By.CSS_SELECTOR, self.profile_team_css_selector)
            assert profile_image.is_displayed()
            assert profile_name.is_displayed()
            assert profile_team.is_displayed()

            assert driver.find_element(By.XPATH, select_option.done_btn_xpath).get_attribute("disabled") is not None
            
            assert driver.find_element(By.CSS_SELECTOR, self.navigation_bar_css_selector).is_displayed()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_003(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_alone_btn_css_selector))
            )

            home.open_eat_alone()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.rounded-full.cursor-pointer'))
            )

            util.click_back()
            assert "https://kdt-pt-1-pj-2-team03.elicecoding.com/" == driver.current_url
            assert driver.find_element(By.CSS_SELECTOR, home.eat_alone_btn_css_selector).is_displayed()
            assert driver.find_element(By.CSS_SELECTOR, home.eat_together_btn_css_selector).is_displayed()
            assert driver.find_element(By.CSS_SELECTOR, home.eat_team_btn_css_selector).is_displayed()
            navigation_home_icon_color = driver.find_element(By.CSS_SELECTOR, self.navigation_home_icon_css_selector).value_of_css_property("color")
            navigation_home_text_color = driver.find_element(By.CSS_SELECTOR, self.navigation_home_text_css_selector).value_of_css_property("color")
            assert navigation_home_icon_color == "rgba(255, 77, 77, 1)"
            assert navigation_home_text_color == "rgba(255, 77, 77, 1)"

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
        

    def test_home_004(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_alone_btn_css_selector))
            )

            home.open_eat_alone()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            options = driver.find_elements(By.CSS_SELECTOR, select_option.options_css_selector)

            actual_options = [opt.text.strip() for opt in options]
            expected_options = ["한식", "중식", "양식", "일식", "분식", "아시안", "패스트푸드", "기타"]

            assert set(actual_options) == set(expected_options), f"드롭다운 옵션 불일치: {actual_options}"
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
        
    
    def test_home_005(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_alone_btn_css_selector))
            )

            home.open_eat_alone()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            
            selected_option_text = driver.find_element(By.CSS_SELECTOR, "span[style='pointer-events: none;']").text.strip()
            dropdown_text = driver.find_element(By.CSS_SELECTOR, select_option.dropdown_css_selector + " span").text.strip()
            
            assert selected_option_text == dropdown_text
            assert driver.find_element(By.XPATH, select_option.done_btn_xpath).is_enabled()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# 수정 필요
    def test_home_006(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_alone_btn_css_selector))
            )

            home.open_eat_alone()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            select_option.click_done_button()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.rounded-full.cursor-pointer'))
            )

            header_text = driver.find_element(By.CSS_SELECTOR, self.header_text_css_selector).text.strip()
            assert header_text == "메뉴 추천"
            
            # 오늘의 메뉴, 음식 사진, 서브 텍스트, 맛집 리스트 텍스트, 맛집 리스트 결과, 버튼 2개
            
            assert driver.find_element(By.CSS_SELECTOR, self.navigation_bar_css_selector).is_displayed()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    
    def test_home_007(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_alone_btn_css_selector))
            )

            home.open_eat_alone()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            select_option.click_done_button()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.rounded-full.cursor-pointer'))
            )

            util.click_back()
            assert "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone" == driver.current_url

            dropdown_text = driver.find_element(By.CSS_SELECTOR, select_option.dropdown_css_selector + " span").text.strip()
            assert dropdown_text == "음식 카테고리를 설정해주세요"

            assert driver.find_element(By.XPATH, select_option.done_btn_xpath).get_attribute("disabled") is not None

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


# tc 8,9,10 서버 고친 뒤 추가 필요


    def test_home_011(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_together_btn_css_selector))
            )

            home.open_eat_together()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.rounded-full.cursor-pointer'))
            )
            
            header_text = driver.find_element(By.CSS_SELECTOR, self.header_text_css_selector).text.strip()
            assert header_text == "추천 옵션 선택"
            
            select_category_text = driver.find_element(By.CSS_SELECTOR, self.select_category_text_css_selector).text.strip()
            assert select_category_text == "🍽️ 추천 받고자하는 음식 카테고리"

            dropdown_text = driver.find_element(By.CSS_SELECTOR, select_option.dropdown_css_selector + " span").text.strip()
            assert dropdown_text == "음식 카테고리를 설정해주세요"

            eating_people_text = driver.find_element(By.XPATH, self.eating_people_text_xpath).text.strip()
            assert eating_people_text == "🙌 먹는 인원"

            assert driver.find_element(By.CSS_SELECTOR, self.division_css_selector).is_displayed()

            assert driver.find_element(By.CSS_SELECTOR, self.search_field_css_selector).is_displayed()

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(By.CSS_SELECTOR, self.user_lists_css_selector)
            assert len(user_list) > 0

            random_user = random.choice(user_list)
            assert random_user.find_element(By.CSS_SELECTOR, self.profile_image_css_selector).is_displayed()
            assert random_user.find_element(By.CSS_SELECTOR, self.profile_name_css_selector).is_displayed()
            assert random_user.find_element(By.CSS_SELECTOR, self.profile_team_css_selector).is_displayed()
            assert random_user.find_element(By.CSS_SELECTOR, self.profile_checkbox_css_selector).is_displayed()

            assert driver.find_element(By.XPATH, select_option.done_btn_xpath).get_attribute("disabled") is not None
            
            assert driver.find_element(By.CSS_SELECTOR, self.navigation_bar_css_selector).is_displayed()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_012(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_together_btn_css_selector))
            )

            home.open_eat_together()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.rounded-full.cursor-pointer'))
            )

            util.click_back()
            assert "https://kdt-pt-1-pj-2-team03.elicecoding.com/" == driver.current_url
            assert driver.find_element(By.CSS_SELECTOR, home.eat_alone_btn_css_selector).is_displayed()
            assert driver.find_element(By.CSS_SELECTOR, home.eat_together_btn_css_selector).is_displayed()
            assert driver.find_element(By.CSS_SELECTOR, home.eat_team_btn_css_selector).is_displayed()
            navigation_home_icon_color = driver.find_element(By.CSS_SELECTOR, self.navigation_home_icon_css_selector).value_of_css_property("color")
            navigation_home_text_color = driver.find_element(By.CSS_SELECTOR, self.navigation_home_text_css_selector).value_of_css_property("color")
            assert navigation_home_icon_color == "rgba(255, 77, 77, 1)"
            assert navigation_home_text_color == "rgba(255, 77, 77, 1)"

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
        

    def test_home_013(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_together_btn_css_selector))
            )

            home.open_eat_together()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            options = driver.find_elements(By.CSS_SELECTOR, select_option.options_css_selector)

            actual_options = [opt.text.strip() for opt in options]
            expected_options = ["한식", "중식", "양식", "일식", "분식", "아시안", "패스트푸드", "기타"]

            assert set(actual_options) == set(expected_options), f"드롭다운 옵션 불일치: {actual_options}"
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
        
    
    def test_home_014(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_together_btn_css_selector))
            )

            home.open_eat_together()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            
            selected_option_text = driver.find_element(By.CSS_SELECTOR, "span[style='pointer-events: none;']").text.strip()
            dropdown_text = driver.find_element(By.CSS_SELECTOR, select_option.dropdown_css_selector + " span").text.strip()
            
            assert selected_option_text == dropdown_text
            assert driver.find_element(By.XPATH, select_option.done_btn_xpath).get_attribute("disabled") is not None
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_015(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_together_btn_css_selector))
            )

            home.open_eat_together()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(By.CSS_SELECTOR, self.user_lists_css_selector)
            random_user = random.choice(user_list)
            random_user = ws(driver, 10).until(
                EC.element_to_be_clickable(random_user)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", random_user)
            driver.execute_script("arguments[0].click();", random_user)
            
            assert driver.find_element(By.CSS_SELECTOR, self.profile_image_css_selector).is_displayed()
            assert driver.find_element(By.CSS_SELECTOR, self.profile_name_css_selector).is_displayed()
            assert driver.find_element(By.CSS_SELECTOR, self.profile_team_css_selector).is_displayed()
            assert driver.find_element(By.CSS_SELECTOR, self.profile_cancel_btn_css_selector).is_displayed()

            assert driver.find_element(By.XPATH, select_option.done_btn_xpath).is_enabled()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_016(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_together_btn_css_selector))
            )

            home.open_eat_together()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(By.CSS_SELECTOR, self.user_lists_css_selector)
            random_user_name = random.choice(user_list).find_element(By.CSS_SELECTOR, self.profile_name_css_selector).text.strip()
            
            driver.find_element(By.CSS_SELECTOR, self.search_field_css_selector).send_keys(random_user_name)
            assert driver.find_element(By.CSS_SELECTOR, self.searched_user_css_selector).is_displayed()
            assert driver.find_element(By.CSS_SELECTOR, self.searched_profile_image_css_selector).is_displayed()
            assert driver.find_element(By.CSS_SELECTOR, self.searched_profile_name_tag_name).text == random_user_name
            assert driver.find_element(By.CSS_SELECTOR, self.searched_profile_team_css_selector).is_displayed()
            
            util.click_element(By.CSS_SELECTOR, self.searched_user_css_selector + ":nth-of-type(1)")
            assert driver.find_element(By.CSS_SELECTOR, self.profile_image_css_selector).is_displayed()
            assert driver.find_element(By.CSS_SELECTOR, self.profile_name_css_selector).text == random_user_name
            assert driver.find_element(By.CSS_SELECTOR, self.profile_team_css_selector).is_displayed()
            assert driver.find_element(By.CSS_SELECTOR, self.profile_cancel_btn_css_selector).is_displayed()

            assert driver.find_element(By.CSS_SELECTOR, self.search_field_css_selector).get_attribute("value") == ""
            
            assert driver.find_element(By.XPATH, select_option.done_btn_xpath).is_enabled()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    # 수정 필요? 먹는 인원?
    def test_home_017(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_together_btn_css_selector))
            )

            home.open_eat_together()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(By.CSS_SELECTOR, self.user_lists_css_selector)
            random_user = random.choice(user_list)
            random_user = ws(driver, 10).until(
                EC.element_to_be_clickable(random_user)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", random_user)
            driver.execute_script("arguments[0].click();", random_user)
            
            driver.execute_script("window.scrollTo(0, 0);")
            util.click_element(By.CSS_SELECTOR, self.profile_cancel_btn_css_selector)

            assert driver.find_element(By.XPATH, select_option.done_btn_xpath).get_attribute("disabled") is not None
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    
    # 수정 필요
    def test_home_018(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_together_btn_css_selector))
            )

            home.open_eat_together()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(By.CSS_SELECTOR, self.user_lists_css_selector)
            random_user = random.choice(user_list)
            random_user = ws(driver, 10).until(
                EC.element_to_be_clickable(random_user)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", random_user)
            driver.execute_script("arguments[0].click();", random_user)

            select_option.click_done_button()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.rounded-full.cursor-pointer'))
            )

            header_text = driver.find_element(By.CSS_SELECTOR, self.header_text_css_selector).text.strip()
            assert header_text == "메뉴 추천"
            
            # 오늘의 메뉴, 음식 사진, 서브 텍스트, 맛집 리스트 텍스트, 맛집 리스트 결과, 버튼 2개
            
            assert driver.find_element(By.CSS_SELECTOR, self.navigation_bar_css_selector).is_displayed()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    
    # 수정 필요? 먹는 인원?
    def test_home_019(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_together_btn_css_selector))
            )

            home.open_eat_together()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            user_list = driver.find_elements(By.CSS_SELECTOR, self.user_lists_css_selector)
            random_user = random.choice(user_list)
            random_user = ws(driver, 10).until(
                EC.element_to_be_clickable(random_user)
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", random_user)
            driver.execute_script("arguments[0].click();", random_user)

            select_option.click_done_button()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.rounded-full.cursor-pointer'))
            )

            util.click_back()
            assert "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/together" == driver.current_url

            dropdown_text = driver.find_element(By.CSS_SELECTOR, select_option.dropdown_css_selector + " span").text.strip()
            assert dropdown_text == "음식 카테고리를 설정해주세요"

            assert driver.find_element(By.XPATH, select_option.done_btn_xpath).get_attribute("disabled") is not None

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


# tc 20,21,22 서버 고친 뒤 추가 필요


    def test_home_023(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_team_btn_css_selector))
            )

            home.open_eat_team()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.rounded-full.cursor-pointer'))
            )
            
            header_text = driver.find_element(By.CSS_SELECTOR, self.header_text_css_selector).text.strip()
            assert header_text == "추천 옵션 선택"
            
            select_category_text = driver.find_element(By.CSS_SELECTOR, self.select_category_text_css_selector).text.strip()
            assert select_category_text == "🍽️ 추천 받고자하는 음식 카테고리"

            dropdown_text = driver.find_element(By.CSS_SELECTOR, select_option.dropdown_css_selector + " span").text.strip()
            assert dropdown_text == "음식 카테고리를 설정해주세요"

            eating_people_text = driver.find_element(By.XPATH, self.eating_people_text_xpath).text.strip()
            assert eating_people_text == "🙌 먹는 인원"

            assert driver.find_element(By.CSS_SELECTOR, self.team_css_selector).is_displayed()

            assert driver.find_element(By.XPATH, select_option.done_btn_xpath).get_attribute("disabled") is not None
            
            assert driver.find_element(By.CSS_SELECTOR, self.navigation_bar_css_selector).is_displayed()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


    def test_home_024(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_team_btn_css_selector))
            )

            home.open_eat_team()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.rounded-full.cursor-pointer'))
            )

            util.click_back()
            assert "https://kdt-pt-1-pj-2-team03.elicecoding.com/" == driver.current_url
            assert driver.find_element(By.CSS_SELECTOR, home.eat_alone_btn_css_selector).is_displayed()
            assert driver.find_element(By.CSS_SELECTOR, home.eat_together_btn_css_selector).is_displayed()
            assert driver.find_element(By.CSS_SELECTOR, home.eat_team_btn_css_selector).is_displayed()
            navigation_home_icon_color = driver.find_element(By.CSS_SELECTOR, self.navigation_home_icon_css_selector).value_of_css_property("color")
            navigation_home_text_color = driver.find_element(By.CSS_SELECTOR, self.navigation_home_text_css_selector).value_of_css_property("color")
            assert navigation_home_icon_color == "rgba(255, 77, 77, 1)"
            assert navigation_home_text_color == "rgba(255, 77, 77, 1)"

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
        

    def test_home_025(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_team_btn_css_selector))
            )

            home.open_eat_team()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            options = driver.find_elements(By.CSS_SELECTOR, select_option.options_css_selector)

            actual_options = [opt.text.strip() for opt in options]
            expected_options = ["한식", "중식", "양식", "일식", "분식", "아시안", "패스트푸드", "기타"]

            assert set(actual_options) == set(expected_options), f"드롭다운 옵션 불일치: {actual_options}"
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise
        
    
    def test_home_026(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_team_btn_css_selector))
            )

            home.open_eat_team()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            
            selected_option_text = driver.find_element(By.CSS_SELECTOR, "span[style='pointer-events: none;']").text.strip()
            dropdown_text = driver.find_element(By.CSS_SELECTOR, select_option.dropdown_css_selector + " span").text.strip()
            
            assert selected_option_text == dropdown_text
            assert driver.find_element(By.XPATH, select_option.done_btn_xpath).is_enabled()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

# 수정 필요
    def test_home_027(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_team_btn_css_selector))
            )

            home.open_eat_team()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            select_option.click_done_button()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.rounded-full.cursor-pointer'))
            )

            header_text = driver.find_element(By.CSS_SELECTOR, self.header_text_css_selector).text.strip()
            assert header_text == "메뉴 추천"
            
            # 오늘의 메뉴, 음식 사진, 서브 텍스트, 맛집 리스트 텍스트, 맛집 리스트 결과, 버튼 2개
            
            assert driver.find_element(By.CSS_SELECTOR, self.navigation_bar_css_selector).is_displayed()
            
            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

    
    def test_home_028(self, driver: WebDriver):
        try:
            util = WebUtils(driver)
            home = HomePage(driver)
            select_option = SelectOptionPage(driver)

            util.open_url()
            util.login()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, home.eat_team_btn_css_selector))
            )

            home.open_eat_team()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, select_option.dropdown_css_selector))
            )

            select_option.click_category_dropdown()
            select_option.click_category_dropdown_option_randomly()
            select_option.click_done_button()
            ws(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.rounded-full.cursor-pointer'))
            )

            util.click_back()
            assert "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team" == driver.current_url

            dropdown_text = driver.find_element(By.CSS_SELECTOR, select_option.dropdown_css_selector + " span").text.strip()
            assert dropdown_text == "음식 카테고리를 설정해주세요"

            assert driver.find_element(By.XPATH, select_option.done_btn_xpath).get_attribute("disabled") is not None

            LogUtils.log_success()

        except Exception as e:
            LogUtils.log_error(e, driver)
            raise


# tc 29,30,31 서버 고친 뒤 추가 필요