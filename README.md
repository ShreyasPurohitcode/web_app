# Web App - Exploring CI/CD and DevOps Basics

This project is a simple web application that I've used to learn and practice some foundational DevOps concepts. The focus here is on containerizing the app with Docker, managing the code with GitHub, and automating the build and deployment process using GitHub Actions.

## Overview

The "web_app" project helped me get hands-on experience with containerization, version control, and CI/CD pipelines. The goal was to create a basic application that could be consistently deployed across different environments with minimal manual intervention.

## Technologies Used

- **Python** and **Flask**: For the web application itself.
- **Docker**: To containerize the application.
- **GitHub**: For version control.
- **GitHub Actions**: To automate the CI/CD pipeline.

## DevOps Workflow

### Dockerization

I created a Dockerfile to containerize the app, making it easier to deploy and run anywhere. Here's what the Dockerfile looks like:

```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
```

To build and run the Docker container:

```bash
docker build -t web_app .
docker run -p 5000:5000 web_app
```

### Version Control

The project is version-controlled with Git and hosted on GitHub. You can clone the repo using:

```bash
git clone https://github.com/ShreyasPurohitcode/web_app.git
cd web_app
```

### CI/CD Pipeline

I set up a basic CI/CD pipeline with GitHub Actions that builds the Docker image and pushes it to DockerHub whenever I push changes to the `main` branch. Here's a snippet of the workflow:

```yaml
name: Docker Image CI

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Login to DockerHub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Build and push
      uses: docker/build-push-action@v2
      with:
        push: true
        tags: shreyasp13/web_app:latest
```

## Conclusion

This project was a great way for me to get familiar with some essential DevOps tools and processes. While it's a simple app, the focus was really on learning how to automate and streamline the deployment process using Docker and GitHub Actions.