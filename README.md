# Loan Management Web App

## How to run this project locally

1. Install Python 3 (v>=3.10)
2. Make a virual environment and activate it
3. Install the neccessary dependencies for this project by running:
  ```
    pip install -r requirements.txt
  ```
4. Migrate the database:
  ```
    python3 manage.py makemigrations

    python3 manage.py migrate
  ```
5. Run the project:
  ```
    python3 manage.py runserver
  ```
