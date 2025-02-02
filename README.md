# MuseumPlanner backend and frontend (SPA)

**Important notes:**

- although in theory the project works on Windows, this is not officially supported and to do on your
own time and at your own risk. Make it happen only if you are very experienced with the ins and outs of running a python
server on windows.
- the readme here is a general guide on how to set things up, but because there are too many different possible setups
  (with/without docker; on Mac, locally on Linux, on a Linux remote server, etc), not all possible use-cases have been
  covered, and as such it is unlikely to work out of the box.
- If you're unsure what setup to use, you can go with the following rule of thumb: if you'll work on it, then run it
  natively. Otherwise run it in docker.

### External links

It is strongly recommended to read the following documentation before starting to work on the project:

##### Backend:

- [Django](https://www.djangoproject.com/) as the base backend framework and ORM
- [Django REST Framework](https://www.django-rest-framework.org/) for all REST-related stuff

##### Frontend

- Typescript
- [Vue.js](https://vuejs.org/) and [Vuetify](https://vuetifyjs.com/en/) for the rendering
- [Pinia](https://pinia.vuejs.org/) for state management
- [Vitest](https://vitest.dev/) for the tests

It is also expected that you are familiar with the following concepts:

- your operating system's command line interface and package manager
- [Environment variables](https://en.wikipedia.org/wiki/Environment_variable)
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)

### Install the executables

- Python 3.12
- Node v20
- Docker and docker-compose (they generally come together)

### Configure your environment!

Copy the `.env.example` into `.env` and complete it with custom values.

You'll need to [get an API key](https://docs.google.com/forms/d/e/1FAIpQLSfkmEBqH76HLMMiCC-GPPnhcvHC9aJS86E32dOd0Z8MpY2rvQ/viewform) for the Harvard Arts Museum


### Run the app in Docker

Firstly, create the Docker network: `docker network create museumplanner`. This
allows to communicate with other microservices on your computer.

Then you need to run `docker-compose up -d` from the root of the repo. This will start the services.
Last, you'll need to run the migrations and create a first user:

```shell script
docker-compose exec --rm mp-backend python manage.py migrate
```

Django is then available on http://localhost:8000.

Then you have to run your Python commands in the `mp-backend` service,
e.g. to open a shell:
`docker-compose exec mp-backend python manage.py shell_plus`

Whenever you change `requirements.txt` or `requirements-dev.txt`, run `docker-compose build` to rebuild the Django
image.

Launch the unit tests like so:
`docker-compose exec mp-backend python manage.py runserver`

### Run the app without Docker

If you don't want to use the Docker environment, you can follow these steps (adapt to your OS):

```
cd backend
# Numpy require some libs to be installed
sudo apt-get install python3-dev \
     build-essential libssl-dev libffi-dev \
     libxml2-dev libxslt1-dev zlib1g-dev \
     python3-pip
python -m venv venv
source venv/bin/activate # Unix
venv/Scripts/activate # Windows
pip install --upgrade pip
pip install -r requirements-dev.txt

python manage.py migrate
python manage.py runserver
```

You should now be able to:

- see the available commands using `python manage.py help` (we recommend you take a moment to look at them)
- access [the APIs](http://localhost:8000/api/)

For the frontend:

```
cd frontend
pnpm install
pnpm dev
```

With this you should be able to head over to http://localhost:5173/ and enjoy MuseumPlanner 🍾🍾🍾

### Run the tests

The backend tests use `python manage.py test` to run the tests.

The frontend tests use `pnpm test:unit` to run the tests.

### VSCode example config

```
# .vscode/settings.json
{
    "python.linting.pylintEnabled": true,
    "python.linting.pylintArgs": [
        "--load-plugins",
        "pylint_django",
        "--rcfile",
        "/path/to/django-app/.pylintrc"
    ],
    "python.pythonPath": "/path/to/python",
    "python.linting.enabled": true,
    "[python]": {
        "editor.formatOnSave": true,
        "editor.formatOnPaste": true,
    },
    "editor.codeActionsOnSave": {
        "source.fixAll": true
    },
}
```

### Python Style Guide

The code you write must be formatted using [Black](black.readthedocs.io/en/stable/). You can install it
using `pip install black`. You can then run it using `black . --line-length 120` in the root of the project.
The `--line-length 120` option is mandatory.
