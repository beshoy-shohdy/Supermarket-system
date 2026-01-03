# Supermarket Management System

A **Python Tkinter-based supermarket management system** with Admin, Employee, and Customer panels, integrated with **MySQL**.

---

## Setup Instructions

### 1. Database

1. Import the `shop_db` **structure and data** into MySQL.
2. Run the following command to allow updates in the database:

```sql
SET SQL_SAFE_UPDATES = 0;
```

3. Open `loginDef/.env` and update with your **database name** and **password**.

---

### 2. Install Dependencies

Run this command to install the MySQL connector for Python:

```bash
pip install mysql-connector-python
```

---

### 3. Run the Application

Run the main program using Python **3.13.5**:

```bash
python main.py
```

---

## Notes

* Ensure **MySQL server** is running before starting the application.
* The project requires **Python 3.13.5** for full compatibility.
* All GUI components are built with **Tkinter**.

---

## Features

* **Admin Panel**: Add employees, view total net profit.
* **Employee Panel**: Add customers, add goods, change discounts, handle sales transactions.
* **POS System**: Add items to cart, calculate cashback, manage payment.
* **Login System**: Separate logins for admin,
