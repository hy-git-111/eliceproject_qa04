import random
from src.utils.helpers import WebUtils
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


# [홈 페이지]
class HomePage:
    eat_alone_btn_xpath = "(//button[contains(@class, 'cursor-pointer')])[1]"
    eat_together_btn_xpath = "(//button[contains(@class, 'cursor-pointer')])[2]"
    eat_team_xpath = "(//button[contains(@class, 'cursor-pointer')])[3]"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # WebUtils 사용하여 [홈 페이지] 진입 함수 추가 필요

    def open_eat_alone(self):
        self.click_element(By.XPATH, self.eat_alone_btn_xpath)

    def open_eat_together(self):
        self.click_element(By.XPATH, self.eat_together_btn_xpath)
    
    def open_eat_team(self):
        self.click_element(By.XPATH, self.eat_team_xpath)


# 혼자 먹기, 회식 하기의 [추천 옵션 선택 페이지]
class SelectOptionPage:
    dropdown_xpath = "//button[@role='combobox']"
    options_xpath = "//button[@role='option']"
    done_btn_xpath = "//buton[text()='선택 완료']"
    
    # 뒤로 가기 추가 필요

    def click_category_dropdown(self):
        self.click_element(By.XPATH, self.dropdown_xpath)

    def click_category_dropdown_option(self):
        options = self.driver.find_elements(By.XPATH, self.options_xpath)
        random_option = random.choice(options)
        random_option.click()

    def click_done_button(self):
        self.click_element(By.XPATH, self.done_btn_xpath)


# 같이 먹기의 [추천 옵션 선택 페이지]


# [메뉴 추천 페이지]
class RecommendationPage:
    buttons_xpath = "(//button[contains(@class, 'cursor-pointer') and (text()='다시 추천 받기' or text()='추천 수락하기')])"
    refresh_recommendation_btn_xpath = "//button[text()='다시 추천 받기']"
    accept_recommendation_btn_xpath = "//button[text()='추천 수락하기']"

    # 뒤로 가기 추가 필요

    def scroll_to_buttons(self):
        self.scroll_to_element(By.XPATH, self.refresh_recommendation_btn_xpath)

    def click_refresh_recommendation_button(self):
        self.click_element(By.XPATH, self.refresh_recommendation_btn_xpath)

    def click_accept_recommendation_button(self):
        self.click_element(By.XPATH, self.accept_recommendation_btn_xpath)

    