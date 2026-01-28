# import time
# import random
# import pyautogui
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# # --- КОНФИГУРАЦИЯ ЗА ТВОЯ ДИСПЛЕЙ (1920x1080, 144Hz) ---
# SCREEN_WIDTH = 1920
# SCREEN_HEIGHT = 1080
# CHROME_HEADER_OFFSET = 130  # Отместване за лентата на Chrome и Windows
# pyautogui.PAUSE = 0.01  # Оптимизация за 144Hz
# pyautogui.FAILSAFE = True  # Спиране при мишка в ъгъла
#
# # --- ПЪТИЩА ДО ТВОИТЕ ФАЙЛОВЕ НА DESKTOP ---
# FILE_CYRILLIC = r"C:\Users\Aleks\Desktop\bg-names-cyrillic.txt"
# FILE_LATIN = r"C:\Users\Aleks\Desktop\bg-names-latin.txt"
#
# # --- ТВОИТЕ ДАННИ ЗА ВХОД (ПОПЪЛНИ ТУК) ---
# MY_EMAIL = "i82331028@gmail.com"
# MY_PASS = "Djobsi%Aleks%20"
# TARGET_URL = "https://www.facebook.com/ivan.g.ivanov.71/friends_all"
#
#
# def load_names():
#     """Зарежда имената от двата файла на десктопа"""
#     names = set()
#     for path in [FILE_CYRILLIC, FILE_LATIN]:
#         try:
#             with open(path, 'r', encoding='utf-8') as f:
#                 for line in f:
#                     name = line.strip().lower()
#                     if name:
#                         names.add(name)
#             print(f"✅ Успешно заредени имена от: {path}")
#         except Exception as e:
#             print(f"❌ Грешка при четене на {path}: {e}")
#     return names
#
#
# def human_mouse_move(element):
#     """Физическо движение на мишката до бутона с леко треперене за реализъм"""
#     try:
#         # Взимаме позицията на бутона спрямо браузъра
#         location = element.location_once_scrolled_into_view
#         size = element.size
#
#         # Изчисляваме координатите на екрана
#         target_x = location['x'] + (size['width'] / 2)
#         target_y = location['y'] + (size['height'] / 2) + CHROME_HEADER_OFFSET
#
#         # Добавяме лек "шум" (човешко треперене)
#         target_x += random.randint(-4, 4)
#         target_y += random.randint(-4, 4)
#
#         # Движение с плавно намаляване на скоростта (Ease Out)
#         pyautogui.moveTo(target_x, target_y,
#                          duration=random.uniform(0.6, 1.2),
#                          interpolation=pyautogui.easeOutQuad)
#     except Exception as e:
#         print(f"⚠️ Грешка при движение на мишката: {e}")
#
#
# def run_fb_bot():
#     bg_names = load_names()
#     count = 0  # <--- Преместваме го тук най-горе!
#
#     if not bg_names:
#         print("🛑 Списъкът с имена е празен!")
#         return
#
#     print(f"🚀 Стартирам тест за 2 заявки срещу: {TARGET_URL}")
#
#     options = webdriver.ChromeOptions()
#     options.add_argument("--disable-notifications")
#     options.add_argument("--start-maximized")
#     # Добавяме User-Agent, за да изглеждаме като истински браузър
#     options.add_argument(
#         "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
#
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#
#     try:
#         driver.get("https://www.facebook.com")
#
#         # По-сигурно приемане на бисквитки
#         try:
#             time.sleep(4)
#             cookie_btn = driver.find_element(By.XPATH, "//button[contains(., 'Allow all') or contains(., 'Приемане')]")
#             driver.execute_script("arguments[0].click();", cookie_btn)  # Използваме JS клик
#             print("🍪 Бисквитките са затворени чрез JS.")
#         except:
#             pass
#
#         driver.find_element(By.ID, "email").send_keys(MY_EMAIL)
#         driver.find_element(By.ID, "pass").send_keys(MY_PASS)
#
#         # Използваме JavaScript за клик на Login, за да не се влияе от пречещи елементи
#         login_btn = driver.find_element(By.NAME, "login")
#         driver.execute_script("arguments[0].click();", login_btn)
#
#         print("🔑 Логване (JS Click)... Изчаквам зареждане.")
#         time.sleep(12)
#
#         # 2. Навигация към целта
#         driver.get(TARGET_URL)
#         time.sleep(7)
#
#         # 3. Основен цикъл (ТЕСТ ЗА 2 ЗАЯВКИ)
#         count = 0
#         while count < 2:
#             # Намираме "картите" на приятелите
#             friends_cards = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")
#
#             for card in friends_cards:
#                 if count >= 2: break
#
#                 try:
#                     # Извличаме името
#                     full_name = card.find_element(By.CSS_SELECTOR, "span").text.lower()
#                     first_name = full_name.split()[0] if full_name else ""
#
#                     # Проверка в българския списък
#                     if first_name in bg_names:
#                         # Намираме бутона
#                         btn = card.find_element(By.XPATH, ".//div[@role='button']")
#                         btn_text = btn.text
#
#                         if "Add Friend" in btn_text or "Добавяне" in btn_text:
#                             # Центрираме бутона на екрана
#                             driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
#                             time.sleep(2)
#
#                             # Движим мишката и кликваме
#                             human_mouse_move(btn)
#                             time.sleep(random.uniform(0.5, 1.0))
#                             btn.click()
#
#                             count += 1
#                             print(f"✨ [{count}] Успешна покана за: {full_name}")
#
#                             # ДЪЛГА ПАУЗА (имитация на човек, който разглежда)
#                             time.sleep(random.uniform(15, 25))
#
#                             # Проверка за прозорец "Познавате ли този човек?"
#                             if "познавате" in driver.page_source or "know" in driver.page_source:
#                                 try:
#                                     confirm = driver.find_element(By.XPATH,
#                                                                   "//div[@aria-label='Confirm' or @aria-label='Потвърждавам']")
#                                     confirm.click()
#                                     print("   🛡️ Прозорецът за сигурност е затворен.")
#                                 except:
#                                     pass
#
#                         elif "Message" in btn_text or "Съобщение" in btn_text:
#                             print(f"🤝 Пропускам {full_name} (вече сте приятели).")
#                         elif "Cancel" in btn_text or "Отмяна" in btn_text:
#                             print(f"⏩ Пропускам {full_name} (поканата е изпратена).")
#
#                 except Exception:
#                     continue
#
#             # Скролване за още резултати
#             driver.execute_script("window.scrollBy(0, 500);")
#             time.sleep(3)
#
#     except Exception as e:
#         print(f"🛑 Критична грешка: {e}")
#     finally:
#         print(f"🏁 ТЕСТЪТ ПРИКЛЮЧИ. Пратени заявки: {count}")
#         driver.quit()
#
#
# if __name__ == "__main__":
#     run_fb_bot()


