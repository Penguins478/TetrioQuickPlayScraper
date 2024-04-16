# - Does not work if they use captcha
# - May need to re-run the program if it crashes on initial load
# - Firefox only
# - Will probably stop working with future updates
# - Already got the 100+ badge tho :skull:

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

website = 'https://tetr.io'

options = Options()
driver = webdriver.Firefox(options=options)
driver.get(website)

threshold = 100
rapid_update = False
sleep_const = 5
quick_spectate = 2
osk = 'osk'
initial_cooldown = 300
cooldown_osk = initial_cooldown
cooldown_100 = initial_cooldown
enableEmail = False
waiting_osk = False
waiting_100 = False

sender_email = 'email@gmail.com'
receiver_email = 'email@gmail.com'
password = 'password'


def send_email(text):

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'TETRIO QuickPlay Notification'

    body = text
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print('Email notification sent successfully!')


if __name__ == '__main__':

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

            player_containers = driver.find_elements(By.CSS_SELECTOR, '.scroller_player.ns:not(.spectator)')
            usernames = [container.get_attribute('data-username') for container in player_containers]

            if osk in usernames:
                print("@@@@@@@@@@@@     OSK is in the room!     @@@@@@@@@@@@@")
                if enableEmail and not waiting_osk:
                    send_email("@@@@@@@@@@@@     OSK is in the room!     @@@@@@@@@@@@@")
                    waiting_osk = True

            if rapid_update:
                print("Player Count:", playercount)

            if playercount >= threshold:
                print('-------------------------------------')
                print("@@@@@@@@@@@@    GO   @@@@@@@@@@@@@@")
                current_time = datetime.now()
                formatted_time = current_time.strftime("%H:%M:%S")
                print("Current Time:", formatted_time)
                if enableEmail and not waiting_100:
                    send_email("@@@@@@@@@@@@     QuickPlay has 100+ players!     @@@@@@@@@@@@@")
                    waiting_100 = True

            sleep(quick_spectate)

            if enableEmail:
                if waiting_osk:
                    cooldown_osk -= quick_spectate
                    if cooldown_osk == 0:
                        cooldown_osk = initial_cooldown
                        waiting_osk = False

                if waiting_100:
                    cooldown_100 -= quick_spectate
                    if cooldown_100 == 0:
                        cooldown_100 = initial_cooldown
                        waiting_100 = False

    finally:

        driver.quit()


