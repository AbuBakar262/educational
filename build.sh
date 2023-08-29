#!/bin/bash

# Run makemigrations and migrate
echo "Build Start"
eche "Make migrations"
python manage.py makemigrations --noinput
echo "Migrating"
python manage.py migrate --noinput
echo "Build End"

# Build the frontend (replace this with your actual frontend build command)
# npm run build

# Instruct Vercel to continue with the build
touch vercel-build
