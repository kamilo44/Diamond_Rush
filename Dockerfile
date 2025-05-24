FROM selenium/standalone-chrome:latest

USER root
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install selenium

WORKDIR /usr/src/app
COPY scripts ./scripts
# COPY capturas ./capturas

CMD ["/bin/bash"]
