📚 LibraryProject
🎯 Objective

Set up a Django development environment and create a basic Django project to gain familiarity with Django’s workflow.
This includes project creation, running the development server, and exploring the default project structure.

🧩 Task Description

Installed Django and created a new Django project named LibraryProject.
The setup serves as the foundation for developing Django applications and provides an understanding of the roles of key project components.

⚙️ Steps
1. Install Django

Ensure Python is installed on the system.
Install Django using pip:

pip install django

2. Create the Django Project

Create a new Django project named LibraryProject:

django-admin startproject LibraryProject

3. Run the Development Server

Navigate into the project directory:

cd LibraryProject


Create a README.md file inside the project directory.

Start the development server:

python manage.py runserver


Open a web browser and visit:

http://127.0.0.1:8000/


The default Django welcome page should appear, confirming a successful setup.

4. Explore the Project Structure

Expected directory structure:

LibraryProject/
│
├── LibraryProject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
