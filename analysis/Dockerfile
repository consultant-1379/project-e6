FROM python:3.10.12-slim-bullseye
COPY /raw_data /app/raw_data
COPY requirements.txt /app
COPY functions.py /app
COPY app.py /app
# COPY . /app
WORKDIR /app
RUN pip install --upgrade cython
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]