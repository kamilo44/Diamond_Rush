FROM selenium/standalone-chrome:latest

USER root

# Instala unzip
RUN apt-get update && apt-get install -y unzip curl

# Descarga y descomprime uBlock Origin
RUN mkdir -p /opt/ublock && \
    curl -L -o /tmp/ublock.zip https://github.com/gorhill/uBlock/releases/download/1.64.1b1/uBlock0_1.64.1b1.chromium.zip && \
    unzip /tmp/ublock.zip -d /opt/ublock

ENV CHROME_EXTENSION_PATH=/opt/ublock

# Chrome busca extensiones desde este entorno
ENV CHROME_OPTIONS="--load-extension=$CHROME_EXTENSION_PATH"

USER 1200
