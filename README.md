###### Tech Stack: Python/Django, SQL, CSS ######

# Welcome to I, Joseph!
# Story

I Joseph is an appication that connects members of a community to volunteer opportunities to help families in need. Users of this application can create new jobs to submit to the community. Users can select jobs to complete, can deselect them if they change their mind, and can mark them as complete. Users can see when jobs they have submitted have been complete and can edit and delete their submitted jobs.

<hr />

*Wireframes*

![](/ijosephproject/ijosephapp/images/I_Joseph_Wireframe_ONE.jpg)




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
