FROM python:3.8-alpine
COPY ./requirements.txt ./requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir /app
WORKDIR /app
COPY ./main.py /app/
COPY ./test.py /app/
RUN adduser -D flask
USER flask
EXPOSE 48080
CMD ["python", "main.py"]