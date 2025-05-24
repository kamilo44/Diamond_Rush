from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del navegador
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1280,720")
options.binary_location = "/usr/bin/chromium"

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# Abre la página
driver.get("https://www.minijuegos.com/juego/diamond-rush")


driver.execute_script("document.body.style.zoom='50%'")

try:
    seconds = 15
    wait = WebDriverWait(driver, seconds)
    xpath = "/html/body/div[6]/section[1]/div/div/div[2]/div/div[3]/button/div/div[4]/span"
    boton = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    boton.click()
    print("Botón clickeado.")
except Exception as e:
    print("No se pudo hacer clic en el botón:", str(e))

time.sleep(3)
driver.save_screenshot("capturas/pantallazo_post_click.png")
print("Pantallazo guardado.")
# driver.quit()
