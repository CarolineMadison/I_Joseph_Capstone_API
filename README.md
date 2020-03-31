Welcome to I, Joseph, A Community of Helpers

Steps to get I, Joseph started:

1. Clone the repo and cd into it

2. Create your OSX virtual environment in Terminal:

  python -m venv workforceenv
  source ./workforceenv/bin/activate

  OR Create your Windows virtual environment in Command Line:

  python -m venv workforceenv
  source ./workforceenv/Scripts/activate
  Install the app's dependencies:

3. pip install -r requirements.txt

4. Build your database from the existing models:

  python manage.py makemigrations ijosephapp
  python manage.py migrate
  
5. python manage.py runserver

