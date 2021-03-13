import os
import sys
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def accept_cookie_consent(my_driver):
    try:
        WebDriverWait(my_driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, "//button[text()='Ausgewählte akzeptieren']")))
        button = my_driver.find_element_by_xpath("//button[text()='Ausgewählte akzeptieren']")
        button.click()
    except NoSuchElementException:
        return my_driver
    except TimeoutException:
        return my_driver


def click_jessica(my_driver):
    try:
        WebDriverWait(my_driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "iframe[id^='typeform-full'")))
        iframe = my_driver.find_element_by_css_selector("iframe[id^='typeform-full'")
        my_driver.switch_to.frame(iframe)
        WebDriverWait(my_driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, "//div[text()='Jessica Steiger']")))
        div_jessica = my_driver.find_element_by_xpath("//div[text()='Jessica Steiger']")
        div_jessica.click()

        return my_driver

    except NoSuchElementException:
        return my_driver
    except TimeoutException:
        return my_driver


def click_nein(my_driver):
    try:
        WebDriverWait(my_driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[text()='Nein']")))

        div_nein = my_driver.find_element_by_xpath("//div[text()='Nein']")
        div_nein.click()

        return my_driver

    except NoSuchElementException:
        return my_driver
    except TimeoutException:
        return my_driver


def click_weiter(my_driver):
    buttons = my_driver.find_elements_by_xpath("//button[normalize-space()='Weiter']")
    for button in buttons:
        try:
            button.click()
        except:
            continue

    return my_driver


def make_screenshot(my_driver, file_name: str):
    time.sleep(1)
    my_driver.save_screenshot(file_name)
    return my_driver


def main():
    tries = 2
    if len(sys.argv) > 1:
        tries = int(sys.argv[1])

    options = Options()
    options.headless = True
    profile = webdriver.FirefoxProfile()
    profile.set_preference('intl.accept_languages', 'en-US, en')

    counter = 0

    session_time = str(time.time())

    driver = webdriver.Firefox(options=options, firefox_profile=profile)

    screenshot_dir = "screenshots"

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
        os.chmod(screenshot_dir, 0o777)

    while counter < tries:
        driver.get('https://www.toyota-crowd.de/projekt-des-jahres/abstimmung')
        accept_cookie_consent(driver)
        iframe_driver = click_jessica(driver)
        iframe_driver = click_nein(iframe_driver)
        iframe_driver = click_weiter(iframe_driver)

        file_name = "./screenshots/" + session_time + "_vote_" + str(counter) + ".png"
        make_screenshot(iframe_driver, file_name)

        print('Vote: ' + str(counter))

        counter += 1

    for file in os.listdir(screenshot_dir):
        os.chmod(os.path.join(screenshot_dir, file), 0o777)

    driver.quit()


if __name__ == "__main__":
    main()
