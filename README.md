<p align="center">
  <img src="https://raw.githubusercontent.com/Rubinskiy/IF184202-Data-Structures/main/its.png" height="150" />
</p>

<h2 align="center">Rent4Wheels - Car Rental System</h2>

<p align="center">
  <b>Design Pattern Implementation for ER234301: Software Development</b><br>
  Final Project by:<br>
  <b>Samuel Arthur Gamalliel (5025221109)</b> & <b>Surya Prima Pradana (5025221076)</b><br>
</p>

---

## 🧭 Project Overview

**Rent4Wheels** is a simplified **car rental management system** that demonstrates core principles of **object-oriented design** and the **use of design patterns** in a real-world inspired application. It simulates key system components like users, cars, booking services, and automated notifications, implemented in **Python**.

The focus of this system is to **illustrate the Proxy and Observer design patterns**, enforcing booking permissions and decoupled notifications, respectively.

---

## 🎯 Purpose

This project was developed to:

- Demonstrate **practical design pattern applications** in software architecture
- Build a **basic modular rental system** with separate layers: models, services, patterns, and utils
- Highlight **separation of concerns**, **clean architecture**, and **expandability**
- Serve as a working prototype or educational backend for more advanced systems

---

## ✨ Features

| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| 👤 **User Verification**       | Users are classified as verified or not, controlling access to bookings     |
| 🚗 **Vehicle Listing**         | Each car is uniquely identified and contains basic info (model, ID)         |
| 📅 **Booking Service**         | Enables bookings if conditions (verification) are met                       |
| 🔐 **Proxy Pattern**           | Gatekeeps access to booking functionality                                   |
| 📣 **Observer Pattern**        | Sends notifications to users regarding booking status                       |
| 🧪 **Minimal Python Setup**   | No external libraries needed, runs with plain Python                        |

---

## 🛠️ Design Patterns Used

### 1. 🔐 **Proxy Pattern**
- **Purpose**: Protect the booking process by verifying user status
- **How**: `BookingProxy` checks if a user is verified before creating a `Booking`
- **Benefit**: Prevents unauthorized actions while keeping booking logic separate

### 2. 📣 **Observer Pattern**
- **Purpose**: Notify users when booking status changes (approved/denied)
- **How**: `Notifier` broadcasts messages to subscribed `UserObserver` instances
- **Benefit**: Decouples notification logic from booking logic, ensuring modularity

---

## 📂 Folder Structure

<details> <summary>📁 Click to expand folder structure</summary>
plaintext
Salin
Edit
rent4wheels/
├── main.py                         # Entry point for the system
├── models/                         # Core domain models
│   ├── user.py                     # User class with verification status
│   ├── vehicle.py                  # Vehicle class with unique ID & model
│   └── booking.py                  # Booking class with confirmation logic
├── patterns/                       # Design pattern implementations
│   ├── proxy.py                    # Proxy to restrict booking access
│   └── observer.py                 # Observer base and UserObserver class
├── services/                       # Business logic layer
│   └── booking_service.py         # High-level booking flow using Proxy + Observer
└── utils/                          # Utility components
    └── notifier.py                # Notification broadcaster for Observer pattern
</details>


## 📄 Example Code Walkthrough

### ✅ Booking by Verified User
```python
user = User("Alice", is_verified=True)
vehicle = Vehicle("V123", "Toyota Camry")
process_booking(user, vehicle)
```

### ❌ Booking by Unverified User
```python
user = User("Bob", is_verified=False)
vehicle = Vehicle("V123", "Toyota Camry")
process_booking(user, vehicle)
```
