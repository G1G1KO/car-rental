# 🚗 WeRent — Car Rental Web Platform

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0+-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Lucide Icons](https://img.shields.io/badge/Icons-Lucide-F56565?style=for-the-badge)

**WeRent** is a Django-based car rental web application where users can list their cars for rent, search and filter available vehicles, book them online, and manage rentals from their profile.

---

## ✨ Main Features

- **User Authentication & Profile:** Register, log in, and manage personal listings, rented cars, liked cars, and notifications.
- **Car Listings (CRUD):** Add, edit, and delete cars with up to 3 photos per listing.
- **Search, Filter & Pagination:** Filter cars by city, fuel type, transmission, price, or brand/model with pagination.
- **Online Car Rental:** Rent available cars, calculate total price by days, and track remaining rental time.
- **Notifications:** Automatic notifications for car owners when someone rents their car, with a navbar counter and delete option.
- **Likes System:** Like/unlike cars and view top-liked vehicles on the home page.
- **Responsive Design:** Works on desktop, tablet, and mobile screens with clean Lucide vector icons.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, Lucide Icons
- **Database:** SQLite3

---

## 📂 Project Structure

```text
car-rental/
├── accounts/               # User registration, login, and profile
├── cars/                   # Car CRUD, filtering, rentals, and notifications
│   ├── context_processors.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── conf/                   # Main project settings and URLs
├── static/
│   └── css/
│       └── styles.css      # Global and responsive styles
├── templates/              # HTML templates (base, accounts, cars)
├── .gitignore
├── manage.py
└── README.md