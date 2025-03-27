import pytest
import time
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










    # def my_profile(self):
    #     # 프로필 이미지
    #     profile_img = self.driver.find_element(By.XPATH,
    #                                       '//*[@id="root"]/div[1]/main/section/section/section/div[1]/div[1]/img')
    #     if profile_img:
    #         print("프로필 이미지 확인")
    #     else:
    #         print("프로필 이미지 미확인")
    #
    #     # 팀명
    #     profile_team = self.driver.find_element(By.XPATH,
    #                                        '//*[@id="root"]/div[1]/main/section/section/section/div[1]/div[2]/div/div')
    #     if profile_team:
    #         print("팀명 확인")
    #     else:
    #         print("팀명 미확인")
    #
    #     # 유저명
    #     profile_name = self.driver.find_element(By.XPATH,
    #                                        '//*[@id="root"]/div[1]/main/section/section/section/div[1]/div[2]/span').text
    #     if profile_name:
    #         print(f"사용자명: {profile_name}")
    #     else:
    #         print("사용자명 미식별")