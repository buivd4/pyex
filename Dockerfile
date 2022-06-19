FROM python:3.9-slim-buster

WORKDIR /app
COPY . .
RUN pip install .
EXPOSE 5000
CMD ["pyex", "--host", "0.0.0.0", "--port", "5000", "-s"]