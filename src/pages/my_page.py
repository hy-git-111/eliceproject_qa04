import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver



class MyPage():
    def __init__(self, driver):
        self.driver = driver()

    # 개인 피드 버튼 클릭
    def open_mypage(self,driver):
        mypage_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[4]/a')
        mypage_btn.click()
        time.sleep(2)

    # 프로필 수정하기 버튼 클릭
    def profile_setup(self, driver):
        porfile_setup_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[1]/div[2]/div/svg/path')
        porfile_setup_btn.click()

    # 프로필 정보 수정 - 이미지 첨부 버튼 클릭
    # 여기서부터 다시 작업 예정
    # def image_attach(self):

    # 내가 먹은 메뉴
    def my_food_review(self, driver):
        my_food_add_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[2]/div[1]/button')
        my_food_add_btn.click()
        time.sleep(2)

    # 같은 메뉴 먹기
    def same_food_review(self, driver):
        same_food_review_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[2]/div[2]/div[1]/div[2]/button')
        same_food_review_btn.click()
