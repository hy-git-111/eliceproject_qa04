import random
from src.utils.helpers import WebUtils
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from src.utils.locators import LOCATORS


# [홈 페이지]
class HomePage(WebUtils):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_eat_alone(self):
        self.click_element(*LOCATORS.get("eat_alone_btn"))

    def open_eat_together(self):
        self.click_element(*LOCATORS.get("eat_together_btn"))
    
    def open_eat_team(self):
        self.click_element(*LOCATORS.get("eat_team_btn"))


# [추천 옵션 선택 페이지]
class SelectOptionPage(WebUtils):

    def click_category_dropdown(self):
        self.click_element(*LOCATORS.get("dropdown"))

    def click_category_dropdown_option_randomly(self):
        options = self.driver.find_elements(*LOCATORS.get("options"))
        random_option = random.choice(options)
        random_option.click()

    def click_colleague_randomly(self):
        colleagues = self.driver.find_elements(*LOCATORS.get("colleague"))
        random_colleague = random.choice(colleagues)
        random_colleague.click()

    def search_colleague(self, text):
        self.click_element(*LOCATORS.get("search_field"))
        search_field = self.driver.find_element(*LOCATORS.get("search_field"))
        search_field.send_keys(text)

    def click_searched_colleague(self, text):
        colleagues = self.driver.find_elements(*LOCATORS.get("colleagues"))
    
        for colleague in colleagues:
            name_element = colleague.find_element(*LOCATORS.get("h2"))
            if name_element.text == text:
                colleague.click()
                break
            else:
                raise ValueError(f"일치하는 동료 '{text}'을(를) 찾을 수 없습니다.")

    def click_done_button(self):
        self.click_element(*LOCATORS.get("done_btn"))


# [메뉴 추천 페이지]
class RecommendationPage(WebUtils):
    
    def click_refresh_recommendation_button(self):
        self.click_element(*LOCATORS.get("refresh_recommendation_btn"))

    def click_accept_recommendation_button(self):
        self.click_element(*LOCATORS.get("accept_recommendation_btn"))