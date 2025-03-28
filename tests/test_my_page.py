import pytest
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.my_page import MyPage
from src.utils.helpers import WebUtils


class TestMyPage:
    # 웹 오픈 후 개인 피드 페이지 이동
    @pytest.mark.order(1)
    def test_my_page_001(self, driver):
        mypage_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/my"

        web_utils = WebUtils(driver)
        web_utils.open_url()
        web_utils.login()

        web_utils.click_tab_personal()

        current_url = driver.current_url
        assert current_url == mypage_url, f"URL 불일치"
        time.sleep(3)

        # UI 확인
        # 헤더 텍스트
        header_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//header//span'))
        )
        header_text = header_element.text

        assert header_text == "내 피드", f"헤더 텍스트 불일치"

        # 이미지 노출 여부 + 파일명
        profile_img = driver.find_element(By.CSS_SELECTOR, 'img[alt="프로필 이미지"')
        profile_image_src = profile_img.get_attribute("src")
        image_filename = os.path.basename(profile_image_src)
        assert profile_img is not None, "이미지가 로드되지 않음"
        assert image_filename, "이미지가 존재하지 않음"
        print(f"프로필 이미지 파일명: {image_filename}")

        # 프로필 - 계정 정의 필요
        team_name = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[1]/div[2]/div/div/span').text
        assert team_name == "디자인 1팀"

        user_name = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[1]/div[2]/span').text
        assert user_name == "4조_test"

        food_orientation = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[2]/span').text
        assert food_orientation == "🍽️ 음식 성향", "음식 성향 타이틀 미노출"

        # 슬라이더 보류
        sweat_taste_text = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[2]/section[1]/span').text
        assert sweat_taste_text == "단 맛", "단 맛 텍스트 미노출"

        salty_taste_text = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[2]/section[2]/span').text
        assert salty_taste_text == "짠 맛", "짠 맛 텍스트 미노출"

        spicy_taste_text = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[2]/section[3]/span').text
        assert  spicy_taste_text == "매운 맛", "매운 맛 텍스트 미노출"

        favorite_food_text = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[2]/div[1]/p').text
        assert favorite_food_text == "이런것들은 좋아합니다.", "좋아하는 음식 텍스트 다름"

        least_favorite_food_text = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[2]/div[2]/p').text
        assert least_favorite_food_text == "이런것들은 싫어해요", "싫어하는 음식 텍스트 다름"

        # 내 통계
        statistics_text = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[1]/span').text
        assert statistics_text == "📊 내 통계", "내 통계 텍스트 미노출"

        statistics_canvas = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[1]/div/div/canvas')
        assert statistics_canvas is not None, "내 통계 그래프 미노출"

        # 내가 먹은 메뉴
        my_food_review_title = driver.find_element(By.CSS_SELECTOR, "font-bold text-sub-2 text-title").text
        assert my_food_review_title == "🍽️ 내가 먹은 메뉴", "내가 먹은 메뉴 텍스트 미노출"

        my_food_review_add_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[2]/div[1]/button')
        assert my_food_review_add_btn is not None, "내가 먹은 메뉴 추가 버튼 미노출"

        # 후기 있는 경우 진행 코드 따기(파일명 코드는 프로필)
        my_food_review_img = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[2]/div[2]/div[1]/div[1]/img')
        assert my_food_review_img is not None, "후기 이미지 미노출"

        # UI 확인 > 하단 스크롤 > 목록 전체 불러오기
        # 목록 추가, 내용 리스트 받아오는 코드

    @pytest.mark.order(2)
    def test_my_page_002(self, driver):
        web_utils = WebUtils(driver)
        web_utils.open_url()
        web_utils.login()
        web_utils.click_tab_personal()
        time.sleep(1)

        MyPage.profile_setup()
        time.sleep(1)

        my_profile_modify_header = driver.find_element(By.CSS_SELECTOR, "text-main-black font-semibold").text
        assert my_profile_modify_header == "프로필 정보 수정", "프로필 정보 수정 헤더 미노출"

        my_profile_modify_close = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[1]/button')
        assert my_profile_modify_close is not None, "프로필 정보 수정 닫기 버튼 미노출"

        my_profile_img_title = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[1]/span').text
        assert my_profile_img_title == "프로필 이미지 수정", "프로필 이미지 수정 텍스트 미노출"