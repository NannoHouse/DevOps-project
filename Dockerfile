FROM alpine

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN apk add py3-pip

COPY /src/app.py /usr/
COPY /src/app_test.py /usr/
COPY /src/requirements.txt /usr/
RUN pip3 install -r /usr/requirements.txt --break-system-packages

EXPOSE 5000

CMD ["python3", "/usr/app.py"]