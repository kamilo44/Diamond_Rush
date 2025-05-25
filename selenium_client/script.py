from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote(
    command_executor='http://selenium-chrome:4444/wd/hub',
    options=options
)

driver.maximize_window()

driver.get("https://www.minijuegos.com/juego/diamond-rush")

driver.execute_script("document.body.style.zoom='100%'")

try:
    xpath = '//*[@id="clickToPlayButton"]/div/div[3]'
    seconds = 30
    boton = WebDriverWait(driver, seconds).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    boton.click()
    print("Botón clickeado.")

except Exception as e:
    print("No se encontró el botón:", e)

try:
    xpath = '//*[@id="game-player"]'
    seconds = 30
    iframe1 = WebDriverWait(driver, seconds).until(
        EC.frame_to_be_available_and_switch_to_it((By.XPATH, xpath))
    )
    print("Elemento cambio a primer iframe.")
except Exception as e:
    print("No se encontró el elemento:", e)

try:
    xpath = '/html/body/div[1]/iframe'

    iframe2 = WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it((By.XPATH, xpath))
    )
    print("Elemento cambio a segundo iframe.")
except Exception as e:
    print("No se encontró el elemento:", e)

try:
    canvas = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "canvas"))
    )
    time.sleep(1)
    canvas.screenshot("./capturas/canvas.png")
    time.sleep(0.5)
    driver.switch_to.default_content()
    print("Pantallazo guardado.")
except Exception as e:
    print("No se realizó correctamente el pantallazo:", e)

try:
    xpath = '//*[@id="game-player"]'

    elemento = WebDriverWait(driver, seconds).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

    actions = ActionChains(driver)
    actions.move_to_element(elemento).click().perform()
    for i in range(5):
        actions.send_keys(Keys.ARROW_RIGHT).perform()
        time.sleep(0.5)
    print("Flecha derecha presionada.")
except Exception as e:
    print("No se movió correctamnete con las flechas:", e)

time.sleep(5)
driver.quit()