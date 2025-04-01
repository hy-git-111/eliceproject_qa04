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
    
    "signin_pg_btn_continue": (By.CSS_SELECTOR, 'button.c1085a438'),
    

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
    "profile_pg_team_btn" : (By.CSS_SELECTOR, 'div:nth-child(2) > div > button'),
    "profile_pg_team_selector" : (By.CSS_SELECTOR, 'div:nth-child(2) > div > select'),
    
    "profile_pg_taste_title" : (By.CSS_SELECTOR, 'div:nth-child(3) > p'),
    "profile_pg_taste_slider_sweetness" : (By.CSS_SELECTOR, 'div:nth-child(3) > div > section:nth-child(1) > div'),
    "profile_pg_taste_slider_salty" : (By.CSS_SELECTOR, 'div:nth-child(3) > div > section:nth-child(2) > div'),
    "profile_pg_taste_slider_spicy" : (By.CSS_SELECTOR, 'div:nth-child(3) > div > section:nth-child(3) > div'),
    
    "profile_pg_preference_title" : (By.CSS_SELECTOR, 'div:nth-child(4) > p'),
    "profile_pg_like_title" : (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(1) > p'),
    "profile_pg_like_input" : (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(1) > div > textarea'),
    "profile_pg_dislike_title" : (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(2) > p'),
    "profile_pg_dislike_input" : (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(2) > div > textarea'),
    
    "profile_pg_btn_submit" : (By.CLASS_NAME, 'bg-main'),
    
    "profile_pg_error_name" : (By.CSS_SELECTOR, 'div:nth-child(1) > div > p'),
    "profile_pg_error_team" : (By.CSS_SELECTOR, 'div:nth-child(2) > div > p'),
    "profile_pg_error_sweetness" : (By.CSS_SELECTOR, 'div:nth-child(3) > div > p:nth-child(2)'),
    "profile_pg_error_salty" : (By.CSS_SELECTOR, 'div:nth-child(3) > div > p:nth-child(4)'),
    "profile_pg_error_spicy" : (By.CSS_SELECTOR, 'div:nth-child(3) > div > p:nth-child(6)'),
    "profile_pg_error_like" : (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(1) > div > div > p'),
    "profile_pg_error_dislike" : (By.CSS_SELECTOR, 'div:nth-child(4) > div > div:nth-child(2) > div > div > p'),
   
    # [홈 페이지]
    "home_pg_subtitle_1": (By.CSS_SELECTOR, 'p.pb-4.text-sub-2'),
    "home_pg_subtitle_2": (By.CLASS_NAME, 'py-1'),

    "eat_alone_btn": (By.CSS_SELECTOR, 'button.cursor-pointer:nth-of-type(1)'),
    "eat_together_btn": (By.CSS_SELECTOR, 'button.cursor-pointer:nth-of-type(2)'),
    "eat_team_btn": (By.CSS_SELECTOR, 'button.cursor-pointer:nth-of-type(3)'),

    "header_text": (By.CSS_SELECTOR, 'header span.text-title'),
    "ai_recommendation_text": (By.CSS_SELECTOR, 'p.text-body'),
    "eat_alone_text": (By.CSS_SELECTOR, 'div.flex.items-center:nth-of-type(1) p'),
    "eat_together_text": (By.CSS_SELECTOR, 'div.flex.items-center:nth-of-type(2) p'),
    "eat_team_text": (By.CSS_SELECTOR, 'div.flex.items-center:nth-of-type(3) p'),
    "employee_preference_text": (By.CSS_SELECTOR, 'span.text-body'),
    "preference_analysis_chart": (By.CSS_SELECTOR, 'canvas[role=\'img\']'),
    "menu_suggestion_text": (By.CSS_SELECTOR, 'h1.text-body.text-sub-2'),
    "menu_suggestion_subtext": (By.CSS_SELECTOR, 'div.pb-4 > h2.text-lg.text-dark-gray'),
    "my_preference_text": (By.CSS_SELECTOR, 'span.text-body.font-bold.text-sub-2:not(.py-1)'),
    "my_preference_subtext": (By.XPATH, '//h2[contains(text(), \'취향 데이터\')]'),
    "navigation_bar": (By.CSS_SELECTOR, 'div.fixed.bottom-0'),
    "navigation_home_icon": (By.CSS_SELECTOR, 'a.text-main path'),
    "navigation_home_text": (By.CSS_SELECTOR, 'a.text-main span'),

    # [홈 > 추천 옵션 선택 페이지]
    "dropdown": (By.CSS_SELECTOR, 'button[role=\'combobox\']'),
    "dropdown_text" : (By.CSS_SELECTOR, 'button[role=\'combobox\ span'),
    "options": (By.CSS_SELECTOR, 'div[role=\'option\']'),
    "selected_option_text": (By.CSS_SELECTOR, 'span[style=\'pointer-events: none;\']'),
    "colleague": (By.CSS_SELECTOR, 'div.flex.flex-col.gap-2.py-2'),
    "colleagues": (By.CSS_SELECTOR, 'div.flex.items-center.gap-6'),
    "search_field": (By.CSS_SELECTOR, 'input.text-body'),
    "done_btn": (By.XPATH, '//button[text()=\'선택 완료\']'),

    "select_category_text": (By.CSS_SELECTOR, 'span.font-bold.text-sub-2.text-title'),
    "eating_people_text": (By.XPATH, '//span[contains(text(), \'인원\')]'),
    "eating_people": (By.CSS_SELECTOR, 'div.scrollbar-hide'),
    "eating_people_profie_image" : (By.CSS_SELECTOR, 'div.scrollbar-hide img.aspect-square'),
    "profile_image": (By.CSS_SELECTOR, 'img.aspect-square'),
    "profile_name": (By.CSS_SELECTOR, 'div.font-semibold'),
    "profile_team": (By.CSS_SELECTOR, 'div.text-gray-500'),
    "profile_checkbox": (By.CSS_SELECTOR, 'input[type=\'checkbox\']'),
    "profile_cancel_btn": (By.CSS_SELECTOR, 'svg.absolute'),
    "team": (By.CSS_SELECTOR, 'div.bg-sub-2'),
    "division": (By.CSS_SELECTOR, 'div.border-t'),
    "search_field": (By.CSS_SELECTOR, 'input[type=\'text\']'),
    "user_list": (By.CSS_SELECTOR, 'div.flex.items-center.justify-between'),
    "searched_user": (By.CSS_SELECTOR, 'ul.absolute'),
    "searched_user_first_one": (By.CSS_SELECTOR, 'ul.absolute:nth-of-type(1)'),
    "searched_profile_image": (By.CSS_SELECTOR, 'img.rounded-full'),
    "searched_profile_name": (By.TAG_NAME, 'h2'),
    "searched_profile_team": (By.CSS_SELECTOR, 'h2.text-subbody'),

    # [홈 > 메뉴 추천 페이지]
    "refresh_recommendation_btn": (By.XPATH, '//button[text()=\'다시 추천 받기\']'),
    "accept_recommendation_btn": (By.XPATH, '//button[text()=\'추천 수락하기\']'),

    "menu_recommendation_text": (By.CSS_SELECTOR, 'span.font-bold.text-body'),
    "menu_text": (By.CSS_SELECTOR, 'span.text-main'),
    "food_image": (By.CSS_SELECTOR, 'img.rounded-lg'),
    "ai_analysis_text": (By.XPATH, '//span[contains(text(), \'분석\')]'),
    "ai_analysis_percentage": (By.CSS_SELECTOR, 'div.text-xs'),
    "restaurant_list_text": (By.CSS_SELECTOR, 'div.gap-2 > span.text-body'),
    "restaurant_list": (By.CSS_SELECTOR, 'div.swiper-wrapper'),
    "no_search_result_section": (By.CSS_SELECTOR, 'section.border-light-gray'),
    "no_search_result_text": (By.CSS_SELECTOR, 'h1.text-body'),
    "no_search_result_image": (By.TAG_NAME, 'rect'),

    # [히스토리 페이지]
    "history_pg_btn_back": (By.CSS_SELECTOR, 'header > div > svg'),
    "history_pg_title": (By.CSS_SELECTOR, 'header > div > span'),
    "history_pg_subtitle": (By.CSS_SELECTOR, 'span.text-sub-2.text-title'),

    "history_pg_list": (By.CLASS_NAME, 'shadow-md'),
    "history_pg_list_1": (By.CSS_SELECTOR, 'section > div:nth-child(2)'),
    "history_pg_list_10": (By.CSS_SELECTOR, 'section > div:nth-child(11)'),
    "history_pg_list_11": (By.CSS_SELECTOR, 'section > div:nth-child(12)'),
    "history_pg_list_20": (By.CLASS_NAME, 'section > div:nth-child(21)'),
    "history_pg_list_21": (By.CLASS_NAME, 'section > div:nth-child(22)'),

    "history_pg_btn_before_review": (By.CSS_SELECTOR, 'button.bg-main-black'),
    "history_pg_btn_after_review": (By.CSS_SELECTOR, 'button.bg-main'),

    "history_food_image": (By.CSS_SELECTOR, 'img.rounded-lg'),
    "history_tag": (By.CSS_SELECTOR, 'div.text-xs'),
    "history_menu_text": (By.CSS_SELECTOR, 'div.font-bold'),

    # [후기 등록 페이지]
    "review_pg_btn_exit": (By.CLASS_NAME, 'text-2xl'),
    "review_pg_btn_radio_alone": (By.ID, '혼밥'),
    "review_pg_btn_radio_group": (By.ID, '그룹'),
    "review_pg_btn_radio_team": (By.ID, '회식'),
    "review_pg_input_menu": (By.CSS_SELECTOR, 'input[name~=menu]'),
    "review_pg_drop_down_category": (By.CSS_SELECTOR, '#modal-root > div > div.flex-1.overflow-auto > section > form > div:nth-child(4) > button > span'),
    "review_pg_input_review": (By.CSS_SELECTOR, 'input[name~=menu]'),
    
}