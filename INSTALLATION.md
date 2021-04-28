# Makrwatch Coding Challenge

The application is divided into two parts - Frontend and Backend.
The frontend is written in React and the backend is written in Django (a python web framework). It is therefore assumed that you have installed [Node](https://nodejs.org/en/download/) and [Python](https://www.python.org/downloads/). Please do refer to the links to install those if you have not already.

You are encouraged to use a virtual environment for this application. This application used pipenv. To install pipenv run the following command.

```bash
pip install pipenv
```
Install the project dependencies by installing the packages in the Pipfile with the command
```bash
pipenv install
```
You can start the virtual environment by running the command
```bash
pipenv shell
```

## Running the server (backend)

The server is a DJango - Django Rest Framework application. To run it, please go to the backend folder and type the command

```bash
python manage.py runserver
```


## Running the client (frontend)
The client is a react application. Please run the following command to install the dependencies
```bash
npm install
```
Then start the project with the command
```bash
npm start
```

## Tests
To run the tests, type the following command
```bash
python manage.py test
```

### Side notes
 Please do have a **.env** file in the **./backend/api/** folder and add this line to it
```bash
API_KEY=<YOUR_API_KEY>
```
where <YOUR_API_KEY> is the credentials key from Google to use the Youtube Data API.