import cv2
import matplotlib.pyplot as plt
import os
import pprint

# Función para comparar dos imágenes
def comparar_imagenes(imagen1, imagen2):
    # Redimensionar imagen2 si es más grande
    if imagen2.shape[0] > imagen1.shape[0] or imagen2.shape[1] > imagen1.shape[1]:
        imagen2 = cv2.resize(imagen2, (min(imagen1.shape[1], imagen2.shape[1]), min(imagen1.shape[0], imagen2.shape[0])))

    # === Comparación de forma (template matching en escala de grises) ===
    gray1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)
    resultado = cv2.matchTemplate(gray1, gray2, cv2.TM_CCOEFF_NORMED)
    _, max_val_forma, _, _ = cv2.minMaxLoc(resultado)

    # === Comparación de color (histograma HSV) ===
    hsv1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2HSV)

    # Calcular histogramas (solo Hue y Saturación)
    hist1 = cv2.calcHist([hsv1], [0, 1], None, [180, 256], [0, 180, 0, 256])
    hist2 = cv2.calcHist([hsv2], [0, 1], None, [180, 256], [0, 180, 0, 256])

    # Normalizar
    cv2.normalize(hist1, hist1, 0, 1, cv2.NORM_MINMAX)
    cv2.normalize(hist2, hist2, 0, 1, cv2.NORM_MINMAX)

    # Comparar histogramas (1.0 es idéntico)
    similitud_color = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    # === Combinación de ambas métricas ===
    # Ambas van de 0 (peor) a 1 (mejor). Normalizamos la métrica de color si se sale de ese rango
    similitud_color = max(0, min(similitud_color, 1))  # Clamp

    # Ponderación (puedes ajustar los pesos)
    peso_forma = 0.5
    peso_color = 0.5
    similitud_total = (peso_forma * max_val_forma) + (peso_color * similitud_color)

    return similitud_total


def crear_matriz(path_screenshot, path_images):
    img = cv2.imread(path_screenshot)

    img_rgb= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    # Carga las imágenes de referencia
    carpeta_referencia = path_images
    imagenes_referencia = []

    for archivo in os.listdir(carpeta_referencia):
        imagen = cv2.imread(os.path.join(carpeta_referencia, archivo))
        imagenes_referencia.append((imagen,archivo))


    # Carga la imagen recibida
    #Crear un Ciclo for que cargue todas las imagenes recibidas

    lectura_de_datos=[]

    #Leer cada una de las celdas que se entregan de imagen del nivel
    for k in range(13):
        fila=[]
        for i in range(10):
            imagen = img_rgb[128+64*k:64*k+192, 64*i:64*i+64]
            fila.append(imagen)
        lectura_de_datos.append(fila)

    matriz_juego=[]

    for k in range(13):
        fila=[]
        for i in range(10):

            # Compara la imagen recibida con cada imagen de referencia
            mejor_coincidencia = None
            mejor_similitud = 0

            imagen_recibida=lectura_de_datos[k][i]

            for imagen_referencia, nombre_archivo in imagenes_referencia:
                similitud = comparar_imagenes(imagen_recibida, imagen_referencia)
                if similitud > mejor_similitud:
                    flag=nombre_archivo
                    mejor_similitud = similitud
                    mejor_coincidencia = imagen_referencia

            # Muestra la mejor coincidencia
            if mejor_coincidencia is not None:

                if "muro" in flag:
                    fila.append(1)
                elif "piso" in flag:
                    fila.append(2)
                elif "salidos" in flag:
                    fila.append(3)
                elif "diamante" in flag:
                    fila.append(4)
                elif "indiana" in flag:
                    fila.append(0)
                elif "pinchos" in flag:
                    fila.append(5)
                elif "lava" in flag:
                    fila.append(6)
                elif "roca" in flag:
                    fila.append(7)
                elif "reliquia" in flag:
                    fila.append(8)
                elif "puerta_llave.png" == flag:
                    fila.append(11)
                elif "llave (1).png" == flag:
                    fila.append(9)
                elif "salida" in flag:
                    fila.append(10)
                elif "hueco" in flag:
                    fila.append(12)
                elif "piedra" in flag:
                    fila.append(13)
                elif "reja" in flag:
                    fila.append(14)
                elif "boton" in flag:
                    fila.append(15)
                else:fila.append(flag)

            else:
                print("No se encontró una coincidencia")

        matriz_juego.append(fila)

    return matriz_juego

def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:4} ", end="  ")  # Imprime cada elemento con un ancho de 4 caracteres
        print()