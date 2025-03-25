import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from tests.conftest import driver

class MyPage():
    def __init__(self, driver):
        self.driver = driver()

    # 마이페이지 버튼 클릭
    def open_mypage(self, driver):
        mypage_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[4]/a')
        mypage_btn.click()
        time.sleep(2)

    # 프로필 요소 확인
    def my_profile(self, driver):
        # 프로필 이미지
        profile_img = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[1]/div[1]/img')
        if profile_img:
            print("프로필 이미지 확인")
        else:
            print("프로필 이미지 미확인")

        # 팀명
        profile_team = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[1]/div[2]/div/div')
        if profile_team:
            print("팀명 확인")
        else:
            print("팀명 미확인")

        # 유저명
        profile_name = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[1]/div[2]/span').text
        if profile_name:
            print(f"사용자명: {profile_name}")
        else:
            print("사용자명 미식별")