FROM python:3.11
COPY . /app
WORKDIR /app
COPY templates /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["client.py"]
