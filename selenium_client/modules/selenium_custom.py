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

class DiamondRushSelenium:
    def __init__(self):
        self.driver = None
        pass

    def click_button(self, xpath):
        try:
            timeout = 30
            boton = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            boton.click()
            # print("Botón clickeado.")
            return True
        except Exception as e:
            print("No se encontró el botón:", e)
            return False

    def switch_to_default_content(self):
        try:
            self.driver.switch_to.default_content()
            # print("Se cambió al contenido por defecto.")
        except Exception as e:
            print("No se pudo cambiar al contenido por defecto:", e)
            return False

    def switch_to_canva(self,):
        try:
            xpath = '//*[@id="game-player"]'
            timeout = 30
            iframe1 = WebDriverWait(self.driver, timeout).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, xpath))
            )
            # print("Se cambio a primer iframe.")
        except Exception as e:
            print("No se encontró el primer iframe:", e)
            return False

        try:
            xpath = '/html/body/div[1]/iframe'
            timeout = 30
            iframe2 = WebDriverWait(self.driver, timeout).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, xpath))
            )
            # print("Se cambio a segundo iframe.")
        except Exception as e:
            print("No se encontró el segundo iframe:", e)
            return False

        try:
            tag = "canvas"
            timeout = 30
            canvas = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, tag))
            )
            time.sleep(1)

            canvas = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//canvas[@width="640" and @height="960"]')
                )
            )
            time.sleep(0.5)
            # print("Se cambio a canvas correctamente.")
            return canvas
        except Exception as e:
            print("No se encontró canvas:", e)
            return False

    def close_driver(self):
        try:
            self.driver.quit()
            print("Driver cerrado correctamente.")
        except Exception as e:
            print("Error al cerrar el driver:", e)

    def start_driver(self):
        try:
            options = Options()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            self.driver = webdriver.Remote(
                command_executor='http://selenium-chrome:4444/wd/hub',
                # command_executor='http://localhost:4444/wd/hub',
                options=options
            )
            self.driver.maximize_window()

            # Ir a la página
            self.driver.get("https://www.minijuegos.com/juego/diamond-rush")
            
            #Maximizar la ventana
            self.driver.execute_script("document.body.style.zoom='100%'")

            # Esperar a que la página esté completamente cargada
            # WebDriverWait(self.driver, 30).until(
            #     lambda d: d.execute_script("return document.readyState") == "complete"
            # )

            # Da clic en el botón de "Juega ahora"
            xpath = '//*[@id="clickToPlayButton"]/div/div[3]'
            self.click_button(xpath)

            # Valida que el iframe y canvas se carguen correctamente
            canva = self.switch_to_canva()
            self.switch_to_default_content()

            print("✅ Página completamente cargada.")
            return True
        except Exception as e:
            print("Error al iniciar el driver:", e)
            self.close_driver()
            return False


    def move_arrow_to(self, arrow):
        '''
        U = "Up"
        D = "Down"
        L = "Left"
        R = "Right"
        '''
        try:
            xpath = '//*[@id="game-player"]'
            timeout = 30
            elemento = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.XPATH, xpath))
                )
            actions = ActionChains(self.driver)
            actions.move_to_element(elemento).click().perform()

            if arrow == "R":
                actions.send_keys(Keys.ARROW_RIGHT).perform()
            elif arrow == "L":
                actions.send_keys(Keys.ARROW_LEFT).perform()
            elif arrow == "U":
                actions.send_keys(Keys.ARROW_UP).perform()
            elif arrow == "D":
                actions.send_keys(Keys.ARROW_DOWN).perform()
            else:
                print("Flecha no válida.")
                return False
            time.sleep(0.5)
            print("Flecha movida:", arrow)
            return True
        except Exception as e:
            print("No se movió correctamnete con las flechas:", e)
            return False
        
    def take_screenshot(self,):
        try:
            canvas = self.switch_to_canva()
            path = './capturas/pantallazo.png'
            canvas.screenshot(path)
            time.sleep(0.5)
            self.switch_to_default_content()
            print("Pantallazo guardado.")
            return True
        except Exception as e:
            print("No se realizó correctamente el pantallazo:", e)
            return False
