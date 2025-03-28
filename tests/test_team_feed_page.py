import time
import pytest
from src.utils.helpers import WebUtils
from src.pages.team_feed_page import TeamFeed
from src.utils.directory_util import Directories
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestTeamFeedPage:
    def into_team_feed(self, driver): # 팀 피드 진입 기능
        webutils = WebUtils(driver)
        # directories = Directories(driver)
        webutils.open_url()
        ws(driver, 5).until(EC.url_contains("signin"))

        webutils.login()
        ws(driver, 5).until(    # 페이지 타이틀 & 차트 떴는지 확인
            lambda _: EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[class *= 'text-title']"), "오늘 뭐먹지 ?")(driver)
            and EC.visibility_of_element_located((By.CSS_SELECTOR, "[role='img']"))(driver))
        webutils.click_tab_team()

    @pytest.mark.skip(reason="passed")
    def test_team_001(self, driver):
        # Settings & Precondition & Stpes
        # directories = Directories(driver)
        self.into_team_feed(driver)

        # Expected Result
        ws(driver, 5).until(    # 페이지 타이틀 & 팀 이름 확인 (팀 이름은 DB 확인 가능여부 체크 필요)
            lambda _: EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class*='text-title']"), "팀 피드")(driver)
            and EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[style='pointer-events: none;']"), "디자인 1팀")(driver))

    @pytest.mark.skip(reason="passed")
    def test_team_002(self, driver):
       # Settings & Precondition
       webutils = WebUtils(driver)
       #directories = Directories(driver)
       self.into_team_feed(driver)

       # Steps
       webutils.click_back()

       # Expected Result
       ws(driver, 5).until(
           lambda _: EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[class *= 'text-title']"), "오늘 뭐먹지 ?")(driver)
           and EC.visibility_of_element_located((By.CSS_SELECTOR, "[role='img']"))(driver))        

    @pytest.mark.skip(reason="failed")
    def test_team_003(self, driver):
        # Settings
        webutils = WebUtils(driver)
        team_feed = TeamFeed(driver)
        #dir = Directories(driver)

        # Preconditions
        self.into_team_feed(driver)
        ws(driver, 5).until(    # 페이지 타이틀 & 팀 이름 확인 (팀 이름은 DB 확인 가능여부 체크 필요)
            lambda _: EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class*='text-title']"), "팀 피드")(driver)
            and EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[style='pointer-events: none;']"), "디자인 1팀")(driver))
        team_feed.open_team_combobox()
        team_feed.select_team_combobox(0)
        ws(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[style='pointer-events: none;']"), "개발 1팀"))
        
        # Steps
        webutils.click_back()

        # Expected Result
        ws(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[style='pointer-events: none;']"), "디자인 1팀"))

    @pytest.mark.skip(reason="postpone - 많은 요소 검증이어서 마지막에 요소별로 확인하는 코드 넣을 예정")
    def test_team_004(self, driver):
        # Settings
        #dir = Directories(driver)

        wait_time = ws(driver, 5)

        # Preconditions & Steps
        self.into_team_feed(driver)

        # Expected Result - 검증 요소가 너무 많아서 추후 작성 예정

    @pytest.mark.skip(reason="postpone - 스크린샷 이용해볼 예정 / XPATH로 요소 감지 시도 먼저 하기")
    def test_team_005(self, driver):
        # Settings
        webutils = WebUtils(driver)
        team_feed = TeamFeed(driver)
        #dir = Directories(driver)
        
        # Preconditions
        self.into_team_feed(driver)
        
        # Steps
        team_feed.open_team_combobox()
        team_feed.select_team_combobox(0)

        # Expected Result
        # 스크린샷으로 해봐야할지..
        # 요소 특정이 어려워서 그 요소가 안 나왔다고 표현이 어렵다

    #@pytest.mark.skip(reason="postpone - 스크린샷 이용해볼 예정 / XPATH로 요소 감지 시도 하기")
    def test_team_005(self, driver):
        # Settings
        team_feed = TeamFeed(driver)
        #dir = Directories(driver)
        
        # Preconditions
        self.into_team_feed(driver)
        
        # Steps
        team_feed.open_team_combobox()
        team_feed.select_team_combobox(2)

    @pytest.mark.skip(reason="postpone - 스크린샷 이용해볼 예정 / XPATH로 요소 감지 시도 하기")
    def test_team_005(self, driver):
        # Settings
        team_feed = TeamFeed(driver)
        #dir = Directories(driver)
        
        # Preconditions
        self.into_team_feed(driver)
        
        # Steps
        team_feed.open_team_combobox()
        team_feed.select_team_combobox(2)

        # Expected Results
        ws(driver, 3).until(EC.invisibility_of_element, ((By.XPATH, "//*[@id='root']/div[1]/main/section/section/section/div[1]/div/div/svg")))


    @pytest.mark.skip(reason="pass")
    def test_team_006(self, driver):
        # Settings
        team_feed = TeamFeed(driver)
        #dir = Directories(driver)
        
        # Preconditions & Steps
        self.into_team_feed(driver)
        
        # Expected Result
        ws(driver, 5).until(EC.visibility_of_element_located, (By.XPATH, "//*[@id='root']/div[1]/main/section/section/section/div[1]/div/div/svg"))
        team_feed.select_modify_team_profile_icon()

    @pytest.mark.skip(reason="pass")
    def test_team_007(self, driver):
        # Settings
        team_feed = TeamFeed(driver)
        #dir = Directories(driver)
        
        # Preconditions & Steps
        self.into_team_feed(driver)
        team_feed.open_team_combobox()
        team_feed.select_team_combobox(0)
        driver.execute_script("window.scrollTo(0,600);")
        ws(driver, 5).until(EC.visibility_of_element_located, (By.CSS_SELECTOR, '.flex.w-full.gap-6.p-4.shadow-md.rounded-2xl'))
                
        # Expected Result
        ws(driver, 3).until(EC.invisibility_of_element, ((By.XPATH, "//*[@id='root']/div[1]/main/section/section/div[3]/div[1]/button")))
    
    @pytest.mark.skip(reason="pass")
    def test_team_008(self, driver):
        # Settings
        team_feed = TeamFeed(driver)
        #dir = Directories(driver)
        
        # Preconditions & Steps
        self.into_team_feed(driver)
        team_feed.open_team_combobox()
        team_feed.select_team_combobox(2)
        driver.execute_script("window.scrollTo(0,600);")
        ws(driver, 5).until(EC.visibility_of_element_located, (By.CSS_SELECTOR, '.flex.w-full.gap-6.p-4.shadow-md.rounded-2xl'))
                
        # Expected Result
        ws(driver, 3).until(EC.visibility_of_element_located, ((By.XPATH, "//*[@id='root']/div[1]/main/section/section/div[3]/div[1]/button")))
    
    