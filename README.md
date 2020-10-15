# BasicAuthAPI

Basic Authentication and Crop Data API - Django and Python3 Application

- Sign up - for a user to create an account
- Sign in
- Get Data for 10 crops


## How to run this app:

```
git clone https://github.com/Utkarsh3587/BasicAuthAPI.git
python3.7 -m venv api-env
source api-env/bin/activate
cd BasicAuthAPI
pip install -r requirments.txt
python manage.py migrate
python manage.py runserver
```

## Sign UP API

```
URL: localhost:8000/users/register/
Method: POST
Headers
Content-Type: application/json
JSON BODY Request Parameters - User Registeration API
{
	"email":"xyz@example.com",
	"password":"password123@"
}
```

Response: JSON Response containing user email and user id

## Login API

```
URL: localhost:8000/users/login/
Method: POST
Headers
Content-Type: application/json
JSON BODY Request Parameters - User Login API
{
	"email":"xyz@example.com",
	"password":"password123@"
}
```
Response: JSON Response containing user email and user id

## Fetch Crops Data API

```
URL: localhost:8000/crops/
Method: GET
Headers
Content-Type: application/json
```
Response: JSON Response containing a list of crops data
