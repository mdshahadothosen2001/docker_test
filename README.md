# docker_test
simple docker deploying test project..


This repo is used for Docker test and friendly with docker.

Tech stack: Django, Docker.


## Local development installation
1. At first pull the repository.


2. Create a virtual environment then activate it.

```bash
py -m venv venv
```
```bash
venv/Scripts/activate.bate
```

3. Install the required packages.

```bash
pip install -r backend/requirements/development.txt
```


4. Run docker containers:

```bash
docker-compose up --build
```

click here [URL](http://localhost:8020/admin)  for check this project working or not
If you see login page then it is working.
