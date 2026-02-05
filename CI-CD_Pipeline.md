## CI-CD Pipeline

- CI (Continuos Integration) -> Every-time you push code to Github -> it is automatically tested and built
- CD (Continuous Deployment / Delivery) If everything is OK → the app is automatically built as a Docker image and deployed

The goal of this workflow is to:
1. Check your Flask app
2. Build a Docker image
3. Push that image to Docker Hub

Workflow name
```text
name: Flask Todo CI/CD
```

This is just the name of the workflow.
You will see this name in the Actions tab in GitHub.

```text
on: 
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
```

This means:
The workflow runs when:
You push code to the main branch
You create or update a pull request to the main branch

👉 So every important change is automatically checked.

```text
jobs:
  build:
    runs-on: ubuntu-latest
```

jobs → list of tasks to run
build → job name (you can name it anything)
runs-on: ubuntu-latest → GitHub gives a Linux virtual machine

This machine is temporary and created only for this workflow.

Each step runs one by one.

**Step 1: Checkout code**
```text
- name: Checkout code
  uses: actions/checkout@v4
```

This step:
Downloads your GitHub repository
Makes your code available inside the virtual machine
Without this, GitHub Actions cannot see your code.


**Step 2: Set up Python**
```text
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: "3.11"
```

This step:
Installs Python 3.11
Makes Python available for the next steps
Important because Flask is a Python framework.


**Step 3: Install dependencies**
```text
- name: Install dependencies
  run: |
    pip install --upgrade pip
    pip install -r requirements.txt
```

This step:
Updates pip
Installs all Python libraries from requirements.txt

Example:
Flask
SQLAlchemy
Other packages your app needs

**Step 4: Check Flask app**
```text
- name: Run Flask app check
  run: |
    python -m py_compile app.py
```

This step:
Checks if app.py has syntax errors
Does not run the app
Only confirms the code is valid Python
If there is a mistake, the workflow fails here.

**Step 5: Build Docker image**
```text
- name: Build Docker image
  run: |
    docker build -t flask-todo-app .
```

This step:
Uses the Dockerfile
Creates a Docker image named flask-todo-app
So now your Flask app is containerized.

**Step 6: Login to Docker Hub**
```text
- name: Login to Docker Hub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKER_USERNAME }}
    password: ${{ secrets.DOCKER_PASSWORD }}
```

This step:
Logs in to Docker Hub
Uses GitHub Secrets (secure, not visible)

Why secrets?
To protect your Docker Hub username and password

**Step 7: Push Docker image**
```text
- name: Push Docker image
  run: |
    docker tag flask-todo-app ${{ secrets.DOCKER_USERNAME }}/flask-todo-app:latest
    docker push ${{ secrets.DOCKER_USERNAME }}/flask-todo-app:latest
```

This step:
Tags the image with your Docker Hub username
Pushes the image to Docker Hub






