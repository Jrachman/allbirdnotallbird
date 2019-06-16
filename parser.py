# import web driver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

USER_EMAIL = "allbirdnotallbird@gmail.com"
USER_PASSWORD = "thisisnotanallbird8"
INSTAGRAM_ROOT_URL = "https://www.instagram.com"


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def initialize_driver():
    # specifies the path to the chromedriver.exe
    return webdriver.Chrome("./chromedriver")


def login_insta(driver):
    driver.get(f"{INSTAGRAM_ROOT_URL}/accounts/login/?source=auth_switcher")

    username = driver.find_element_by_name("username")
    username.send_keys(USER_EMAIL)

    password = driver.find_element_by_name("password")
    password.send_keys(USER_PASSWORD)
    password.submit()

    time.sleep(5)

    if check_exists_by_xpath(driver, "/html/body/div[3]"):
        actions = ActionChains(driver)
        actions.click()
        actions.send_keys(Keys.TAB * 2)
        actions.send_keys(Keys.ENTER)
        actions.perform()


if __name__ == "__main__":
    driver = initialize_driver()
    login_insta(driver)
