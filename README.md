# Django REST API template

## Python version
\>= 3.10

## Local
### Installation
#### Django app
1. Create venv
```bash
python3.10 -m venv .venv
```

2. Activate venv
```bash
source .venv/bin/activate
```

3. Install requirements
```bash
pip install -r django_core/requirements/local.txt
```

Run ``pip freeze`` after project's first requirements installation to pin requirements' versions.

4. Copy .env
```bash
cp django_core/django_core/local.example.env django_core/django_core/.env
```

#### Docker and Docker compose
Refer to:

https://docs.docker.com/engine/install/

### Deploy

Use the script to start PSQL in Docker Compose, apply migrations and run development server:
```bash
make local
```

## Swagger Docs
Go to http://127.0.0.1:8000/api/docs after running server

## Development

During development, use Black formatter, Pylint and Flake8.

## Prod

### Installation
Copy .env:
```bash
cp django_core/django_core/production.example.env django_core/django_core/.env
```

### Deploy
Use shortcut script:
```bash
make up
```
