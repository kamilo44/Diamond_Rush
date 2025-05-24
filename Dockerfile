FROM python:3.10-slim

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg2 ca-certificates fonts-liberation libnss3 \
    libxss1 libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libgtk-3-0 libgbm-dev chromium chromium-driver && \
    rm -rf /var/lib/apt/lists/*

# Verifica que chromium-driver y chromium-browser estén instalados
RUN which chromium && which chromedriver

# Instala selenium
RUN pip install selenium

# Establecer directorio de trabajo
WORKDIR /usr/src/app

# Copiar scripts
COPY scripts /usr/src/app
