# Django CRUD Web App

![version](https://img.shields.io/badge/Version-Dev-blue)
![release](https://img.shields.io/badge/Release-0.6.0-blue)
![language](https://img.shields.io/badge/Language-python-brightgreen)
![last-update](https://img.shields.io/badge/Last_update-9/2/2022-orange)

Example of a CRUD web application, using the Django framework.

## Run Django CRUD app
Commands to create the virtual environment (`venv`) and run the **Django CRUD app** on the web server.

```console
  cd C:\Dev Projects\django-crud
  python -m venv .venv
  .venv\Scripts\activate
  cd webapp\
  python manage.py runserver 8080
  deactivate
```

**Note**: The following command should be executed only the first time:

```console
  python -m venv .venv
```

## Project Dependencies
The list of project requirements can be found in the following text <a href="https://github.com/ansegura7/django-crud/blob/main/requirements.txt">file</a>.

To automatically install the exact version of all dependencies, run the following commands in the terminal:

```console
  cd C:\Dev Projects\django-crud
  .venv\Scripts\activate
  pip install -r requirements.txt
```

To manually install the latest version of Django, run the following command in the terminal:

```console
  pip install Django
```

## Contributing and Feedback
Any kind of feedback/suggestions would be greatly appreciated (algorithm design, documentation, improvement ideas, spelling mistakes, etc...). If you want to make a contribution to the course you can do it through a PR.

## Author
- Created by Andrés Segura-Tinoco
- Created on Feb 01, 2018

## License
This project is licensed under the terms of the <a href="https://github.com/ansegura7/django-crud/blob/master/LICENSE">MIT license</a>.
