FROM python:3.10-slim

WORKDIR /app

RUN apt update && apt install -y netcat-openbsd

RUN apt-get update && apt-get install -y \
    iputils-ping \
    curl \
    netcat-openbsd \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install selenium

COPY . .

RUN chmod -R 755 /app/ublock

# CMD ["python", "script.py"]
CMD ["tail", "-f", "/dev/null"]
