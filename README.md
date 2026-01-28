Create a folder in This PC > Disk C: called selenium_profile.

------------------------------------------------------------------------------------------------------------------------------------------
Second: Press Win + R, type the following, and hit Enter: chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenium_profile"

------------------------------------------------------------------------------------------------------------------------------------------
Third, sign in to your Facebook account and go to the profile whose friends you want to add!

------------------------------------------------------------------------------------------------------------------------------------------
Fourth: Paste and run the code in PyCharm (need to install all this libraries!). REMEMBER: ALL YOU DO IS AT YOUR OWN RISK!

------------------------------------------------------------------------------------------------------------------------------------------
Final checklist before the start:

1.Chrome is completely closed before running the command in Win+R.

2.The screen scale (Zoom) in Chrome is at 100%.

3.The PyCharm console is open to monitor the counter [count/150].

------------------------------------------------------------------------------------------------------------------------------------------

import time
import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Configuration
TARGET_LIMIT = 150
CHROME_HEADER_OFFSET = 130
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.001


def sniper_move(element):
    try:
        location = element.location_once_scrolled_into_view
        size = element.size
        target_x = location['x'] + (size['width'] / 2)
        target_y = location['y'] + (size['height'] / 2) + CHROME_HEADER_OFFSET
        pyautogui.moveTo(target_x, target_y, duration=0.07)
    except Exception:
        pass


def run_fb_marathon():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    print(f"Target: {TARGET_LIMIT} invites. Start...")

    count = 0
    try:
        while count < TARGET_LIMIT:
            buttons = driver.find_elements(By.XPATH,
                                           "//div[@role='button'][contains(., 'Add Friend') or contains(., 'Добавяне')]")

            if not buttons:
                driver.execute_script("window.scrollBy(0, 1000);")
                time.sleep(1)
                continue

            for btn in buttons:
                if count >= TARGET_LIMIT: break

                try:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                    time.sleep(0.2)

                    sniper_move(btn)
                    driver.execute_script("arguments[0].click();", btn)

                    count += 1
                    print(f"[{count}/{TARGET_LIMIT}] Ready!")

                    # --- CHECK FOR "YOU DON'T KNOW THIS PERSON" ERROR ---
                    time.sleep(1)
                    warnings = driver.find_elements(By.XPATH,
                                                    "//span[contains(., 'OK') or contains(., 'ОК') or contains(., 'Confirm') or 								contains(., 'Потвърждавам')]")

                    if warnings:
                        driver.execute_script("arguments[0].click();", warnings[0])
                        print(
                            "⚠️'You don't know this person' window detected")
                        time.sleep(2)
                        continue

                    if count % 20 == 0:
                        print("Rest 10-20 seconds for safety...")
                        time.sleep(random.uniform(10, 20))
                    else:
                        # Quick pause between clicks
                        time.sleep(random.uniform(1.5, 2.5))

                except:
                    continue

            driver.execute_script("window.scrollBy(0, 1500);")
            time.sleep(0.5)

    except Exception as e:
        print(f"Stopped for: {e}")
    finally:
        print(f"Total send: {count}")
        # Sound on completion (if Windows supports it)
        import winsound
        winsound.Beep(1000, 500)


if __name__ == "__main__":
    run_fb_marathon()

------------------------------------------------------------------------------------------------------------------------------------------
What to do if Facebook freezes you?
If, despite the breaks, the "You don't know this person" window starts to appear on every click:

1.Stop the script manually.

2.Wait at least 2 hours before running it again.

3.Change random.uniform(1.5, 2.5) to something slower, for example (5.0, 8.0).

------------------------------------------------------------------------------------------------------------------------------------------

If this profile is important to you, always start with smaller amounts (e.g. 200-300 per day) and gradually increase so as not to "stress" the system.

------------------------------------------------------------------------------------------------------------------------------------------
IMPORTANT DISCLAIMER
This script is for educational purposes only. Using automation tools on Facebook can lead to account restrictions or permanent bans. Use this software at your own risk. The author is not responsible for any consequences resulting from the use of this code.
