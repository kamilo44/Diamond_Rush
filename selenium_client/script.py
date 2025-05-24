from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

options = Options()
# options.add_argument("--window-size=1280,720")
# options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--load-extension=/app/ublock")

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
    elemento = WebDriverWait(driver, seconds).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    print("Elemento encontrado.")
except Exception as e:
    print("No se encontró el elemento:", e)

try:
    time.sleep(5)
    elemento.screenshot("./capturas/captura_elemento.png")
    print("Pantallazo guardado.")
except Exception as e:
    print("No se realizó correctamente el pantallazo:", e)

time.sleep(5)
driver.quit()