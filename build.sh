#!/bin/bash

# Run makemigrations and migrate
echo "Build Start"
python3.10 -m pip install -r requirements.txt
python3.10 manage.py makemigrations --noinput
python3.10 manage.py migrate --noinput
echo "Build End"

# Build the frontend (replace this with your actual frontend build command)
# npm run build

# Instruct Vercel to continue with the build
touch vercel-build
