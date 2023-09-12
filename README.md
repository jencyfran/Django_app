Build a Django service in Python and deploy it on AWS using a free tier service. Make sure you comment on your code and have documentation in a Readme.MD file to represent how to start the service. Make sure to have the service able to receive and send out dummy data.

Getting Started
Prerequisites
Python (>=3.6)
Django
AWS CLI (for deployment)


# STEPS

1. virtualenv venv
2. django-admin startproject storage
3. django-admin startapp api
4. python3 manage.py makemigrations
5. python3 manage.py migrate
6. python3 manage.py runserver

## Access on Ports

### ADMIN
1. http://127.0.0.1:8000/admin/
2. Username: jency
3. pass: 1234

### ITEM
http://127.0.0.1:8000/api/item/

### LOCATION
http://127.0.0.1:8000/api/location/




# STEPS for AWS - EC2 

1. sudo dnf update -y
2. sudo dnf install git -y
3. git clone https://github.com/jencyfran/Django_app.git
4. cd Django_app
5. sudo dnf install pip -y
6. pip install django djangorestframework
7. pip install pillow
8. python3 manage.py makemigrations
9. python3 manage.py migrate
10. python3 manage.py runserver 0.0.0.0:8000

