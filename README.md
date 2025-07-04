# Django Expense Tracker API - Intern Task


## Project Overview
  ##### Goal: Build a REST API for expense/income tracking with user authentication.

## Core Requirements
 ### User Access Control

###### Regular users: Can only manage their own expense/income records.

###### Superusers: Can access and manage all users' records.

###### Authentication: JWT tokens required for all API operations. 




## Key Features

##### User registration and login system.

##### Personal expense/income tracking.

##### Automatic tax calculation (flat amount or percentage).

##### Paginated API responses.

##### Complete CRUD operations.


## 🔗 API Endpoints
### Authentication
##### POST /api/auth/register/ → User registration

##### POST /api/auth/login/ → User login (returns JWT tokens)

##### POST /api/auth/refresh/ → Refresh JWT token



## 🔧 Technical Requirements
##### Backend: Django, Django REST Framework

##### Authentication: JWT (djangorestframework-simplejwt)

##### Database: SQLite (development)

##### Python: 3.8+

