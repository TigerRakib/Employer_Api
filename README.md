# 🧑‍💼 Employer Management System API

A simple RESTful API for managing employers using Django REST Framework (DRF) with JWT authentication and a custom user model.

---

## 📦 Features

- Custom User Model (email as username)
- JWT Authentication (`djangorestframework-simplejwt`)
- CRUD for Employer records
- Protected API endpoints
- Clean and scalable codebase

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/employer-api.git
cd employer-api
```

### 2. Set Up Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

---

## 🔐 Authentication

This project uses **JWT (JSON Web Tokens)** for authentication.

### Obtain Token

`POST /api/token/`

```json
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

### Refresh Token

`POST /api/token/refresh/`

```json
{
  "refresh": "your_refresh_token"
}
```

Include the **access token** in the `Authorization` header for protected endpoints:

```
Authorization: Bearer your_access_token
```

---

## 📂 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/token/`          | Get JWT token pair (login) |
| POST   | `/api/token/refresh/`  | Refresh access token |
| GET    | `/api/employers/`      | List all employers |
| POST   | `/api/employers/`      | Create new employer |
| GET    | `/api/employers/<id>/` | Retrieve employer by ID |
| PUT    | `/api/employers/<id>/` | Update employer |
| DELETE | `/api/employers/<id>/` | Delete employer |

---



## 🛠 Tech Stack

- Python 3
- Django
- Django REST Framework
- Simple JWT
- SQLite (default, can switch to PostgreSQL)

---

## 📁 Project Structure

```
employer_api/
├── accounts/         # Custom user model app
├── employers/        # Employer model and views
├── employer_api/     # Project settings
├── manage.py
└── requirements.txt
```

---

## 🤝 License

This project is licensed under the MIT License.
