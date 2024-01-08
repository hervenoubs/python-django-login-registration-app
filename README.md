# Django Authentication Project

This Django project implements user authentication with features such as registration, login, home, and logout. The project uses MySQL as the database for storing user information. This project is going to grow to become a complete blogging website with its features and functionalities. Stay tune this week!

<img src="https://github.com/hervenoubs/python-django-login-registration-app/blob/main/ScreenShot.png" />

## Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:hervenoubs/python-django-login-registration-app.git
cd python-django-login-registration-app

2. Create a Virtual Environment

python -m venv venv

3. Activate the Virtual Environment
On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

4. Install Dependencies

pip install -r requirements.txt

5. Set Up MySQL Database
Create a MySQL database and update the DATABASES configuration in simpleauth/settings.py with your database details:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'users_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
6. Run Migrations

python manage.py makemigrations
python manage.py migrate

7. Create a Superuser (Optional)

python manage.py createsuperuser

8. Set Environment Variables
Create a .env file in the project root and set your Django secret key:

9. Run the Development Server

python manage.py runserver
Visit http://127.0.0.1:8000 in your browser.

Project Structure

authentication/: Django app for handling authentication features.
templates/: HTML templates for the project views.

Contributing
If you would like to contribute to this project, please follow the standard GitHub flow:

Fork the repository
Create a new branch (git checkout -b feature/your-feature)
Commit your changes (git commit -am 'Add some feature')
Push to the branch (git push origin feature/your-feature)
Create a new pull request]

This project is going to grow to become a complete blogging website with its features and functionalities.
