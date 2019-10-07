# Code Bible

A small application designed to capture code snippets which solve a specific problem, or share some interesting solution.

Currently it depends on [PrismJS](https://prismjs.com) for the syntax highlighting.

# Running

## Dependencies

Developed using 

- Python 3.7.4
- Django 2.2.6

# Database

Currently it's just a toy project, so I've just packaged the sqlite database in the repo :)

Should you need to change the models
1. `python manage.py makemigrations tricks`
2. `python manage.py migrate`

## Running the Server

`python manage.py runserver`