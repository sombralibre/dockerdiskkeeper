FROM alpine:latest

LABEL maintainer="sombra.libre@gmail.com" version="0.0.1" greeting="give me a dollar."

ADD *.py /
ADD pips.txt /

RUN apk update && \
        apk add python3 && \
        pip3 install -r /pips.txt

CMD ["python3", "/dockerdiskkeeper.py"]
