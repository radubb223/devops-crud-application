# CRUD Flask App

Simple CRUD web application built with Flask and MySQL.

## Technologies

* Python / Flask
* MySQL
* Docker
* Docker Compose

## Run locally

Clone the repository and start the containers:

```bash
git clone https://github.com/radubb223/devops-crud-application.git
cd devops-crud-application
docker compose up --build
```

The application will be available at:

```text
http://localhost:5000
```

## Project structure

* `app.py` — Flask application
* `Dockerfile` — application container
* `compose.yaml` — Flask + MySQL services
* `requirements.txt` — Python dependencies

## Purpose

This project was built to practice containerization, Docker Compose, environment configuration and basic application deployment workflows.
