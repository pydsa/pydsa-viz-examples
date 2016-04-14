#!/bin/bash

python pyDSA/manage.py makemigrations
python pyDSA/manage.py migrate
python pyDSA/manage.py createsuperuser
python pyDSA/manage.py runserver
