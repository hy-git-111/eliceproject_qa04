import random
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.conftest import driver



class MyPage():
    def __init__(self, driver:WebDriver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    # 개인 피드 버튼 클릭
    def open_mypage(self):
        mypage_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[4]/a')
        mypage_btn.click()

    def profile_setup(self):
        parent_div = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.flex.items-center.justify-between.text-subbody")))
        child_elements = parent_div.find_elements(By.XPATH, "./*")  # 부모 기준 모든 직계 자식
        child_svg = child_elements[1]
        child_svg.click()

    # 프로필 정보 수정 - 이미지 첨부 버튼 클릭
    def image_attach(self):
        image_attach_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[1]/div/button')
        image_attach_btn.click()

    # 음식 성향 - 단 맛 슬라이더 변경
    def profile_sweet_slider(self):
        sweet_slider = self.driver.find_elements(By.CSS_SELECTOR, 'span[data-orientation="horizontal"].relative.h-2.w-full')


    # 좋아하는 음식 입력 필드 작성
    def favorite_food_input(self, favorite_text):
        favorite_input = self.driver.find_element(By.CSS_SELECTOR, 'textarea[name="pros"]')
        favorite_input.send_keys(favorite_text)

    # 싫어하는 음식 입력 필드 작성
    def least_favorite_food_input(self, least_favorite_text):
        least_favorite_input = self.driver.find_element(By.CSS_SELECTOR, 'textarea[name="cons"]')
        least_favorite_input.send_keys(least_favorite_text)

    # 프로필 수정 완료 버튼 클릭
    def profile_setup_completed(self):
        profile_setup_completed_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/button')
        profile_setup_completed_btn.click()

    # 내가 먹은 메뉴 추가하기 버튼 클릭
    def my_food_review(self):
        my_food_add_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[2]/div[1]/button'))
        )
        my_food_add_btn.click()

    # 요소를 중앙에 위치하게 스크롤
    def scroll_to_element(self, by, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, value))).click()

    # 메뉴명 입력
    def menu_name_input(self, text):
        review_food_name = self.driver.find_element(By.XPATH, '//input[@placeholder="메뉴 명을 입력해주세요."]')
        review_food_name.send_keys(text)

    # 음식 카테고리 랜덤 선택
    def food_combobox_random(self):  # index : 선택할 팀 특정
        food_lists = self.driver.find_elements(By.CSS_SELECTOR, "[role='option']")
        foods = len(food_lists)
        food_index = random.randint(0, foods-1)
        food_lists[food_index].click()

    # 후기 텍스트 입력
    def review_input(self, text):
        review_food_detail = self.driver.find_element(By.XPATH, '//textarea[@placeholder="후기를 등록 입력해주세요."]')
        review_food_detail.send_keys(text)

    # 별점 랜덤 클릭
    def review_star_random(self):
        review_stars = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.w-10.h-10.cursor-pointer.text-gray-300'))
        )
        selected_star = random.choice(review_stars)
        selected_star.click()

        selected_star_index = review_stars.index(selected_star) + 1
        return selected_star_index

    # 같은 메뉴 먹기 버튼 클릭
    def same_food_review(self):
        same_food_review_btn = self.driver.find_element(By.XPATH, "//button[text()='같은 메뉴 먹기']")
        same_food_review_btn.click()

    def recent_review_info(self):
        recent_review = self.driver.find_element(By.CSS_SELECTOR, ".flex.w-full.gap-6.p-4.shadow-md.rounded-2xl")

        # 이미지 파일명 가져오기
        img_element = recent_review.find_element(By.CSS_SELECTOR, "img")
        img_src = img_element.get_attribute("src")
        img_filename = img_src.split("/")[-1]  # URL에서 파일명 추출

        # 태그명 가져오기 (최대 3개)
        tag_elements = recent_review.find_elements(By.CSS_SELECTOR, ".flex.gap-2 .inline-flex")[:3]
        tags = [tag.text for tag in tag_elements]

        # 메뉴명 가져오기
        menu_name = recent_review.find_element(By.CSS_SELECTOR, ".font-bold").text

        # 별점 가져오기 (★의 개수 카운트)
        star_elements = recent_review.find_elements(By.XPATH, ".//div[contains(@class, 'flex') and contains(@class, 'gap-0.5')]/span")
        rating = sum(1 for star in star_elements if "★" in star.text)

        # 후기 내용 가져오기
        review_text = recent_review.find_element(By.CSS_SELECTOR, ".relative p").text

        return {
            "image_filename": img_filename,
            "tags": tags,
            "menu_name": menu_name,
            "star_rating": rating,
            "review_text": review_text
        }