# import time
# import random
# import pyautogui
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# # --- НАСТРОЙКИ ЗА ЕКРАНА ---
# CHROME_HEADER_OFFSET = 130  # Отместване за 1080p
# pyautogui.FAILSAFE = True
#
#
# def human_mouse_move(element):
#     try:
#         location = element.location_once_scrolled_into_view
#         size = element.size
#         target_x = location['x'] + (size['width'] / 2)
#         target_y = location['y'] + (size['height'] / 2) + CHROME_HEADER_OFFSET
#
#         # Променено: ползваме 'tween' вместо 'interpolation'
#         pyautogui.moveTo(target_x, target_y,
#                          duration=random.uniform(0.7, 1.3),
#                          tween=pyautogui.easeOutQuad)
#     except Exception as e:
#         print(f"⚠️ Грешка при движение: {e}")
#
#
# def run_fb_bot_no_names():
#     # Свързване към твоя отворен Chrome
#     chrome_options = Options()
#     chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#     driver.maximize_window()
#
#     print(f"🚀 Свързан! Започвам да добавям ВСИЧКИ наред...")
#
#     try:
#         # 3. Основен цикъл (ТЕСТ ЗА 2 ЗАЯВКИ)
#         count = 0
#         while count < 20:
#             # Търсим всички възможни бутони за добавяне на страницата
#             # Този XPATH търси бутони, които съдържат текст "Add Friend" или "Добавяне"
#             all_buttons = driver.find_elements(By.XPATH,
#                                                "//div[@role='button'][contains(., 'Add Friend') or contains(., 'Добавяне')]")
#
#             print(f"👀 Намерени общо {len(all_buttons)} потенциални бутона на екрана.")
#
#             for btn in all_buttons:
#                 if count >= 20: break
#
#                 try:
#                     # Проверяваме дали бутонът е видим
#                     if btn.is_displayed():
#                         # Центрираме бутона
#                         driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
#                         time.sleep(2)
#
#                         # Движим мишката физически
#                         human_mouse_move(btn)
#                         time.sleep(random.uniform(0.5, 1.0))
#
#                         # Клик чрез JavaScript (най-сигурният начин)
#                         driver.execute_script("arguments[0].click();", btn)
#
#                         count += 1
#                         print(f"✨ [{count}] Успешно натиснат бутон!")
#
#                         # Дълга пауза, за да не те блокира Facebook
#                         time.sleep(random.uniform(15, 25))
#                 except Exception as e:
#                     print(f"⚠️ Пропуск на бутон поради: {e}")
#                     continue
#
#             # Ако не е намерил нищо или е минал през всички на екрана - скролва надолу
#             print("📜 Скролвам за още хора...")
#             driver.execute_script("window.scrollBy(0, 800);")
#             time.sleep(4)
#
#     except Exception as e:
#         print(f"🛑 Грешка: {e}")
#     finally:
#         print(f"🏁 ТЕСТЪТ ПРИКЛЮЧИ. Ако всичко е точно, промени лимита на 250.")
#
#
# if __name__ == "__main__":
#     run_fb_bot_no_names()


