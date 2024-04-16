# - Does not work if they use captcha
# - Add a ping/notification feature
# - Firefox only
# - Will probably stop working with future updates
# - Already got the 100+ badge tho :skull:

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime

website = 'https://tetr.io'

options = Options()
driver = webdriver.Firefox(options=options)
driver.get(website)

threshold = 100
rapid_update = False
sleep_const = 5
quick_spectate = 1

try:

    html_content = driver.page_source

    # print(html_content)

    join_button = driver.find_element(By.CSS_SELECTOR, '#entry_button.oob_button_full.ns')
    join_button.click()

    sleep(sleep_const)

    multiplayer_button = driver.find_element(By.CSS_SELECTOR, '#play_multi')
    multiplayer_button.click()

    sleep(sleep_const)

    quickplay_button = driver.find_element(By.CSS_SELECTOR, '#multi_quickplay')
    quickplay_button.click()

    sleep(quick_spectate)

    switch_button = driver.find_element(By.ID, 'swb_addendum')
    switch_button.click()

    sleep(sleep_const)

    while True:
        playercount_element = driver.find_element(By.ID, 'playercount')
        playercount_text = playercount_element.text
        playercount = int(playercount_text)

        if rapid_update:
            print("Player Count:", playercount)

        if playercount >= threshold:
            print('-------------------------------------')
            print("@@@@@@@@@@@@    GO   @@@@@@@@@@@@@@@@")
            current_time = datetime.now()
            formatted_time = current_time.strftime("%H:%M:%S")
            print("Current Time:", formatted_time)

finally:

    driver.quit()

