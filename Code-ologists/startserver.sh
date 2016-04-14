#!/bin/bash

python pydsa/manage.py makemigrations
python pydsa/manage.py migrate
python pydsa/manage.py createsuperuser
python pydsa/manage.py runserver
