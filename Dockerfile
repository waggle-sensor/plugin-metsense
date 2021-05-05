FROM python:3.8-alpine

RUN apk add --no-cache i2c-tools

# we pull in gcc and linux headers just long enough to compile a couple
# python packages
COPY requirements.txt .
RUN apk add --no-cache gcc musl-dev && \
    CFLAGS="-fcommon" pip3 install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev

COPY . .

ENTRYPOINT ["python3" , "main.py"]
