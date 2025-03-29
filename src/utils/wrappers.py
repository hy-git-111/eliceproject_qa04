from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementNotSelectableException
from src.utils.directory_util import Directories
from src.utils.log_util import LogUtils

from functools import wraps
import functools
import logging


def wrapper_test_login_page(test_func):
    func_name = test_func.__name__  # wraper 실행 시 내부 wrapper에 의해 name 속성이 변경되므로, wraper함수 호출 전에 메서드명을 정의

    @functools.wraps(test_func)
    def wrapper(self, *args, **kwargs):
        try:
            # logger = logging.getLogger("myTestLogger")
            driver = kwargs.get("driver", None)
            result = test_func(self, *args, **kwargs)
            # logger.info(f"{func_name} - 테스트 완료")
            # print(f"{func_name} - 테스트 완료")
            # return test_func(self, **kwargs)
            return result
        
# 추후 분리 예정
        except Exception as e:
            LogUtils.log_error(e, driver)
            raise

        # except AssertionError as e:
        #     # self.driver.save_screenshot(self.dir_util.screenshots_path(f"{func_name}_AssertionError.png"))
        #     # logger.error(f"{func_name} - {e}")
        #     raise

        # except NoSuchElementException as e:
        #     # driver.save_screenshot(self.dir_util.screenshots_path(f"{func_name}_NoSuchElementException.png"))
        #     # logger.error(f"{func_name} - {e}")
        #     raise

        # except TimeoutException as e:
        #     # driver.save_screenshot(self.dir_util.screenshots_path(f"{func_name}_TimeoutException.png"))
        #     # logger.error(f"{func_name} - {e}")
        #     raise

        # except StaleElementReferenceException as e:
        #     # driver.save_screenshot(self.dir_util.screenshots_path(f"{func_name}_InvalidElementStateException.png"))
        #     # logger.error(f"{func_name} - StaleElementReferenceException")
        #     raise

        # except ElementNotSelectableException as e:
        #     # driver.save_screenshot(self.dir_util.screenshots_path(f"{func_name}_ElementNotSelectableException.png"))
        #     # logger.error(f"{func_name} - {e}")
        #     raise

        # except Exception as e:
        #     # driver.save_screenshot(self.dir_util.screenshots_path(f"{func_name}_Other_Exception.png"))
        #     # logger.error(f"{func_name} - Other Exception: {e}")
        #     raise

    return wrapper

