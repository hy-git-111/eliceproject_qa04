import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..resources.testdata.user_data import user_data

class WebUtils():

    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def open_url(self):
        url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/"
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    def click_element(self, by, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def scroll_to_element(self, by, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)  

    def click_back(self):
        back_btn = self.driver.find_element(By.CSS_SELECTOR, '.rounded-full.cursor-pointer')
        back_btn.click()
        time.sleep(1)

    def click_close(self):
        close_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[1]/button')
        close_btn.click()
        time.sleep(1)

    # 새로운 후기 등록하기 - 식사 유형 그룹
    def ate_group(self):
        ate_group_btn = self.driver.find_element(By.XPATH, '//*[@id="그룹"]')
        ate_group_btn.click()

    # 새로운 후기 등록하기 - 식사 유형 회식
    def ate_party(self):
        ate_party_btn = self.driver.find_element(By.XPATH, '//*[@id="회식"]')
        ate_party_btn.click()

    # 새로운 후기 등록하기 - 후기 사진 추가
    def review_image_attach(self):
        review_image_attach = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/button')
        review_image_attach.click()

    # 새로운 후기 등록하기 - 카테고리 드롭다운 클릭
    def review_category(self):
        review_category_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/button')
        review_category_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 한식
    def category_korean_food(self):
        korean_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[1]')
        korean_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 중식
    def category_chinese_food(self):
        chinese_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[2]')
        chinese_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 양식
    def category_western_food(self):
        western_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[3]')
        western_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 일식
    def category_japan_food(self):
        japan_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[4]')
        japan_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 분식
    def category_school_food(self):
        school_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[6]')
        school_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 아시안
    def category_asian_food(self):
        asian_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[5]')
        asian_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 패스트푸드
    def category_fast_food(self):
        fast_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[7]')
        fast_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 기타
    def category_etc_food(self):
        etc_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[8]')
        etc_food_btn.click()

    # 새로운 후기 등록하기 - 별점 1~5 버튼 클릭
    def star_review_one_click(self):
        star_review_one = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[6]/div/div[1]')
        star_review_one.click()

    def star_review_two_click(self):
        star_review_two = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[6]/div/div[2]')
        star_review_two.click()

    def star_review_three_click(self):
        star_review_three = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[6]/div/div[3]')
        star_review_three.click()

    def star_review_four_click(self):
        star_review_four = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[6]/div/div[4]')
        star_review_four.click()

    def star_review_five_click(self):
        star_review_five = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[6]/div/div[5]')
        star_review_five.click()

    # 새로운 후기 등록하기 - 후기 작성 완료 버튼 클릭
    def review_completed(self):
        review_completed_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/button')
        review_completed_btn.click()

    def click_tab_home(self):
        navigation_bar = self.driver.find_element(By.CSS_SELECTOR, ".bottom-0")
        tab_home = navigation_bar.find_elements(By.TAG_NAME,"a")[0]
        tab_home.click()
        time.sleep(1)

    def click_tab_team(self):
        navigation_bar = self.driver.find_element(By.CSS_SELECTOR, ".bottom-0")
        tab_home = navigation_bar.find_elements(By.TAG_NAME,"a")[1]
        tab_home.click()
        time.sleep(1)

    def click_tab_history(self):
        navigation_bar = self.driver.find_element(By.CSS_SELECTOR, ".bottom-0")
        tab_home = navigation_bar.find_elements(By.TAG_NAME,"a")[2]
        tab_home.click()
        time.sleep(1)

    def click_tab_personal(self):
        navigation_bar = self.driver.find_element(By.CSS_SELECTOR, ".bottom-0")
        tab_home = navigation_bar.find_elements(By.TAG_NAME,"a")[3]
        tab_home.click()
        time.sleep(1)

    # email, password를 입력해서 로그인하는 함수
    def login(self):
        btn_login = self.driver.find_element(By.XPATH, '//button[contains(@class, "bg-main")]')
        btn_login.click()

        input_email = self.driver.find_element(By.ID, 'username')
        input_email.send_keys(user_data["email"])
        input_password = self.driver.find_element(By.ID, 'password')
        input_password.send_keys(user_data["password"])

        btn_submit = self.driver.find_element(By.NAME, 'action')
        btn_submit.click()
        time.sleep(1)
