# 팀 피드 페이지 기능
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
    def select_modify_team_profile_icon(self):
        team_modify_icon = self.driver.find_elements(By.CLASS_NAME, "cursor-pointer")[1]
        team_modify_icon.click()

    # 프로필 정보 수정 > 프로필 수정 완료 버튼 클릭
    def click_team_profile_modify_done(self):
        team_modify_done_btn = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")
        team_modify_done_btn.click()
    
    # 음식 성향 - 단 맛 슬라이더 변경
    def modify_team_sweet(self):
       print("코드 삽입 예정")

    # 음식 성향 - 짠 맛 슬라이더 변경
    def modify_team_salty(self):
        print("코드 삽입 예정")
            
    # 음식 성향 - 매운 맛 슬라이더 변경
    def modify_team_hot(self):
        print("코드 삽입 예정")

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

    # 팀 통계 부분은 나중에 여유될 때 진행합니다. (차트 영역 확인)
    # 테스트 코드에서 차트 요소 불러왔는지만 확인 예정

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