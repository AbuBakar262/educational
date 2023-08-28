#!/bin/bash

# Run makemigrations and migrate
python manage.py makemigrations
python manage.py migrate

# Build the frontend (replace this with your actual frontend build command)
# npm run build

# Instruct Vercel to continue with the build
touch vercel-build
