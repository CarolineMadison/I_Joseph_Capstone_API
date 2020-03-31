Welcome to I, Joseph! 

Steps to get I, Joseph started:

1. Clone the repo and cd into it

2. To Create your OSX virtual environment in Terminal:

      python -m venv ijosephENV
      source ./ijosephENV/bin/activate

3. To Create your Windows virtual environment in Command Line:

      python -m venv ijosephENV
      source ./ijosephENV/Scripts/activate

3. pip install -r requirements.txt

4. Build your database from the existing models:

  python manage.py makemigrations ijosephapp
  python manage.py migrate
  
5. python manage.py runserver

