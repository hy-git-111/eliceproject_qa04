import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.conftest import driver
from ..utils.helpers import WebUtils

class MyPage():
    def __init__(self, driver:WebDriver):
        self.driver = driver

    # 개인 피드 버튼 클릭
    def open_mypage(self):
        mypage_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[4]/a')
        mypage_btn.click()
        time.sleep(2)

    # 프로필 수정하기 버튼 클릭
    def profile_setup(self):
        porfile_setup_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/section/div[1]/div[2]/div/svg/path')
        porfile_setup_btn.click()

    # 프로필 정보 수정 - 이미지 첨부 버튼 클릭
    def image_attach(self):
        image_attach_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[1]/div/button')
        image_attach_btn.click()

    # 프로필 정보 수정 - 단 맛 슬라이더

    # 프로필 정보 수정 - 짠 맛 슬라이더

    # 프로필 정보 수정 - 매운 맛 슬라이더

    # 프로필 수정 완료 버튼 클릭
    def profile_setup_completed(self):
        profile_setup_completed_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/button')
        profile_setup_completed_btn.click()

    # 내가 먹은 메뉴 추가하기 버튼 클릭
    def my_food_review(self):
        my_food_add_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[2]/div[1]/button')
        my_food_add_btn.click()
        time.sleep(2)

    # 같은 메뉴 먹기 버튼 클릭
    def same_food_review(self):
        same_food_review_btn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/section/section/div[2]/div[2]/div[1]/div[2]/button')
        same_food_review_btn.click()


