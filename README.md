# task-app

A django web applicaiton for adding tasks and showing reports on the tasks.

## Instalation

1. clone the repo
git clone https://github.com/Ahmedq02/task-app.git
cd task-app

2. Install `poetry` if you haven't installed it

3. Install dependencies with `poetry` and activate the environment

`poetry install`
`make activate`

4. Apply migrations 
`make migrate`

5. Create `.env` file with `STANDARD_USER_USERNAME` variable set

6. Run the server, by default this will run at port 8000

`make runserver`

7. Nagivate to the admin page and create a new user with the username set in `STANDARD_USER_USERNAME` (this will be auto-populated) - this will be the passkey used for accessing the app