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
    driver = webdriver.Chrome("./chromedriver")
    return driver, ActionChains(driver)


def get_srcs(set_of_srcs):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return {thing.get("src") for thing in soup.find_all("img") if thing.get("class")[0] == "FFVAD" and thing.get("src") not in set_of_srcs}


def login_insta():
    driver.get(f"{INSTAGRAM_ROOT_URL}/accounts/login/?source=auth_switcher")

    username = driver.find_element_by_name("username")
    username.send_keys(USER_EMAIL)

    password = driver.find_element_by_name("password")
    password.send_keys(USER_PASSWORD)
    password.submit()

    time.sleep(3)

    if check_exists_by_xpath(driver, "/html/body/div[3]"):
        actions.click()
        actions.send_keys(Keys.TAB * 2)
        actions.send_keys(Keys.ENTER)
        actions.perform()


def gather_images(category, input, maxnum_of_images=None):
    # maxnum_of_images currently unused
    set_of_srcs = set()
    if category == "tag":
        suffix_url = f"/explore/tags/{input}/?hl=en"
    elif category == "user":
        suffix_url = f"/{input}/?hl=en"

    full_url = f"{INSTAGRAM_ROOT_URL}{suffix_url}"
    driver.get(full_url)

    # actions.send_keys(Keys.TAB * 5)
    # actions.send_keys(Keys.ENTER)
    # actions.send_keys(Keys.RIGHT * 10)
    # actions.perform()

    for _ in range(20):
        set_of_srcs |= get_srcs(set_of_srcs)
        print(f"{len(set_of_srcs)} images captured for {category}('{input}')")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)

    return set_of_srcs



if __name__ == "__main__":
    driver, actions = initialize_driver()
    login_insta()
    set_of_srcs = gather_images("tag", "allbirdsshoes", 100)
    print(set_of_srcs, len(set_of_srcs))
