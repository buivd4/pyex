FROM python:3.9-slim-buster

WORKDIR /app
COPY . .
RUN pip install .
EXPOSE 5000
CMD ["pyex", "-s"]