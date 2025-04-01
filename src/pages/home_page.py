import random
from src.utils.helpers import WebUtils
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


# [홈 페이지]
class HomePage(WebUtils):
    eat_alone_btn_css_selector = "button.cursor-pointer:nth-of-type(1)"
    eat_together_btn_css_selector = "button.cursor-pointer:nth-of-type(2)"
    eat_team_btn_css_selector = "button.cursor-pointer:nth-of-type(3)"


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_eat_alone(self):
        self.click_element(By.CSS_SELECTOR, self.eat_alone_btn_css_selector)

    def open_eat_together(self):
        self.click_element(By.CSS_SELECTOR, self.eat_together_btn_css_selector)
    
    def open_eat_team(self):
        self.click_element(By.CSS_SELECTOR, self.eat_team_btn_css_selector)


# [추천 옵션 선택 페이지]
class SelectOptionPage(WebUtils):
    dropdown_css_selector = "button[role='combobox']"
    options_css_selector = "div[role='option']"
    colleague_css_selector = "div.flex.flex-col.gap-2.py-2"
    search_field_css_selector = "input.text-body"
    done_btn_xpath = "//button[text()='선택 완료']"


    def click_category_dropdown(self):
        self.click_element(By.CSS_SELECTOR, self.dropdown_css_selector)

    def click_category_dropdown_option_randomly(self):
        options = self.driver.find_elements(By.CSS_SELECTOR, self.options_css_selector)
        random_option = random.choice(options)
        random_option.click()

    def click_colleague_randomly(self):
        colleagues = self.driver.find_elements(By.CSS_SELECTOR, self.colleague_css_selector)
        random_colleague = random.choice(colleagues)
        random_colleague.click()

    def search_colleague(self, text):
        self.click_element(By.CSS_SELECTOR, self.search_field_css_selector)
        search_field = self.driver.find_element(By.CSS_SELECTOR, self.search_field_css_selector)
        search_field.send_keys(text)

    def click_searched_colleague(self, text):
        colleagues = self.driver.find_elements(By.CSS_SELECTOR, "div.flex.items-center.gap-6")
    
        for colleague in colleagues:
            name_element = colleague.find_element(By.TAG_NAME, "h2")
            if name_element.text == text:
                colleague.click()
                break
            else:
                raise ValueError(f"일치하는 동료 '{text}'을(를) 찾을 수 없습니다.")

    def click_done_button(self):
        self.click_element(By.XPATH, self.done_btn_xpath)


# [메뉴 추천 페이지]
class RecommendationPage(WebUtils):
    refresh_recommendation_btn_xpath = "//button[text()='다시 추천 받기']"
    accept_recommendation_btn_xpath = "//button[text()='추천 수락하기']"

    def scroll_to_buttons(self):
        self.scroll_to_element(By.XPATH, self.accept_recommendation_btn_xpath)

    def click_refresh_recommendation_button(self):
        self.click_element(By.XPATH, self.refresh_recommendation_btn_xpath)

    def click_accept_recommendation_button(self):
        self.click_element(By.XPATH, self.accept_recommendation_btn_xpath)