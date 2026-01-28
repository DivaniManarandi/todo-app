# Docker and Docker Compose

Docker is a platform for **containerization**. It packages an application together with everything it needs — **code, runtime, system libraries, and configuration** — into a single unit called a container.

This ensures the app runs the same way everywhere.

---

## Key Concepts

* **Container**: A lightweight, isolated environment that runs an application.
* **Image**: A blueprint (template) used to create containers.
* **Dockerfile**: A set of instructions to build a Docker image.
* **Docker Engine**: The software that builds images and runs containers.

---

## Docker Compose

**Docker Compose** is a tool for running **multiple containers together**.

Most real-world applications are not just one service — they usually consist of several components that need to work together.

---

## Simple Analogy (Food 🍽️)

* **Image** → Recipe
* **Container** → Cooked meal
* **Docker** → Kitchen that cooks and runs a single dish
* **Docker Compose** → Planning and serving an entire meal

---

## Simple Explanation

* **Docker**: "Put my app in a box so it runs the same on any computer."
* **Docker Compose**: "Describe my whole application stack and run it all together."

---

## When Should You Use Each?

### Use Docker if:

* You have a single service
* You are learning containers

### Use Docker Compose if:

* You have multiple services
* You want an easy local development setup

---

## Example Application Stack

A real-world application often includes:

* Web application
* Database
* Cache (Redis)
* Background worker

Docker Compose lets you define and start all of these services with a single command.

---

## Why Flask Here?

Flask is doing **two jobs**:

* API server
* UI server

Flask is a **micro web framework for Python**, making it lightweight, flexible, and easy to integrate into containerized applications.

---

## Summary

* Docker packages applications into containers
* Images are blueprints, containers are running instances
* Docker Compose manages multiple containers together
* Flask is commonly used as both API and UI server in small to medium applications

MY to-do app UI

![final outcome](https://github.com/user-attachments/assets/6e03f0d9-5ae7-4131-a36c-a5718942a36c)


find your documentation here;

[DEPLOY A CONTAINERISED APP USING DOCKER AND DOCKER COMPOSE.pdf](https://github.com/user-attachments/files/24900420/DEPLOY.A.CONTAINERISED.APP.USING.DOCKER.AND.DOCKER.COMPOSE.pdf)

Next improvements;
add SQLite database


