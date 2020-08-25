# Chat demo using django channels

## Requirements
- Python 3.8
- Pipenv
- Docker

## Instructions
1. Install required packages:
    ```
    pipenv install
    ```

1. Start a Redis server on port `6379`:

    ```
    docker run -p 6379:6379 -d redis:5
    ```

1. Start the django server:
    ```
    pipenv run python manage.py runserver
    ```

1. Open 2 windows or tabs on a browser, then go to http://localhost:8000/chat/lobby on each of them.

1. Write any message on one of the lobbies, it should appear on every other chat window!

## Tests
Run all tests with:
```
pipenv run python manage.py test --settings=chat_app.settings.test
```
### Coverage report
Run tests with coverage support:
```
pipenv run coverage run manage.py test --settings=chat_app.settings.test
```
See the coverage report:
```
pipenv run coverage report
```