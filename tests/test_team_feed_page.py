import pytest
from src.utils.helpers import WebUtils
from src.utils.directory_util import Directories
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver 

# @pytest.mark.skip(reason="passed")
class TestTeamFeedPage:
    def test_team_001(self):
        self.driver = webdriver.Chrome()
        webutils = WebUtils(self.driver)
        #dir = Directories(self.driver)

        wait_time = ws(self.driver, 5)

        webutils.open_url()
        wait_time.until(EC.url_contains("signin"))

        webutils.login()
        wait_time.until(    # 페이지 타이틀 & 차트 떴는지 확인
            lambda _: EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[class *= 'text-title']"), "오늘 뭐먹지 ?")(self.driver)
            and EC.visibility_of_element_located((By.CSS_SELECTOR, "[role='img']"))(self.driver))
        webutils.click_tab_team()
        wait_time.until(    # 페이지 타이틀 & 팀 이름 확인 (팀 이름은 DB 확인 가능여부 체크 필요)
            lambda _: EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class*='text-title']"), "팀 피드")(self.driver)
            and EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[style='pointer-events: none;']"), "디자인 1팀")(self.driver))
