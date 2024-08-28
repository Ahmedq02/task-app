# task-app

A django web applicaiton for adding tasks and showing reports on the tasks.

## Instalation

1. clone the repo
git clone https://github.com/Ahmedq02/task-app.git
cd task-app

2. Install pipenv if you haven't installed it
pip install pipenv

3. Install dependencies with pipenv and activate the environment
pipenv install
pipenv shell

4. Apply migrations 
python manage.py migrate

5. Run the server, by default this will run at port 8000
python manage.py runserver