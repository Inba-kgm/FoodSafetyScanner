#!/usr/bin/env bash
# exit on error
set -o errexit

# Install all the packages from requirements.txt
pip install -r requirements.txt

# Gather all CSS, Images, and JS into the staticfiles folder
python manage.py collectstatic --no-input

# Update the database to the latest models
python manage.py migrate