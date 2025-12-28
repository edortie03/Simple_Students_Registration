Simple Student Self-Registration System (SSSRS)

**Framework:** Django (Python)
**Project Type:** Web Application
**Target Users:** Students and Administrators

---

1. Project Description

The **Simple Student Self-Registration System (SSSRS)** is a beginner-level Django web application that allows students to register themselves into the system without the help of an administrator.

The system also provides basic administrative control to view registered students.
This project is designed mainly for **learning purposes**, especially for beginners in **Django**, **Git**, and **GitHub collaboration**.

---

2. Objectives

* Allow students to create their own accounts (self-registration)
* Manage student information using Django ORM
* Practice Django authentication and authorization
* Support beginner-friendly team collaboration using GitHub

---

3. System Features

Student Features
* Student self-registration
* Login and logout
* View personal profile information

Admin Features

* View all registered students
* Manage users through Django Admin Panel

---

4. Technologies Used

* **Programming Language:** Python
* **Framework:** Django
* **Database:** SQLite3
* **Frontend:** HTML, CSS (basic)
* **Version Control:** Git & GitHub

---

5. Project Structure (Basic)

```
Students_Registration/
│
├── Students_Registration/        # Main Django project folder
├── Students/     # Student registration app
├── db.sqlite3    # Database
└── manage.py     # Django management file
```

6. Installation and Setup

1. Install Python (version 3.8 or higher)
2. Create and activate a virtual environment
3. Install Django

   ```bash
   pip install django
   ```
4. Clone the project repository
5. Run migrations

   ```bash
   python manage.py migrate
   ```
6. Create a superuser

   ```bash
   python manage.py createsuperuser
   ```
7. Start the development server

   ```bash
   python manage.py runserver
   ```
8. Open your browser and visit

   ```
   http://127.0.0.1:8000/
   ```

7. User Roles

* **Student:** Can register, login, and view personal details
* **Admin:** Can manage all users via Django Admin Panel

---

8. Learning Outcomes

* Understanding Django project structure
* Working with Django forms and authentication
* Using Django ORM for database operations
* Collaborating using Git and GitHub
* Applying basic web development concepts


## 9. Limitations

* No email verification
* Basic user interface
* No role-based dashboards
* Intended for learning and demonstration only

---

## 10. Future Improvements

* Email verification system
* Improved UI using Bootstrap
* Student profile editing
* Password reset functionality
* Role-based dashboards

---

## 11. Contributors

This project is developed by a team of beginner developers for learning purposes.
