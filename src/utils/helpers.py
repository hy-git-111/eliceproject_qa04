import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from src.resources.testdata.expected_texts import EXPECTED_TEXTS
from src.utils.locators import LOCATORS

class WebUtils():

    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    # 로그인 페이지 열기
    def open_url(self):
        url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/"
        self.driver.get(url)

    # 요소 존재할 때까지 기다리기
    def wait_for_element_presence(self, by, value):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((by, value))
        )

    # 요소 클릭 가능할 때까지 기다리기
    def wait_for_element_clickable(self, by, value):
        WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((by, value))
            )
        
    # 요소 사라질 때까지 기다리기
    def wait_for_element_invisible(self, by, value):
        WebDriverWait(self.driver, 5).until(
                    EC.invisibility_of_element_located((by, value))
                )

    # 요소 찾아 클릭
    def click_element(self, by, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    # 요소로 스크롤
    def scroll_to_element(self, by, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)  

    # 뒤로 가기
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
        atd_group_btn = self.driver.find_element(By.XPATH, 'button[value="그룹"]')
        atd_group_btn.click()

    # 새로운 후기 등록하기 - 식사 유형 회식
    def ate_party(self):
        ate_party_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[value="회식"]')
        ate_party_btn.click()

    # 새로운 후기 등록하기 - 후기 사진 버튼 선택
    def review_image_attach(self):
        review_image_attach = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/button')
        review_image_attach.click()
        
    # 새로운 후기 등록하기 - 메뉴 명 입력
    def review_title_write(self, menu_text):
        self.driver.find_element(By.NAME, "menu").send_keys(menu_text)

    # 새로운 후기 등록하기 - 카테고리 드롭다운 클릭
    def review_category(self):
        review_category_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/button')
        review_category_btn.click()

    # 새로운 후기 등록하기 - 카테고리 드롭다운 한식
    def category_korean_food(self):
        korean_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[1]')
        korean_food_btn.click()

    # 새로운 후기 등록하기 - 카테고리 드롭다운 중식
    def category_chinese_food(self):
        chinese_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[2]')
        chinese_food_btn.click()

    # 새로운 후기 등록하기 - 카테고리 드롭다운 양식
    def category_western_food(self):
        western_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[3]')
        western_food_btn.click()

    # 새로운 후기 등록하기 - 카테고리 드롭다운 일식
    def category_japan_food(self):
        japan_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[4]')
        japan_food_btn.click()

    # 새로운 후기 등록하기 - 카테고리 드롭다운 분식
    def category_school_food(self):
        school_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[6]')
        school_food_btn.click()

    # 새로운 후기 등록하기 - 카테고리 드롭다운 아시안
    def category_asian_food(self):
        asian_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[5]')
        asian_food_btn.click()

    # 새로운 후기 등록하기 - 카테고리 드롭다운 패스트푸드
    def category_fast_food(self):
        fast_food_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[4]/select/option[7]')
        fast_food_btn.click()

    # 새로운 후기 등록하기 - 카테고리 드롭다운 기타
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

    # 새로운 후기 등록하기 - 후기 내용 입력
    def review_comment_write(self, comment_text):
        self.driver.find_element(By.NAME, "comment").send_keys(comment_text)

    # 새로운 후기 등록하기 - 후기 작성 완료 버튼 클릭
    def review_completed(self):
        review_completed_btn = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/button')
        review_completed_btn.click()

    # 새로운 후기 등록하기 - 식사 유형 그룹
    def ate_group(self):
        atd_group_btn = self.driver.find_element(By.XPATH, 'button[value="그룹"]')
        atd_group_btn.click()

    # 새로운 후기 등록하기 - 식사 유형 회식
    def ate_party(self):
        ate_party_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[value="회식"]')
        ate_party_btn.click()

    # 새로운 후기 등록하기 - 후기 사진 버튼 선택
    def review_image_attach(self):
        review_image_attach = self.driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div[2]/section/form/div[2]/div/button')
        review_image_attach.click()
        
    # 새로운 후기 등록하기 - 메뉴 명 입력
    def review_title_write(self, menu_text):
        self.driver.find_element(By.NAME, "menu").send_keys(menu_text)

    # 새로운 후기 등록하기 - 카테고리 드롭다운 클릭
    def review_category(self):
        review_category_btn = self.driver.find_element(By.CSS_SELECTOR, '[role="combobox"]')
        review_category_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 한식
    def category_korean_food(self):
        korean_food_btn = self.driver.find_element(By.CSS_SELECTOR, '[value="한식"]')
        korean_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 중식
    def category_chinese_food(self):
        chinese_food_btn = self.driver.find_element(By.CSS_SELECTOR, '[value="중식"]')
        chinese_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 양식
    def category_western_food(self):
        western_food_btn = self.driver.find_element(By.CSS_SELECTOR, '[value="양식"]')
        western_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 일식
    def category_japan_food(self):
        japan_food_btn = self.driver.find_element(By.CSS_SELECTOR, '[value="일식"]')
        japan_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 분식
    def category_school_food(self):
        school_food_btn = self.driver.find_element(By.CSS_SELECTOR, '[value="분식"]')
        school_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 아시안
    def category_asian_food(self):
        asian_food_btn = self.driver.find_element(By.CSS_SELECTOR, '[value="아시안"]')
        asian_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 패스트푸드
    def category_fast_food(self):
        fast_food_btn = self.driver.find_element(By.CSS_SELECTOR, '[value="패스트푸드"]')
        fast_food_btn.click()

    # 새로운 후기 등록하기 - 카텍고리 드롭다운 기타
    def category_etc_food(self):
        etc_food_btn = self.driver.find_element(By.CSS_SELECTOR, '[value="기타"]')
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

    # 새로운 후기 등록하기 - 후기 내용 입력
    def review_comment_write(self, comment_text):
        self.driver.find_element(By.NAME, "comment").send_keys(comment_text)

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

    def login(self, id, pw):
        btn_login = self.driver.find_element(By.XPATH, '//button[contains(@class, "bg-main")]')
        btn_login.click()

        input_email = self.driver.find_element(By.ID, 'username')
        input_email.send_keys(id)
        input_password = self.driver.find_element(By.ID, 'password')
        input_password.send_keys(pw)

        btn_submit = self.driver.find_element(By.NAME, 'action')
        btn_submit.click()
        time.sleep(1)
        
    # 슬라이더 임시 코드
    def slider_sweet(self):
        taste_tendency_area = self.driver.find_element(By.CLASS_NAME, "space-y-6")
        sweet_bar = taste_tendency_area.find_elements(By.CSS_SELECTOR, "[dir='ltr']")[0]    # 단 맛 슬라이더 바 요소
        sweet_bar.click()   # 해당 요소의 정중앙 클릭 > 2.5

    def slider_salty(self):
        taste_tendency_area = self.driver.find_element(By.CLASS_NAME, "space-y-6")
        salty_bar = taste_tendency_area.find_elements(By.CSS_SELECTOR, "[dir='ltr']")[1]    # 짠 맛 슬라이더 바 요소
        salty_bar.click()   # 해당 요소의 정중앙 클릭 > 2.5

    def slider_hot(self):
        taste_tendency_area = self.driver.find_element(By.CLASS_NAME, "space-y-6")
        hot_bar = taste_tendency_area.find_elements(By.CSS_SELECTOR, "[dir='ltr']")[2]     # 매운 맛 슬라이더 바 요소
        hot_bar.click()   # 해당 요소의 정중앙 클릭 > 2.5

    def review_image_upload(self):
        current_file_dir = os.path.dirname(os.path.abspath(__file__))
        img_source = os.path.abspath(os.path.join(current_file_dir,"../resources/testdata/review_photo.jpg")) # 이미지 소스 경로

        upload_input = self.driver.find_element(By. CSS_SELECTOR, 'input.hidden')
        upload_input.send_keys(img_source)

class VerifyHelpers():
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    # 헬퍼함수 / elems = [d,d,d,d] 선언하고 사용
    # 공통사용시 LOCATORS 부분, key 부분만 바꾸면 됨
    def check_existence(self, keys):
        elements = []
        for key in keys:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(LOCATORS.get(key))
            )
            elements.append(element)
        return elements
    
    def check_children_existence(self, parent_key: str, children_keys: list):
        elements = []
        parent = self.driver.find_element(*LOCATORS.get(parent_key))

        for key in children_keys:
            element = parent.find_element(*LOCATORS.get(key))
            elements.append(element)
        return elements
        
    def get_children_text(self, parent_key: list, children_keys: list):
        texts = []
        parent = self.driver.find_element(*LOCATORS.get(parent_key))

        for key in children_keys:
            element = parent.find_element(*LOCATORS.get(key))
            texts.append(element.text)
        return texts

    def get_elem_text(self, by, value):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(LOCATORS.get(key))
        )

        for element in elements:
            texts.append(key.text)
        return texts
    
    def get_expected_texts(self, keys: list):
        titles = []
        for key in keys:
            titles.append(EXPECTED_TEXTS.get(key))
        return titles
    
    def cnt_elements(self, key: str):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(LOCATORS.get(key))
        )
        return len(element)
    
    def click_elem_with_infinity_scroll(self, key: str, value: str):
        while True:
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            time.sleep(2)
            try:
                target_btn_index = []
                all_btns = self.driver.find_elements(By.TAG_NAME, "button")
                target_btns_elems = self.driver.find_elements(key, value)
                if target_btns_elems != []:
                    for btn in all_btns:
                        if btn.text == target_btns_elems[0].text:
                            btn_index = all_btns.index(btn)
                            target_btn_index.append(btn_index)

                            self.driver.execute_script(
                                "arguments[0].focus();", btn
                            )
                            time.sleep(2)
                            self.driver.execute_script("arguments[0].click();", btn)
                            return target_btn_index[0]
                
                if target_btns_elems == []:
                    new_height = self.driver.execute_script("return document.body.scrollHeight")
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
                if new_height == last_height:
                    break

                last_height = new_height

            except NoSuchElementException:
                pass
