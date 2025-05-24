from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--window-size=1280,720")
# options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get("https://www.minijuegos.com/juego/diamond-rush")
driver.execute_script("document.body.style.zoom='80%'")

try:
    boton = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Jugar')]"))
    )
    boton.click()
    print("Botón clickeado.")
except Exception as e:
    print("No se encontró el botón:", e)

time.sleep(5)
driver.save_screenshot("capturas/pantallazo.png")
print("Pantallazo guardado.")
# driver.quit()
