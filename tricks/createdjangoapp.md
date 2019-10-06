# Creating a Django App
-----------------------

1. django-admin startproject codebible
2. cd codebible/
3. python manage.py startapp <app-name>
4. python manage.py migrate
5. python manage.py runserver
6. Make models
7. Add App config to settings
8. python manage.py makemigrations <app-name>
9. Create admin
    - python manage.py createsuperuser