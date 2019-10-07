# Code Bible

A small application designed to capture code snippets which solve a specific problem, or share some interesting solution.

Currently it depends on [PrismJS](https://prismjs.com) for the syntax highlighting.

# Functionality

Currently you can

- View all code tricks
- Add a new code trick

Eventually I hope to add

- View code tricks by language
- Search code tricks
- Tagging or other metadata
- Rating code tricks
- Tricks of the day :D
- Users
- View code tricks by user
- Pagination of results
- Related code tricks

# Running

## VirtualEnv



## VirtualEnv

- `pip install virtualenv`
- `source venv/bin/activate`'

and when finished

- `deactivate`

## Dependencies

- `pip install -r requirements.txt`


# Database

Currently it's just a toy project, so I've just packaged the sqlite database in the repo :)

Should you need to change the models
1. `python manage.py makemigrations tricks`
2. `python manage.py migrate`

## Running the Server

`python manage.py runserver`