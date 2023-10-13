# Django Restful CRUD API with PostgreSQL example

## Setup application 
Install all the packages, preferably in a virtual environment 

```
pip install -r requirements.txt
```

## Running the Application

Create the DB tables first:
```
python manage.py migrate
```
Run the development web server:
```
python manage.py runserver 8080
```
Open the URL http://localhost:8080/ to access the application.