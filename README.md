# Educational Project

The Educational project is a single-page website designed for educational purposes. It includes features like user authentication, dynamic content management, and a basic code compiler.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- - [Admin Authentication](#admin-authentication)
- - [Dynamic Content](#dynamic-content)
- - [Code Compiler](#code-compiler)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Introduction

The Educational project is built using Django and provides a platform for educational content and basic code execution. It consists of two main apps: "accounts" for user management and "contents" for managing educational content.

## Features

### Admin Authentication

The "accounts" app includes a user model to manage admin accounts. Admin can logged in django's default admin panel and can update the content accordingly.

### Dynamic Content

The "contents" app allows administrators to manage educational content dynamically. Content includes paragraphs, sub_parts, introductions, about us sections, and contact us information.

### Code Compiler

The project provides a basic code compiler that executes Python code. Admin can change code snippets like `print('Hello World')` and visitors hit execute button and see the output on the website.

## Installation

Follow these steps to set up the Educational project locally:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/educational.git
   cd educational

2. Create Virtual Environment:
   ```
   python3 -m venv venv
   source venv/bin/activate

3. Install Project Dependencies:
   ```
   pip install -r requirements.txt

4. Apply Migrations and Migrate:
   ```
   create a folder in each app[accounts, contents] named as migrations
   and then create __inti__.py file in migrations folder
   then run the below commands
   
   python manage.py makemigrations
   python manage.py migrate
   
5. Create .env File:
   ```
   create a file named as .env
   now just opy the below keys and write you own values of them withou any inverted commas
   
   SECRET_KEY=
   DB_NAME=
   DB_USER=
   DB_PASSWORD=
   DB_HOST=
   DB_PORT=


6. Run Local Server
   ```
   python manage.py runserver


## Usage
Access the admin panel by visiting http://localhost:8000/admin/ and log in using the superuser credentials.
Use the admin panel to manage content, create users, and configure the website.
Explore the website to view and execute educational content. Try out the code compiler feature by entering Python code snippets.


## Configuration
The project uses environment variables for sensitive information. Set them in a .env file at the project root.
