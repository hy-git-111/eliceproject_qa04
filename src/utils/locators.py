from selenium.webdriver.common.by import By

LOCATORS = {
    # [로그인 페이지]
    "login_pg_title_section": (By.CSS_SELECTOR, 'div.mb-8'),
    "login_pg_title": (By.CSS_SELECTOR, 'h1.mb-2'),
    "login_pg_subtitle": (By.CSS_SELECTOR, 'p.text-gray-600'),

    "login_pg_login_btn": (By.CSS_SELECTOR, 'button.bg-main'),
    "login_pg_signin_btn": (By.CSS_SELECTOR, 'button.bg-sub'),

    # [로그인 정보 입력 페이지]
    "login_input_pg_title_section": (By.CSS_SELECTOR, 'header.c825c97f8'),
    "login_input_pg_title": (By.CSS_SELECTOR, 'h1.ca90b15ee'),
    "login_input_pg_subtitle": (By.CSS_SELECTOR, 'body > div > main > section > div > div > header > div.ced95a2c2.ca6c299fa > p'),

    "login_input_pg_input_email": (By.ID, 'username'),
    "login_input_pg_input_pwd": (By.ID, 'password'), 
    "login_input_pg_placeholder_email": (By.CSS_SELECTOR, 'div[data-dynamic-label-for~="username"]'),
    "login_input_pg_placeholder_pwd": (By.CSS_SELECTOR, 'div[data-dynamic-label-for~="password"]'),

    "login_input_pg_link_reset_pwd": (By.CSS_SELECTOR, 'a.c7c6decd9'),
    "login_input_pg_link_signin": (By.CSS_SELECTOR, 'body > div > main > section > div > div > div > div > p > a'),
    "login_input_pg_btn_continue": (By.CSS_SELECTOR, 'button.cc02a3617'),
    
    # [비밀번호 초기화 페이지]
    "pwd_reset_pg_title": (By.CSS_SELECTOR, 'h1.ca90b15ee.c2bb004c2'),
    "pwd_reset_pg_subtitle": (By.CSS_SELECTOR, 'p.c53c6f72a'),

    "pwd_reset_pg_input_email": (By.ID, 'email'),
    "pwd_reset_pg_placeholder_email": (By.CSS_SELECTOR, 'div.cd61d9fdd.js-required'),

    "pwd_reset_pg_btn_continue": (By.CSS_SELECTOR, 'button.c1085a438'),
    "pwd_reset_pg_link_login": (By.CSS_SELECTOR, 'button._link-back-to-login'),

    #[이메일 전송 완료 페이지]
    "send_mail_pg_title": (By.CSS_SELECTOR, 'h1.c2b7602e3'),
    "send_mail_pg_subtitle": (By.CSS_SELECTOR, 'p.c53c6f72a'),

    "send_mail_pg_btn_resend": (By.CSS_SELECTOR, 'button.c20d4b85c'),

    # [회원가입 페이지]
    "signin_pg_title": (By.CSS_SELECTOR, 'h1.ca90b15ee'),
    "signin_pg_subtitle": (By.CSS_SELECTOR, 'body > div > main > section > div > div > header > div.ced95a2c2.ca6c299fa > p'),

    "signin_pg_input_email": (By.ID, 'email'),
    "signin_pg_input_pwd": (By.ID, 'password'),
    "signin_pg_placeholder_email": (By.CSS_SELECTOR, 'div[data-dynamic-label-for~="email"]'),
    "signin_pg_placeholder_pwd": (By.CSS_SELECTOR, 'div[data-dynamic-label-for~="password"]'),

    "signin_pg_pg_btn_continue": (By.CSS_SELECTOR, 'button.c1085a438'),
    "signin_pg_link_login": (By.CSS_SELECTOR, 'a.c61ec4995'),

    "signin_pg_pw_rule_section": (By.CSS_SELECTOR, 'div.c0829f7cd.c12b49435'),
    "signin_pg_pw_rule_title": (By.CSS_SELECTOR, 'span'),
    "signin_pg_pw_rule_char_num": (By.CSS_SELECTOR, 'ul > li:nth-child(1) > span'),
    "signin_pg_pw_rule_following": (By.CSS_SELECTOR, 'ul > li:nth-child(2) > span'),
    "signin_pg_pw_rule_following_Lower_letters": (By.CSS_SELECTOR, 'ul > li:nth-child(2) > div > ul > li.c81063452.ced6f80b9 > span'),
    "signin_pg_pw_rule_following_upper_letters": (By.CSS_SELECTOR, 'ul > li:nth-child(2) > div > ul > li:nth-child(2) > span'),
    "signin_pg_pw_rule_following_num": (By.CSS_SELECTOR, 'ul > li:nth-child(2) > div > ul > li:nth-child(3) > span'),
    "signin_pg_pw_rule_following_special_char": (By.CSS_SELECTOR, 'ul > li:nth-child(2) > div > ul > li:nth-child(4) > span'),
    
    "signin_pg_pw_btn_continue": (By.CSS_SELECTOR, 'button.c1085a438'),

    # [권한 요청 페이지]
    "authorize_pg_title": (By.CLASS_NAME, 'ca90b15ee'),

    "authorize_pg_form": (By.CLASS_NAME, 'cb9c43b77'),
    "authorize_pg_email": (By.CSS_SELECTOR, 'div.c1d737aca.ca387354c > p:nth-child(1)'),
    "authorize_pg_subtitle": (By.CSS_SELECTOR, 'div.c1d737aca.ca387354c > p:nth-child(2)'),
    "authorize_pg_requested_authorize": (By.XPATH, '//div/ul/li/span'),
    
    "authorize_pg_btn_accept": (By.CLASS_NAME, 'c1085a438'),
    "authorize_pg_btn_decline": (By.CLASS_NAME, 'c20d4b85c'),

    # [로그인 오류 페이지]
    "error_pg_title": (By.CLASS_NAME, 'mb-2'),
    "error_pg_subtitle": (By.CLASS_NAME, 'text-gray-600'),

    "error_pg_btn_retry": (By.CLASS_NAME, 'py-2'),

    # [프로필 입력 페이지]
    "profile_pg_title" : (By.XPATH, '//div[contains(@class, "gap-4")]/span'),
    "profile_pg_form" : (By.CLASS_NAME, 'space-y-8'),
    "profile_pg_name_title" : (By.CSS_SELECTOR, 'div:nth-child(1) > p'),
    "profile_pg_name_input" : (By.CSS_SELECTOR, 'div:nth-child(1) > div > input'),
    "profile_pg_name_placeholder" : (By.CSS_SELECTOR, 'div:nth-child(1) > div > input'),
  
    "profile_pg_team_title" : (By.CSS_SELECTOR, 'div:nth-child(2) > p'),
    "profile_pg_team_dropdown" : (By.CSS_SELECTOR, 'div:nth-child(2) > div > button'),
    
    "profile_pg_taste_title" : (By.CSS_SELECTOR, 'div:nth-child(3) > p'),
    "profile_pg_taste_slider_sweetness" : (By.CSS_SELECTOR, 'div:nth-child(3) > div > section:nth-child(1) > div'),
    "profile_pg_taste_slider_salty" : (By.CSS_SELECTOR, 'div:nth-child(3) > div > section:nth-child(2) > div'),
    "profile_pg_taste_slider_spicy" : (By.CSS_SELECTOR, 'div:nth-child(3) > div > section:nth-child(3) > div'),
    
    "profile_pg_preference_title" : (By.CSS_SELECTOR, 'div:nth-child(4) > p'),
    "profile_pg_like_title" : (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(1) > p'),
    "profile_pg_like_input" : (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(1) > div > textarea'),
    "profile_pg_dislike_title" : (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(2) > p'),
    "profile_pg_dislike_input" : (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(1) > div > textarea'),
    
    "profile_pg_btn_submit" : (By.CLASS_NAME, 'bg-main'),
    
    "profile_pg_error_name" : (By.CSS_SELECTOR, 'div:nth-child(1) > div > p'),
    "profile_pg_error_team" : (By.CSS_SELECTOR, 'div:nth-child(2) > div > p'),
    "profile_pg_error_sweetness" : (By.CSS_SELECTOR, 'div:nth-child(3) > div > p:nth-child(2)'),
    "profile_pg_error_salty" : (By.CSS_SELECTOR, 'div:nth-child(3) > div > p:nth-child(4)'),
    "profile_pg_error_spicy" : (By.CSS_SELECTOR, 'div:nth-child(3) > div > p:nth-child(6)'),
    "profile_pg_error_like" : (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(1) > div > div > p'),
    "profile_pg_error_dislike" : (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(2) > div > div > p'),
   
    # [홈 페이지]
    "home_pg_subtitle": (By.CLASS_NAME, 'py-1'),

    # [히스토리 페이지]
    "history_pg_btn_back": (By.CSS_SELECTOR, 'header > div > svg'),
    "history_pg_title": (By.CSS_SELECTOR, 'header > div > span'),
    "history_pg_subtitle": (By.CSS_SELECTOR, 'span.text-sub-2.text-title'),

    "history_pg_list": (By.CLASS_NAME, 'shadow-md'),
    "history_pg_list_1": (By.CSS_SELECTOR, 'section > div:nth-child(2)'),
    "history_pg_list_10": (By.CSS_SELECTOR, 'section > div:nth-child(11)'),
    "history_pg_list_20": (By.CLASS_NAME, 'section > div:nth-child(21)'),
    "history_pg_btn_before_review": (By.CSS_SELECTOR, 'button.bg-main-black'),
    "history_pg_btn_after_review": (By.CSS_SELECTOR, 'button.bg-main'),

    # [후기 등록 페이지]
    "review_pg_btn_exit": (By.CLASS_NAME, 'text-2xl'),
}