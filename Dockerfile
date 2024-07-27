FROM python:3.12.0-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install --no-cache-dir -r requirements.lock

