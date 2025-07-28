# E-Sports Store – Python & Django Web Development Project

# Project Overview
E-Sports Store is a full-stack web application built using Python and Django that simulates an online platform for selling e-sports-related products such as gaming accessories, jerseys, merchandise, and more. This project showcases the implementation of core web development concepts like user authentication, product catalog management, shopping cart functionality, order tracking, and admin controls.
# Objective
To develop a scalable and responsive e-commerce website tailored to the e-sports and gaming community, enabling users to browse and purchase products while offering admins full control over product listings and orders.
# Features
👤 User Features:
	•	Register and log in securely
	•	Browse products by category (Bat, Footboll, Batminton, etc.)
	•	Add items to the shopping cart
	•	Checkout and place orders
	•	View order history
	•	Search and filter products

# Admin Features:
	•	Admin dashboard
	•	Add/edit/delete products
	•	View and manage orders
	•	Manage user accounts

# Tech Stack
	•	Frontend: HTML, CSS, Bootstrap
	•	Backend: Python, Django
	•	Database: SQLite (or PostgreSQL for production)
	•	Tools: Django Admin, Django ORM, Crispy Forms
# Project Structure
esports-store/
├── esports_store/          # Project settings
│   ├── settings.py
│   └── urls.py
├── store/                  # Main app for products
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/store/
│   └── static/store/
├── cart/                   # Shopping cart logic
├── orders/                 # Order and payment handling
├── users/                  # User registration/login
├── media/                  # Uploaded product images
├── manage.py
└── README.md
# Database Models
	•	User (Django’s built-in user model)
	•	Product (name, price, category, image, stock)
	•	Cart (session-based or user-bound)
	•	Order (products, quantity, payment info, status)

# Setup Instructions
# 1️. Clone the Repository
```bash
git clone https://github.com/yourusername/esports-store.git
cd esports-store
2.Create a Virtual Environmen
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install Requirements
```bash
pip install -r requirements.txt
4.Apply Migrations and Create Superuser
```bash
python manage.py migrate
python manage.py createsuperuser
5.Run the Development Serve
```bash
python manage.py runserver

* Then go to:
	•	Frontend: http://127.0.0.1:8000/
	•	Admin Panel: http://127.0.0.1:8000/admin/

# Future Enhancements
	•	Payment gateway integration (Razorpay, Stripe)
	•	Product reviews and ratings
	•	Responsive frontend with Tailwind or React
	•	Real-time inventory updates
	•	Wishlist feature
# License
This project is licensed under the MIT License.

# Author
	•	Saket Prashar
	•	GitHub
	•	LinkedIn



