FROM python:3 As build
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN CFLAGS="-Wno-error=implicit-function-declaration" pip install --no-cache-dir -r requirements.txt
COPY . .
RUN ls -la
RUN pwd
EXPOSE 8000 80