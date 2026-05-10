# 🏥 MediCore — Advanced Hospital Management System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hospital-ms-ned.streamlit.app)

> **CT-260 Object Oriented Programming | NED University of Engineering & Technology | Spring 2026**

---

## 📌 Project Overview

MediCore is a fully functional **Hospital Management System** built as part of the CT-260 OOP course. It demonstrates core Object-Oriented Programming principles through a real-world healthcare application.

---

## 🚀 Live Demo

🔗 **[Click here to open the live app](https://hospital-ms-ned.streamlit.app)**

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧑‍⚕️ Patient Management | Register, view, and delete patients |
| 👨‍⚕️ Doctor Management | Register, view, and delete doctors |
| 🚨 Emergency Queue | FIFO priority queue for emergency patients |
| 💳 Billing System | General (Rs.500) and Emergency (Rs.1500) bills |
| 💾 Data Persistence | Auto-saves to JSON files |
| 📊 Dashboard | Live stats and recent records overview |

---

## 🧠 OOP Concepts Demonstrated

| Concept | Implementation |
|---|---|
| **Encapsulation** | Private/protected members with public getters |
| **Inheritance** | Patient, Doctor inherit from abstract Person |
| **Polymorphism** | Virtual display() and bill() functions |
| **Abstraction** | Abstract Person and Billing base classes |
| **Singleton** | Hospital class — only one instance |
| **Templates** | show<T>() function template |
| **STL** | vector, queue containers |
| **Exception Handling** | try/catch/throw for invalid inputs |
| **File I/O** | Save and load records from files |

---

## 🗂️ Project Structure
hospital/
├── Person.h / Person.cpp        # Abstract base class
├── Patient.h / Patient.cpp      # Patient (inherits Person)
├── Doctor.h / Doctor.cpp        # Doctor (inherits Person)
├── Billing.h / Billing.cpp      # Abstract Billing + subclasses
├── Hospital.h / Hospital.cpp    # Singleton Hospital manager
├── main.cpp                     # Entry point
└── README.txt                   # Compile instructions
---

## ⚙️ How to Run C++ Console App

```bash
g++ main.cpp Person.cpp Patient.cpp Doctor.cpp Billing.cpp Hospital.cpp -o hospital
./hospital
```

---

## 🌐 How to Run Streamlit Web App

```bash
pip install streamlit
streamlit run app.py
```

---

## 👥 Team Members

| Name | Roll Number | Contribution |
| Ahmed Raza | CT-25277 | OOP Design, C++ Implementation |
| Syed Abdullah Hussain |  CT-25283 | GUI, Streamlit App |
| Muhammad Anas |  CT-25298 | Report, UML Diagram |

---

## 🏫 Course Information

- **Course:** CT-260 Object Oriented Programming
- **University:** NED University of Engineering & Technology
- **Department:** Computer Science & Information Technology
- **Semester:** Spring 2026
