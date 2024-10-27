# API Documentation

## Overview

This API allows for the management of funds, including creating, retrieving, updating, and deleting fund records. The API follows RESTful principles and uses JSON for data interchange.

## Setup Instructions

### 1. Prerequisites

Make sure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)
- **virtualenv** (recommended for creating isolated environments)
- **MySQL** (or an alternative database, if not already available)

### 2. Install Dependencies

Use `pip` to install the project dependencies. 

**Dependencies:**

- **Django**: Web framework
- **djangorestframework**: Django REST framework for building APIs
- **mysqlclient** (or PyMySQL as an alternative): MySQL adapter (or another adapter if using a different database)

### 3. Set Up the Database

**Create a MySQL Database**:
   Open MySQL and create a database for the project:
   ```sql
   CREATE DATABASE fund_db;
   ```

### 4. Run Migrations

To create the necessary tables in the database, run:
```bash
python manage.py makemigrations
python manage.py migrate --run-syncdb
```

The `--run-syncdb` flag ensures all tables are created even if some migrations do not use ORM models directly.

### 5. Exclude ContentType Data

Open the Django shell and run the following commands:

```bash
python manage.py shell
```

In the shell, run:

```python
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
```

Then exit the shell with:

```python
quit()
```

### 6. Load Data from Fixture

Load the JSON data dump (e.g., `datadump.json`) into the database with:

```bash
python manage.py loaddata datadump.json
```

This will populate the database with data specified in the fixture file.


### 7. Start the Development Server

Run the Django development server:
```bash
python manage.py runserver
```

The API is now accessible at `http://127.0.0.1:8000/funds/` by default.

### 8. Access the Admin Panel

Once the server is running, go to the admin panel at `http://127.0.0.1:8000/admin/` and log in with:

- **Username**: `user`
- **Password**: `pass`

This setup will give you direct access to manage your models and data through Django's admin interface with the specified credentials.

## Endpoints

### 1. List and Create Funds

- **URL**: `/funds/`
- **Methods**: `GET`, `POST`

#### GET Request

- **Description**: Retrieve a list of all funds.
- **Sample Request**:
    ```http
    GET /funds/
    ```

- **Response**:
    - **Status**: `200 OK`
    - **Body**:
    ```json
    [
        {
            "fund_id": "FUND001",
            "fund_name": "Test Fund",
            "fund_manager_name": "John Doe",
            "fund_description": "A test fund for unit testing.",
            "fund_nav": "100.00",
            "date_of_creation": "2023-01-01",
            "fund_performance": "10.00"
        }
    ]
    ```

#### POST Request

- **Description**: Create a new fund.
- **Sample Request**:
    ```http
    POST /funds/
    Content-Type: application/json

    {
        "fund_id": "FUND001",
        "fund_name": "Test Fund",
        "fund_manager_name": "John Doe",
        "fund_description": "A test fund for unit testing.",
        "fund_nav": "100.00",
        "date_of_creation": "2023-01-01",
        "fund_performance": "10.00"
    }
    ```

- **Response**:
    - **Status**: `201 Created`
    - **Body**:
    ```json
    {
        "fund_id": "FUND001",
        "fund_name": "Test Fund",
        "fund_manager_name": "John Doe",
        "fund_description": "A test fund for unit testing.",
        "fund_nav": "100.00",
        "date_of_creation": "2023-01-01",
        "fund_performance": "10.00"
    }
    ```

### 2. Retrieve, Update, and Delete a Specific Fund

- **URL**: `/funds/<str:id>/`
- **Methods**: `GET`, `PUT`, `DELETE`

#### GET Request

- **Description**: Retrieve a specific fund by its ID.
- **Sample Request**:
    ```http
    GET /funds/FUND001/
    ```

- **Response**:
    - **Status**: `200 OK`
    - **Body**:
    ```json
    {
        "fund_id": "FUND001",
        "fund_name": "Test Fund",
        "fund_manager_name": "John Doe",
        "fund_description": "A test fund for unit testing.",
        "fund_nav": "100.00",
        "date_of_creation": "2023-01-01",
        "fund_performance": "10.00"
    }
    ```

#### PUT Request

- **Description**: Update a specific fund.
- **Sample Request**:
    ```http
    PUT /funds/FUND001/
    Content-Type: application/json

    {
        "fund_id": "FUND001",
        "fund_name": "Updated Fund",
        "fund_manager_name": "John Doe",
        "fund_description": "A test fund for unit testing.",
        "fund_nav": "100.00",
        "date_of_creation": "2023-01-01",
        "fund_performance": "10.00"
    }
    ```

- **Response**:
    - **Status**: `200 OK`
    - **Body**:
    ```json
    {
        "fund_id": "FUND001",
        "fund_name": "Updated Fund",
        "fund_manager_name": "John Doe",
        "fund_description": "A test fund for unit testing.",
        "fund_nav": "100.00",
        "date_of_creation": "2023-01-01",
        "fund_performance": "10.00"
    }
    ```

#### DELETE Request

- **Description**: Delete a specific fund by its ID.
- **Sample Request**:
    ```http
    DELETE /funds/FUND001/
    ```

- **Response**:
    - **Status**: `204 No Content`

---

# SQL Database Schema

## Fund Table

### Schema

| Field Name           | Data Type        | Constraints                             |
|---------------------|------------------|----------------------------------------|
| fund_id             | VARCHAR(50)      | PRIMARY KEY                            |
| fund_name           | VARCHAR(255)     | NOT NULL                               |
| fund_manager_name    | VARCHAR(255)     | NOT NULL                               |
| fund_description    | TEXT             | NOT NULL                               |
| fund_nav            | DECIMAL(20, 2)   | NOT NULL, CHECK (fund_nav >= 0.00)    |
| date_of_creation    | DATE             | NOT NULL                               |
| fund_performance     | DECIMAL(7, 2)    | NOT NULL, CHECK (fund_performance >= -100.00 AND fund_performance <= 1000.00) |

### Sample SQL Commands

#### Create Table

```sql
CREATE TABLE funds_fund (
    fund_id VARCHAR(50) PRIMARY KEY,
    fund_name VARCHAR(255) NOT NULL,
    fund_manager_name VARCHAR(255) NOT NULL,
    fund_description TEXT NOT NULL,
    fund_nav DECIMAL(20, 2) NOT NULL CHECK (fund_nav >= 0.00),
    date_of_creation DATE NOT NULL,
    fund_performance DECIMAL(7, 2) NOT NULL CHECK (fund_performance >= -100.00 AND fund_performance <= 1000.00)
);
```

#### Sample Insert

```sql
INSERT INTO funds_fund (fund_id, fund_name, fund_manager_name, fund_description, fund_nav, date_of_creation, fund_performance) 
VALUES ('FUND001', 'Test Fund', 'John Doe', 'A test fund for unit testing.', 100.00, '2023-01-01', 10.00);
```

#### Sample Select

```sql
SELECT * FROM funds_fund WHERE fund_id = 'FUND001';
```
