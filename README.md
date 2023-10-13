# Django Restful CRUD API with PostgreSQL example

## Setup application 

### Install packages
Install all the packages, preferably in a virtual environment 

```
pip install -r requirements.txt
```

### Setup Database

create a new database named `vm-app` in your postgres server. 
> NOTE: DB Name is based on [settings.py](./django-rest-vm-app/blob/main/DjangoRestPgSQL/settings.py)! configurations


Create the DB tables first:
```
python manage.py migrate
```

### Setup New Relic Agent

Configure ENV variables for New Relic agent

```
EXPORT NEW_RELIC_APP_NAME=YOUR_APP_NAME
EXPORT NEW_RELIC_LICENSE_KEY=YOUR_INGEST_LICENSE_KEY
```

## Running the Application

Run the development web server with new relic agent:
```
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python manage.py runserver 8080
```
Open the URL http://localhost:8080/ to access the application.