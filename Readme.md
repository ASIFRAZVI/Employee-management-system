# Employee Management System API

## Overview

The Employee Management System API allows Companies to efficiently manage their Employee. This API provides endpoints for creating, reading, Retreiving, updating, and deleting (CRUD) Employees. It uses JSON Web Tokens (JWT) for secure authentication.

## Features

- User registration and login
- JWT-based authentication
- CRUD operations for employee items
- Secure access to the API
- Modular python application 

## Technologies Used

- Django
- Django REST Framework
- JWT Authentication
- PostgreSQL
- Python 3.x

## Installation

### Prerequisites

- Python 3.x installed on your machine.
- Virtualenv
- PostgreSQL.

### Steps to Set Up the Project

1. **Clone the Repository**

   git clone <repository-url>
   cd employee_management_system

2. **Create a Virtual Environment**

   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install Required Packages**

   pip install -r requirements.txt

4. **create .env**

   configure django_secret(djano secreate), DEBUG(True), JWT_SECRET(jwt key) DB_MODE(dev or prod) \*\*note this all are variable names use same

   \*\*db configuration for development mode in env (DB_MODE="dev")
   DB_ENGINE(engine name), DB_NAME(database name), DB_USER(admin name), DB_PASSWORD(admin password), DB_HOST, DB_PORT \*\*note this all are variable names use same

   \*\*db configuration for production mode in env (DB_MODE="prod")
   PRO_DB_ENGINE(engine name), PRO_DB_NAME(database name), PRO_DB_USER(admin name), PRO_DB_PASSWORD(admin password), PRO_DB_HOST, DB_PORT \*\*note this all are variable names use same

5. **Run Migrations**

   python manage.py migrate

6. **runserver**
   cmd
   start.bat

**API Endpoints**

**_Authentication Endpoints_**

### Register a New User

URL: /api/auth/register/
Method: POST
Request Body:

json
{
"email": "user@example.com"
}

Response:
Success: 201 Created
json
{
"email": "user@example.com",
"password": "generated_password"
}

Error: 400 Bad Request
json
{
"error": "A user with this email already exists."
}

**\*Login User**
URL: /api/auth/login/
Method: POST
Request Body:
json
{
"email": "user@example.com",
"password": "your_password"
}

Response:
Success: 200 OK
json
{
"token": "jwt_token",
"refresh_token": "refresh_token",
"ok": "cookies stored!"
}

Error: 400 Bad Request
json
{
"error": "Invalid Email, please provide valid email"
}

**Logout User**
URL: /api/auth/logout/
Method: POST

Response:
Success: 200 OK
json
{
"message": "Logged out successfully."
}

### Employee management Endpoints

**Create Employee**
URL: /api/employee/
Method: POST

Request Body:
json
{
"name":"name",
"email":"example@gmail.com",
"department":"1", (optional choice)
"role":"1" (optional choice)
}

Response:
Success: 201 Created
json
{
"message": "Employee Created!"
}

Error: 400 Bad Request
json
{
"error": "please provide the unique Email"
}

**Get All Employee Items (LIST)**
URL: /api/employee/
Method: GET

Response:
Success: 200 OK
json
[
{
"id": "uuid",
"name": "name",
"email": "example@gmail.com",
"department": "1",
"role": "1",
"user": {
"email": "example@gmail.com"
}
}
...
]

**Get Employees by ID**
URL: /api/mgmt/inventory/<uuid:id>/
Method: GET
Response:
Success: 200 OK
json
[
{
"id": "uuid",
"name": "name",
"email": "example@gmail.com",
"department": "1",
"role": "1",
"user": {
"email": "example@gmail.com"
}
}
]

Error: 400 (if not found)
json
{
"message": "Employee does't exists"
}

**Update Employees**
URL: /api/mgmt/inventory/<uuid:id>/
Method: PUT

Request Body:
json
{
"name":"name",
"email":"example@gmail.com",
"department":"1", (optional choice)
"role":"1" (optional choice)
}

Response:
Success: 200 OK
json
{
"message": "Employee details Updated"
}

Error: 400 (if pk is not provided)
json
{
"message": "please enter employee id"
}

**Delete Inventory Item**
URL: /api/mgmt/inventory/<uuid:id>/
Method: DELETE
Response:
Success: 204 No Content

Error: 400 (if pk is not provided)
json
{
"message": "please enter employee id"
}

---````------------------:^

### For more information refer swagger documebtation

http://host:port/api/schema/swagger-ui/

Portfolio = https://asifrazvi.netlify.app/

----Thankyou :)
