## Simple Student Self-Registration System (SSSRS)

**Framework:** Django (Python)
**Project Type:** Web Application
**Target Users:** Students and Administrators

---

## 1. Project Description

The **Simple Student Self-Registration System (SSSRS)** is a beginner-level Django web application that allows students to register themselves into the system without administrator assistance.

The system also provides basic administrative functionality to view and manage registered students through the Django Admin Panel.

This project is developed mainly for **learning purposes**, especially for beginners in **Django**, **Git**, and **GitHub collaboration**.

---

## 2. Project Objectives

* Allow students to create accounts through self-registration
* Manage student information using Django ORM
* Practice Django authentication and authorization
* Support beginner-friendly collaboration using Git and GitHub

---

## 3. System Features

### Student Features

* Student self-registration
* Login and logout
* View personal profile information

### Admin Features

* View all registered students
* Manage users via the Django Admin Panel

---

## 4. Technologies Used

* **Programming Language:** Python
* **Framework:** Django
* **Database:** SQLite3
* **Frontend:** HTML, CSS (basic)
* **Version Control:** Git & GitHub

---

## 5. Basic Project Structure

```
Students_Registration/
│
├── Students_Registration/   # Main Django project folder
├── Students/                # Student registration app
├── db.sqlite3               # SQLite database
└── manage.py                # Django management file
└── requirements.txt         # Requirements.txt file 
```

---

## 6. Installation and Setup

Follow the steps below to run the project locally.

### 1. Clone the Project Repository

```bash
git clone https://github.com/edortie03/Simple_Students_Registration.git
cd Simple_Students_Registration
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 4. Install Project Dependencies

All required packages are already listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

---

### 6. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create admin login credentials.

---

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

Admin panel:

```
http://127.0.0.1:8000/admin/
```

---

## 7. User Roles

* **Student:** Can register, log in, log out, and view personal details
* **Admin:** Can manage users and student data via the Django Admin Panel

---

## 8. Learning Outcomes

* Understanding Django project and app structure
* Working with Django forms and authentication
* Using Django ORM for database operations
* Collaborating effectively using Git and GitHub
* Applying basic web development concepts

---

## 9. Limitations

* No email verification
* Basic user interface
* No role-based dashboards
* Intended for learning and demonstration purposes only

---

## 10. Future Improvements

* Email verification system
* Improved UI using Bootstrap
* Student profile editing
* Password reset functionality
* Role-based dashboards

---

## 11. Contributors

This project is developed by a team of beginner developers for educational purposes.

---

## Updating Dependencies

If new packages are added during development, update the dependency file using:

```bash
pip freeze > requirements.txt
```

Commit the updated file to keep all contributors in sync.
Always work on your branch abd then push on the main branch
