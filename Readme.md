## Go to venv
.\.venv\Scripts\activate
## Start Application
django-admin startapp SubscriberManagement
## Make migration
python manage.py makemigrations
python manage.py migrate
## Run server
python manage.py runserver

Docker cmds
 docker build -t matrimonybe .
 docker run -p 8000:8000 -d matrimonybe