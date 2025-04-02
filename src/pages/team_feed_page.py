# 팀 피드 페이지 기능
import time
from src.utils.helpers import WebUtils
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

class TeamFeed:
    def __init__(self, driver:WebDriver): # driver : ChromeDriver
        self.driver = driver

    # 팀 콤보박스 열기
    def open_team_combobox(self):
        team_combobox = self.driver.find_element(By.CSS_SELECTOR, "[role='combobox']")
        team_combobox.click()

    # 팀 콤보박스 내 항목 선택
    def select_team_combobox(self, index):  # index : 선택할 팀 특정
        teams = self.driver.find_elements(By.CSS_SELECTOR, "[role='option']")
        teams[index].click()
        
    # 내 팀 음식 성향 편집 아이콘 클릭
    def click_modify_team_profile_icon(self):
        team_modify_icon = self.driver.find_elements(By.CLASS_NAME, "cursor-pointer")[1]
        team_modify_icon.click()

    # 프로필 정보 수정 > 프로필 수정 완료 버튼 클릭
    def click_team_profile_modify_done(self):
        team_modify_done_btn = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")
        team_modify_done_btn.click()
    
    # 음식 성향 - 단 맛 슬라이더 변경
    def modify_team_sweet(self):
       modal_tendency_area = self.driver.find_element(By.ID, "modal-root").find_element(By.CLASS_NAME, "space-y-6")
       container = modal_tendency_area.find_element(By.CSS_SELECTOR, "div.flex.items-center")
       slider = container.find_element(By.CSS_SELECTOR, 'span[role="slider"]')

       input_elem = slider.find_element(By.XPATH, './following-sibling::input')
       value = 2.1

       time.sleep(4)

       valuemin = float(slider.get_attribute("aria-valuemin"))
       valuemax = float(slider.get_attribute("aria-valuemax"))

    # 2. 트랙 바(span.relative.h-2.w-full) 기준 클릭 위치 계산
       track = container.find_element(By.CSS_SELECTOR, 'span.relative.h-2.w-full')
       track_width = track.size['width']
       track_height = track.size['height']

       ratio = (2.1 - valuemin) / (valuemax - valuemin)
       ratio = max(0.0, min(1.0, ratio))  # 0~1 사이 클램프
       offset_x = int(track_width * ratio)
       offset_y = track_height // 2

    # 3. 클릭 실행
       ActionChains(self.driver) \
        .move_to_element_with_offset(track, offset_x, offset_y) \
        .click() \
        .perform()

    # 4. 확인 출력
       time.sleep(0.2)
       actual_value = slider.get_attribute("aria-valuenow")
       print(f":dart: 목표: {2.1} → 실제값: {actual_value}")
       print("슬라이더 현재값:", slider.get_attribute("aria-valuenow"))

       time.sleep(5)
    # 음식 성향 - 짠 맛 슬라이더 변경
    def modify_team_salty(self):
       modal_tendency_area = self.driver.find_element(By.ID, "modal-root").find_element(By.CLASS_NAME, "space-y-6")
       container = modal_tendency_area.find_elements(By.CSS_SELECTOR, "div.flex.items-center")[1]
       slider = container.find_element(By.CSS_SELECTOR, 'span[role="slider"]')

       input_elem = slider.find_element(By.XPATH, './following-sibling::input')
       value = 2.1

       time.sleep(4)

       valuemin = float(slider.get_attribute("aria-valuemin"))
       valuemax = float(slider.get_attribute("aria-valuemax"))

    # 2. 트랙 바(span.relative.h-2.w-full) 기준 클릭 위치 계산
       track = container.find_element(By.CSS_SELECTOR, 'span.relative.h-2.w-full')
       track_width = track.size['width']
       track_height = track.size['height']

       ratio = (2.1 - valuemin) / (valuemax - valuemin)
       ratio = max(0.0, min(1.0, ratio))  # 0~1 사이 클램프
       offset_x = int(track_width * ratio)
       offset_y = track_height // 2

    # 3. 클릭 실행
       ActionChains(self.driver) \
        .move_to_element_with_offset(track, offset_x, offset_y) \
        .click() \
        .perform()

    # 4. 확인 출력
       time.sleep(0.2)
       actual_value = slider.get_attribute("aria-valuenow")
       print(f":dart: 목표: {2.1} → 실제값: {actual_value}")
       print("슬라이더 현재값:", slider.get_attribute("aria-valuenow"))

            
    # 음식 성향 - 매운 맛 슬라이더 변경
    def modify_team_hot(self):
       modal_tendency_area = self.driver.find_element(By.ID, "modal-root").find_element(By.CLASS_NAME, "space-y-6")
       container = modal_tendency_area.find_elements(By.CSS_SELECTOR, "div.flex.items-center")[2]
       slider = container.find_element(By.CSS_SELECTOR, 'span[role="slider"]')

       input_elem = slider.find_element(By.XPATH, './following-sibling::input')
       value = 2.1

       time.sleep(4)

       valuemin = float(slider.get_attribute("aria-valuemin"))
       valuemax = float(slider.get_attribute("aria-valuemax"))

    # 2. 트랙 바(span.relative.h-2.w-full) 기준 클릭 위치 계산
       track = container.find_element(By.CSS_SELECTOR, 'span.relative.h-2.w-full')
       track_width = track.size['width']
       track_height = track.size['height']

       ratio = (-10 - valuemin) / (valuemax - valuemin)
       ratio = max(0.0, min(1.0, ratio))  # 0~1 사이 클램프
       offset_x = int(track_width * ratio)
       offset_y = track_height // 2

    # 3. 클릭 실행
       ActionChains(self.driver) \
        .move_to_element_with_offset(track, offset_x, offset_y) \
        .click() \
        .perform()

    # 4. 확인 출력
       time.sleep(0.2)
       actual_value = slider.get_attribute("aria-valuenow")
       print(f":dart: 목표: {2.1} → 실제값: {actual_value}")
       print("슬라이더 현재값:", slider.get_attribute("aria-valuenow"))


    # 😃 이런 음식은 좋아요! 텍스트 변경
    def modify_team_favorite_text(self, favor_text):
        favorite_text_area = self.driver.find_element(By.CSS_SELECTOR, "[name='pros']")
        favorite_text_area.clear()  # 기존 내용 모두 삭제
        favorite_text_area.send_keys(favor_text)

    # ☹️ 이런 음식은 싫어요! 텍스트 변경
    def modify_team_hate_text(self, hate_text):
        hate_text_area = self.driver.find_element(By.CSS_SELECTOR, "[name='cons']")
        hate_text_area.clear()  # 기존 내용 모두 삭제
        hate_text_area.send_keys(hate_text)

    # 내 팀 > 팀이 먹은 메뉴 후기 추가 버튼 클릭
    def click_add_team_menu(self):
        self.driver.execute_script("window.scrollTo(0,600);")    # 버튼이 보이는 위치로 스크롤 이동
        team_add_menu_btn = self.driver.find_elements(By.CLASS_NAME, "cursor-pointer")[2]
        team_add_menu_btn.click()

    # 로그인 후 팀피드까지 진입하는 동작
    def into_team_feed(self):
        webutils = WebUtils(self.driver)
        # directories = Directories(driver)
        webutils.open_url()
        WebDriverWait(self.driver, 5).until(EC.url_contains("signin"))

        webutils.login("drowsy.work@gmail.com","Qwer1234!@")
        WebDriverWait(self.driver, 5).until(    # 페이지 타이틀 & 차트 떴는지 확인
            lambda _: EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[class *= 'text-title']"), "오늘 뭐먹지 ?")(self.driver)
            and EC.visibility_of_element_located((By.CSS_SELECTOR, "[role='img']"))(self.driver))
        webutils.click_tab_team()
