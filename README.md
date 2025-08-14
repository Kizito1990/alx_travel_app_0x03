🏝️ ALX Travel App 0x01 – API Development for Listings and Bookings
📌 Overview

This project is part of the ALX Backend Django & DRF learning series.
In alx_travel_app_0x01, we implemented API endpoints for managing Listings and Bookings using Django REST Framework (DRF) and documented them with Swagger UI.

The app allows users to:

View, create, update, and delete Listings.

View, create, update, and delete Bookings.

Explore the API via Swagger documentation.

📂 Project Structure
alx_travel_app/
│
├── listings/
│   ├── migrations/              # Database migrations
│   ├── management/              # Custom management commands
│   ├── templates/               # HTML templates (if needed)
│   ├── models.py                 # Listing, Booking, Review models
│   ├── serializers.py            # DRF serializers
│   ├── views.py                  # API ViewSets
│   ├── urls.py                   # API routes
│   └── admin.py                  # Admin panel configuration
│
├── alx_travel_app/
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Project URL configuration
│   └── wsgi.py                   # WSGI entry point
│
├── manage.py                     # Django management script
└── README.md                     # Project documentation


🌐 API Endpoints
Method	Endpoint	Description
GET	/api/listings/	Get all listings
POST	/api/listings/	Create new listing
GET	/api/listings/{id}/	Get listing by ID
PUT	/api/listings/{id}/	Update listing
DELETE	/api/listings/{id}/	Delete listing
GET	/api/bookings/	Get all bookings
POST	/api/bookings/	Create new booking
GET	/api/bookings/{id}/	Get booking by ID
PUT	/api/bookings/{id}/	Update booking
DELETE	/api/bookings/{id}/	Delete booking
📜 Swagger Documentation

Once the server is running, open your browser and visit:

http://127.0.0.1:8000/swagger/


Here you can test endpoints interactively and explore the API schema.

🛠 Tech Stack

Python 3.x

Django 5.x

Django REST Framework

drf-yasg (Swagger/OpenAPI docs)

SQLite (Default DB, can be changed to PostgreSQL/MySQL)

🚀 Author

Kizito Azegba
Backend Developer | Django & DRF Specialist