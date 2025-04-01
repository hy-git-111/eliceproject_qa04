import random
import pytest
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.helpers import WebUtils
from tests.conftest import driver
from src.pages.my_page import MyPage



class TestMyPage:
    # @pytest.mark.skip
    # 개인 피드 페이지 UI 확인
    def test_my_page_001(self, driver):
        mypage_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/my"

        web_utils = WebUtils(driver)
        web_utils.open_url()
        web_utils.login("qa04@ruu.kr", "1234Qwer!")

        web_utils.click_tab_personal()

        current_url = driver.current_url
        assert current_url == mypage_url, f"URL 불일치"
        time.sleep(3)

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
        assert statistics_canvas.is_displayed(), "내 통계 그래프 미노출"

        # 내가 먹은 메뉴
        my_food_review_title = driver.find_element(By.CSS_SELECTOR, "font-bold text-sub-2 text-title").text
        assert my_food_review_title == "🍽️ 내가 먹은 메뉴", "내가 먹은 메뉴 텍스트 미노출"

        my_food_review_add_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[2]/div[1]/button')
        assert my_food_review_add_btn.is_displayed(), "내가 먹은 메뉴 추가 버튼 미노출"

        # 후기 있는 경우 진행 코드 따기(파일명 코드는 프로필)
        my_food_review_img = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[2]/div[2]/div[1]/div[1]/img')
        assert my_food_review_img.is_displayed(), "후기 이미지 미노출"

        # UI 확인 > 하단 스크롤 > 목록 전체 불러오기
        # 목록 추가, 내용 리스트 받아오는 코드

    # @pytest.mark.skip
    # 내 프로필 수정하기 페이지 UI 확인
    def test_my_page_002(self, driver):
        web_utils = WebUtils(driver)
        web_utils.open_url()
        web_utils.login("qa04@ruu.kr", "1234Qwer!")
        web_utils.click_tab_personal()
        time.sleep(1)

        my_page = MyPage(driver)
        my_page.profile_setup()
        time.sleep(1)

        my_profile_modify_header = driver.find_element(By.XPATH, '//span[@class="text-main-black font-semibold" and text()="프로필 정보 수정"]').text
        assert my_profile_modify_header == "프로필 정보 수정", "프로필 정보 수정 헤더 미노출"

        my_profile_modify_close = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[1]/button')
        assert my_profile_modify_close.is_displayed(), "프로필 정보 수정 닫기 버튼 미노출"

        my_profile_img_title = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[1]/span').text
        assert my_profile_img_title == "프로필 이미지 수정", "프로필 이미지 수정 텍스트 미노출"

        profile_modify_img = driver.find_element(By.CSS_SELECTOR, 'img[alt="프로필 이미지"')
        profile_image_src = profile_modify_img.get_attribute("src")
        image_filename = os.path.basename(profile_image_src)
        assert profile_modify_img is not None, "프로필 수정 페이지 이미지가 로드되지 않음"
        assert image_filename, "프로필 수정 페이지 이미지가 존재하지 않음"
        print(f"프로필 이미지 파일명: {image_filename}")

        profile_img_change_btn = driver.find_element(By.CSS_SELECTOR, ".w-12.h-12.text-white.bg-main-black")
        assert profile_img_change_btn.is_displayed(), "프로필 이미지 수정 버튼 미노출"

        profile_modify_sweat_text = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/section[1]/span').text
        assert profile_modify_sweat_text == "단 맛", "프로필 수정 단 맛 텍스트 미노출"

        profile_modify_sweat_slider = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/section[1]/div/span[1]')
        assert profile_modify_sweat_slider.is_displayed(), "프로필 수정 단 맛 슬리이드 미노출"

        profile_modify_salty_text = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/section[2]/span').text
        assert profile_modify_salty_text == "짠 맛", "프로필 수정 짠 맛 텍스트 미노출"

        profile_modify_salty_slider = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/section[2]/div/span[1]')
        assert profile_modify_salty_slider.is_displayed(), "프로필 수정 짠 맛 슬라이더 미노출"

        profile_modify_spicy_text = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/section[3]/span').text
        assert profile_modify_spicy_text == "매운 맛", "프로필 수정 매운 맛 텍스트 미노출"

        profile_modify_spicy_slider = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/section[3]/div/span[1]')
        assert profile_modify_spicy_slider.is_displayed(), "프로필 수정 매운 맛 슬라이더 미노출"

        profile_modify_favorite_text = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[3]/span').text
        assert profile_modify_favorite_text == "😃 이런 음식은 좋아요!", "프로필 수정 - 이런 음식은 좋아요! 미노출"

        profile_modify_favorite_input = driver.find_element(By.CSS_SELECTOR, 'textarea[name="pros"]')
        assert profile_modify_favorite_input.is_displayed(), "좋아하는 음식 입력란 미노출"

        profile_modify_least_favorite_text = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/span').text
        assert profile_modify_least_favorite_text == "☹️ 이런 음식은 싫어요!", "프로필 수정 - 이런 음식은 싫어요! 미노출"

        profile_modify_least_favorite_input = driver.find_element(By.CSS_SELECTOR, 'textarea[name="cons"]')
        assert profile_modify_least_favorite_input.is_displayed(), "싫어하는 음식 입력란 미노출"

        profile_modify_completed_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        assert profile_modify_completed_btn.is_displayed(), "프로필 수정 완료 버튼 미노출"


    # @pytest.mark.skip
    # 새로운 후기 등록하기 페이지 UI 확인
    def test_my_page_003(self, driver):
        web_utils = WebUtils(driver)
        web_utils.open_url()
        web_utils.login("qa04@ruu.kr", "1234Qwer!")
        web_utils.click_tab_personal()

        my_page = MyPage(driver)
        my_page.my_food_review()
        time.sleep(1)

        my_food_review_title = driver.find_element(By.XPATH, '//span[@class="text-main-black font-semibold" and text()="새로운 후기 등록하기"]').text
        assert my_food_review_title == "새로운 후기 등록하기", "새로운 후기 등록하기 타이틀 미노출"

        # my_food_review_close_btn = driver.find_element(By.CSS_SELECTOR, "text-2xl.cursor-pointer")
        # assert my_food_review_close_btn.is_displayed(), "닫기 버튼 미노출"

        review_type_text = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[1]/h1').text
        assert review_type_text == "식사 유형", "식사 유형 텍스트 미노출"

        ate_alone_btn = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[1]/div/div[1]')
        assert ate_alone_btn.is_displayed(), "혼밥 버튼 미노출"

        ate_group_btn = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[1]/div/div[2]')
        assert ate_group_btn.is_displayed(), "그룹 버튼 미노출"

        ate_party_btn = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[1]/div/div[3]')
        assert ate_party_btn.is_displayed(), "회식 버튼 미노출"

        review_img_text = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/h1').text
        assert review_img_text == "후기 사진", "후기 사진 텍스트 미노출"

        review_img = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/div')
        assert review_img.is_displayed(), "후기 사진 영역 미노출"

        review_img_btn = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/button')
        assert review_img_btn.is_displayed(), "후기 사진 등록 버튼 미노출"

        food_name_title = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[3]/h1').text
        assert food_name_title == "메뉴 명", "메뉴 명 텍스트 미노출"

        food_name_input = driver.find_element(By.CSS_SELECTOR, '[name="menu"]')
        assert food_name_input.is_displayed(), "메뉴명 입력랑 미노출"

        food_category = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/h1').text
        assert food_category == "카테고리", "카테고리 텍스트 미노출"

        food_category_dropdown = driver.find_element(By.CSS_SELECTOR, '[role="combobox"]')
        assert food_category_dropdown.is_displayed(), "키테고리 드롭다운 미노출"

        review_detail_title = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[5]/h1').text
        assert review_detail_title == "후기", "후기 텍스트 미노출"

        review_detail_input = driver.find_element(By.CSS_SELECTOR, '[name="comment"]')
        assert review_detail_input.is_displayed(), "후기 입력란 미노출"

        review_star_title = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[6]/h1').text
        assert review_star_title == "별점", "별점 텍스트 미노출"

        review_star_btn = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[6]/div')
        assert review_star_btn.is_displayed(), "별점 버튼 미노출"

        review_write_completed = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/button')
        assert review_write_completed.is_displayed(), "후기 작성 완료 버튼 미노출"


    # @pytest.mark.skip
    # 프로필 수정 기능 테스트
    def test_my_page_004(self, driver):
        # 입력 텍스트값 정의
        favorite_text = "좋아하는 음식 작성 텍스트 비교용 1"
        least_favorite_text = "싫어하는 음식 작성 텍스트 비교용"

        # 페이지 호출 및 로그인
        web_utils = WebUtils(driver)
        web_utils.open_url()
        web_utils.login("qa04@ruu.kr", "1234Qwer!")

        # 개인 피드 페이지 진입
        web_utils.click_tab_personal()

        my_page = MyPage(driver)

        # 프로필 수정 버튼 클릭
        my_page.profile_setup()
        time.sleep(1)

        # 이미지 업로드
        web_utils.review_image_upload()

        # 슬라이더 조작


        # 음식 선호 입력 필드 작성
        my_page.favorite_food_input(favorite_text)
        my_page.least_favorite_food_input(least_favorite_text)

        # 프로필 수정 완료 버튼 클릭
        my_page.profile_setup_completed()
        time.sleep(1)

        # 입력값 결과 비교


    # @pytest.mark.skip(reason = "pass but not yet info check")
    # 혼밥 후기 작성
    def test_my_page_005(self, driver):
        # 로그인 진행
        web_utils = WebUtils(driver)
        web_utils.open_url()
        web_utils.login("qa04@ruu.kr", "1234Qwer!")
        # 개인 피드 지입
        web_utils.click_tab_personal()

        # 후기 추가하기 버튼 클릭 및 후기 작성 페이지 진입
        my_page = MyPage(driver)
        my_page.scroll_to_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[2]/div[1]/button')
        time.sleep(1)

        # 메뉴명 입력
        my_page.menu_name_input("메뉴명을 입력해보자")

        # 이미지 업로드
        web_utils.review_image_upload()
        time.sleep(1)

        # 카테고리 랜덤 선택
        web_utils.review_category()
        my_page.food_combobox_random()
        time.sleep(1)

        # 카테고리 값 변경 확인용 임시 코드
        selected_value = driver.find_element(By.CSS_SELECTOR, "button[role='combobox'] span").text
        print("현재 선택된 값:", selected_value)

        time.sleep(3)
        my_page.review_input("후기 작성")

        my_page.review_star_random()
        print("별점 클릭 완료")
        web_utils.review_completed()
        print("후기 작성 완료 버튼 클릭 완료")
        time.sleep(2)

        # 메뉴 정보 확인
        # menu_info = my_page.get_menu_info()
        # expected_data = {
        #     "image_src": "Users/kimdongyeon/Desktop/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-03-21%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.44.18.pngp",
        #     "tags": ["혼밥", "한식"],
        #     "title": "메뉴명 입력",
        #     "rating": "★☆☆☆☆",
        #     "review": "후기를 입력해보자",
        # }
        #
        # assert menu_info == expected_data, f"Expected {expected_data}, but got {menu_info}"

    # @pytest.mark.skip(reason = "pass, but not yet info check")
    # 그룹 후기 추가 케이스
    def test_my_page_006(self, driver):
        # 로그인 진행
        web_utils = WebUtils(driver)
        web_utils.open_url()
        web_utils.login("qa04@ruu.kr", "1234Qwer!")
        # 개인 피드 지입
        web_utils.click_tab_personal()

        # 후기 추가하기 버튼 클릭 및 후기 작성 페이지 진입
        my_page = MyPage(driver)
        my_page.scroll_to_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[2]/div[1]/button')
        time.sleep(1)

        # 그룹 버튼 클릭
        web_utils.ate_group()

        # 같이 먹은 사람 작성 목록 확인
        group_name_title = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[3]/h1').text
        assert group_name_title == "같이 먹은 사람 등록", "같이 먹은 사람 등록 미노출"
        group_name_input = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[3]/div[1]/input')
        assert group_name_input.is_displayed(), "같이 먹은 사람 입력란 미노출"
        group_name_input.send_keys("누구인가")

        # 메뉴명 입력
        my_page.menu_name_input("메뉴명을 입력해보자")

        # 이미지 업로드
        web_utils.review_image_upload()
        time.sleep(1)

        # 카테고리 랜덤 선택
        web_utils.review_category()
        my_page.food_combobox_random()
        time.sleep(1)

        # 카테고리 값 변경 확인용 임시 코드
        selected_value = driver.find_element(By.CSS_SELECTOR, "button[role='combobox'] span").text
        print("현재 선택된 값:", selected_value)

        time.sleep(3)
        my_page.review_input("후기 작성")

        my_page.review_star_random()
        print("별점 클릭 완료")
        web_utils.review_completed()
        print("후기 작성 완료 버튼 클릭 완료")
        time.sleep(2)

        # 최근 등록 후기 정보 비교
        # review_info = my_page.get_menu_info()
        # expected_data = {
        #     "image_src": "Users/kimdongyeon/Desktop/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-03-21%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.44.18.pngp",
        #     "tags": ["혼밥", "한식"],
        #     "title": "메뉴명 입력",
        #     "rating": "★☆☆☆☆",
        #     "review": "후기를 입력해보자",
        # }
        #
        # assert menu_info == expected_data, f"Expected {expected_data}, but got {menu_info}"

    # @pytest.mark.skip(reason = "same")
    # 회식 후기 작성
    def test_my_page_007(self, driver):
        # 로그인 진행
        web_utils = WebUtils(driver)
        web_utils.open_url()
        web_utils.login("qa04@ruu.kr", "1234Qwer!")
        # 개인 피드 지입
        web_utils.click_tab_personal()

        # 후기 추가하기 버튼 클릭 및 후기 작성 페이지 진입
        my_page = MyPage(driver)
        my_page.scroll_to_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[2]/div[1]/button')
        time.sleep(1)

        # 회식 버튼 클릭
        web_utils.ate_party()

        # 메뉴명 입력
        my_page.menu_name_input("메뉴명을 입력해보자")

        # 이미지 업로드
        web_utils.review_image_upload()
        time.sleep(1)

        # 카테고리 랜덤 선택
        web_utils.review_category()
        my_page.food_combobox_random()
        time.sleep(1)

        # 카테고리 값 변경 확인용 임시 코드
        selected_value = driver.find_element(By.CSS_SELECTOR, "button[role='combobox'] span").text
        print("현재 선택된 값:", selected_value)

        time.sleep(3)
        my_page.review_input("후기 작성")

        my_page.review_star_random()
        print("별점 클릭 완료")
        web_utils.review_completed()
        print("후기 작성 완료 버튼 클릭 완료")
        time.sleep(2)

        # 메뉴 정보 확인
        # menu_info = my_page.get_menu_info()
        # expected_data = {
        #     "image_src": "Users/kimdongyeon/Desktop/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-03-21%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.44.18.pngp",
        #     "tags": ["혼밥", "한식"],
        #     "title": "메뉴명 입력",
        #     "rating": "★☆☆☆☆",
        #     "review": "후기를 입력해보자",
        # }
        #
        # assert menu_info == expected_data, f"Expected {expected_data}, but got {menu_info}"


    # @pytest.mark.skip
    # 또 먹은 후기 혼밥으로 등록하기
    def test_my_page_008(self, driver):
        # 로그인 진행
        web_utils = WebUtils(driver)
        web_utils.open_url()
        web_utils.login("qa04@ruu.kr", "1234Qwer!")
        # 개인 피드 지입
        web_utils.click_tab_personal()

        # 같은 메뉴 먹기 버튼 클릭 및 후기 작성 페이지 진입
        my_page = MyPage(driver)
        my_page.scroll_to_element(By.XPATH, "//button[text()='같은 메뉴 먹기']")
        time.sleep(1)

        # 이미지 업로드
        web_utils.review_image_upload()
        time.sleep(1)

        my_page.review_input("또먹 후기 작성")

        my_page.review_star_random()
        print("별점 클릭 완료")
        web_utils.review_completed()
        print("후기 작성 완료 버튼 클릭 완료")
        time.sleep(2)

        # 메뉴 정보 확인
        # menu_info = my_page.get_menu_info()
        # expected_data = {
        #     "image_src": "Users/kimdongyeon/Desktop/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-03-21%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.44.18.pngp",
        #     "tags": ["혼밥", "한식"],
        #     "title": "메뉴명 입력",
        #     "rating": "★☆☆☆☆",
        #     "review": "후기를 입력해보자",
        # }
        #
        # assert menu_info == expected_data, f"Expected {expected_data}, but got {menu_info}"

    # @pytest.mark.skip
    # 또 먹은 메뉴 후기 그룹 등록
    def test_my_page_009(self, driver):
        # 로그인 진행
        web_utils = WebUtils(driver)
        web_utils.open_url()
        web_utils.login("qa04@ruu.kr", "1234Qwer!")
        # 개인 피드 지입
        web_utils.click_tab_personal()

        # 같은 메뉴 먹기 버튼 클릭 및 후기 작성 페이지 진입
        my_page = MyPage(driver)
        my_page.scroll_to_element(By.XPATH, "//button[text()='같은 메뉴 먹기']")
        time.sleep(1)

        # 그룹 버튼 클릭
        web_utils.ate_group()
        time.sleep(1)

        # 같이 먹은 사람 작성 목록 확인
        group_name_title = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[3]/h1').text
        assert group_name_title == "같이 먹은 사람 등록", "같이 먹은 사람 등록 미노출"
        group_name_input = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[3]/div[1]/input')
        assert group_name_input.is_displayed(), "같이 먹은 사람 입력란 미노출"
        group_name_input.send_keys("누구인가")

        # 이미지 업로드
        web_utils.review_image_upload()
        time.sleep(1)

        my_page.review_input("또먹 후기 작성")

        my_page.review_star_random()
        print("별점 클릭 완료")
        web_utils.review_completed()
        print("후기 작성 완료 버튼 클릭 완료")
        time.sleep(2)

        # 메뉴 정보 확인
        # menu_info = my_page.get_menu_info()
        # expected_data = {
        #     "image_src": "Users/kimdongyeon/Desktop/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-03-21%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.44.18.pngp",
        #     "tags": ["혼밥", "한식"],
        #     "title": "메뉴명 입력",
        #     "rating": "★☆☆☆☆",
        #     "review": "후기를 입력해보자",
        # }
        #
        # assert menu_info == expected_data, f"Expected {expected_data}, but got {menu_info}"

    # @pytest.mark.skip
    # 또 먹은 메뉴 후기 회식 등록
    def test_my_page_010(self, driver):
        # 로그인 진행
        web_utils = WebUtils(driver)
        web_utils.open_url()
        web_utils.login("qa04@ruu.kr", "1234Qwer!")
        # 개인 피드 지입
        web_utils.click_tab_personal()

        # 같은 메뉴 먹기 버튼 클릭 및 후기 작성 페이지 진입
        my_page = MyPage(driver)
        my_page.scroll_to_element(By.XPATH, "//button[text()='같은 메뉴 먹기']")
        time.sleep(1)

        # 회식 버튼 클릭
        web_utils.ate_party()

        # 이미지 업로드
        web_utils.review_image_upload()
        time.sleep(1)

        my_page.review_input("또먹 후기 작성")

        my_page.review_star_random()
        print("별점 클릭 완료")
        web_utils.review_completed()
        print("후기 작성 완료 버튼 클릭 완료")
        time.sleep(2)

        # 메뉴 정보 확인
        # menu_info = my_page.get_menu_info()
        # expected_data = {
        #     "image_src": "Users/kimdongyeon/Desktop/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-03-21%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.44.18.pngp",
        #     "tags": ["혼밥", "한식"],
        #     "title": "메뉴명 입력",
        #     "rating": "★☆☆☆☆",
        #     "review": "후기를 입력해보자",
        # }
        #
        # assert menu_info == expected_data, f"Expected {expected_data}, but got {menu_info}"
