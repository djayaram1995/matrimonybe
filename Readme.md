## Go to venv
.\.venv\Scripts\activate
## Start Application
django-admin startapp SubscriberManagement
## Make migration
python manage.py makemigrations
python manage.py migrate
## Run server
python manage.py runserver