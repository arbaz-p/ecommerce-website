# DRF E-Commerce Project

A RESTful e-commerce API built with **Django REST Framework (DRF)**. Users can register as **Customer**, **Seller**, or **Manager** and manage **products**, **cart**, and **orders**.

---

## Features

### User Roles
- **Customer**: Browse products, add items to cart, place orders.
- **Seller**: Add, update, and delete their own products.
- **Manager**: Manage users, oversee products, and process orders.

### Products
- CRUD operations (Create, Read, Update, Delete)
- Each product has: `name`, `description`, `price`, `stock`, and `seller`.

### Cart
- Customers can add/remove products, update quantities.
- View cart contents and total price.

### Orders
- Place orders from cart items.
- Track order status: pending, shipped, delivered, cancelled.
- Managers/Sellers can manage orders.

---

## Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/drf-ecommerce.git
cd drf-ecommerce
```
# Create virtual environment
```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```
# Install dependencies
```bash
pip install -r requirements.txt
```
# Apply migrations
```bash
python manage.py migrate
```
# Create superuser
```bash
python manage.py createsuperuser
```
# Run development server
```bash
python manage.py runserver
```