# import time
# import random
# import pyautogui
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# # --- TURBO НАСТРОЙКИ ---
# CHROME_HEADER_OFFSET = 130
# pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 0.01  # Минимална пауза за PyAutoGUI
#
#
# def human_mouse_move(element):
#     """Светкавично движение на мишката"""
#     try:
#         location = element.location_once_scrolled_into_view
#         size = element.size
#         target_x = location['x'] + (size['width'] / 2)
#         target_y = location['y'] + (size['height'] / 2) + CHROME_HEADER_OFFSET
#
#         # TURBO СКОРОСТ: 0.1 до 0.2 секунди
#         pyautogui.moveTo(target_x, target_y,
#                          duration=random.uniform(0.1, 0.2),
#                          tween=pyautogui.easeOutQuad)
#     except Exception:
#         pass
#
#
# def run_fb_bot_turbo():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#
#     print(f"🏎️ TURBO РЕЖИМ АКТИВИРАН! Цел: 20 покани.")
#
#     count = 0
#     try:
#         while count < 20:
#             # Директно взимаме всички бутони
#             buttons = driver.find_elements(By.XPATH,
#                                            "//div[@role='button'][contains(., 'Add Friend') or contains(., 'Добавяне')]")
#
#             if not buttons:
#                 driver.execute_script("window.scrollBy(0, 1000);")
#                 time.sleep(0.5)
#                 continue
#
#             for btn in buttons:
#                 if count >= 20: break
#
#                 try:
#                     if btn.is_displayed():
#                         # Бързо центриране и клик
#                         driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
#                         time.sleep(0.3)
#
#                         human_mouse_move(btn)
#
#                         # Форсиран JS клик за моментално действие
#                         driver.execute_script("arguments[0].click();", btn)
#
#                         count += 1
#                         print(f"🚀 [{count}/20] ПРАТЕНО!")
#
#                         # ТУРБО ПАУЗА: 3 до 6 секунди
#                         time.sleep(random.uniform(3, 6))
#                 except:
#                     continue
#
#             # Агресивно скролване
#             driver.execute_script("window.scrollBy(0, 1200);")
#             time.sleep(0.5)
#
#     except Exception as e:
#         print(f"🛑 Стоп: {e}")
#     finally:
#         print(f"🏁 ФИНИШ! Изпратени: {count}")
#
#
# if __name__ == "__main__":
#     run_fb_bot_turbo()


# import time
# import random
# import pyautogui
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# # --- HYPER-SPEED CONFIG ---
# CHROME_HEADER_OFFSET = 130
# pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 0.001  # Премахваме лага на самата библиотека
#
#
# def sniper_move(element):
#     """Светкавично прицелване"""
#     try:
#         location = element.location_once_scrolled_into_view
#         size = element.size
#         target_x = location['x'] + (size['width'] / 2)
#         target_y = location['y'] + (size['height'] / 2) + CHROME_HEADER_OFFSET
#
#         # СВРЪХЗВУКОВА СКОРОСТ (0.05 сек е почти мигновено)
#         pyautogui.moveTo(target_x, target_y, duration=0.08)
#     except Exception:
#         pass
#
#
# def run_fb_hyper_speed():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#
#     print(f"🚀 HYPER-SPEED СТАРТ! Дръж се...")
#
#     count = 0
#     try:
#         while count < 150:
#             # Търсим бутоните
#             buttons = driver.find_elements(By.XPATH,
#                                            "//div[@role='button'][contains(., 'Add Friend') or contains(., 'Добавяне')]")
#
#             if not buttons:
#                 driver.execute_script("window.scrollBy(0, 1200);")
#                 time.sleep(0.3)
#                 continue
#
#             for btn in buttons:
#                 if count >= 150: break
#
#                 try:
#                     # Светкавичен скрол и движение
#                     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
#
#                     sniper_move(btn)
#
#                     # Клик
#                     driver.execute_script("arguments[0].click();", btn)
#
#                     count += 1
#                     print(f"💥 [{count}/20] ИЗСТРЕЛЯНА!")
#
#                     # РИСКОВА ПАУЗА (1.5 до 3 сек)
#                     time.sleep(random.uniform(1.5, 3.0))
#
#                 except:
#                     continue
#
#             # Агресивен скрол за следващата доза
#             driver.execute_script("window.scrollBy(0, 1500);")
#             time.sleep(0.4)
#
#     except Exception as e:
#         print(f"🛑 Error: {e}")
#     finally:
#         print(f"🏁 ФИНИШ! Победи собствения си рекорд.")
#
#
# if __name__ == "__main__":
#     run_fb_hyper_speed()


import time
import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --- Configuration ---
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
                    time.sleep(1)  # Изчакваме прозореца да се появи
                    warnings = driver.find_elements(By.XPATH,
                                                    "//span[contains(., 'OK') or contains(., 'ОК') or contains(., 'Confirm') or contains(., 'Потвърждавам')]")

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