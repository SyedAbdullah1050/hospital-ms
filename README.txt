========================================
  Hospital Management System
  CT-260 Object Oriented Programming
  NED University — Spring 2026
========================================

--- HOW TO COMPILE ---

Using g++ (recommended):
  g++ main.cpp Person.cpp Patient.cpp Doctor.cpp Billing.cpp Hospital.cpp -o hospital

Then run:
  ./hospital          (Linux/Mac)
  hospital.exe        (Windows)

--- PROBLEM DOMAIN ---

A console-based Hospital Management System that manages patients,
doctors, emergency queues, and billing. Data is persisted to text
files between sessions.

--- IMPLEMENTED OOP FEATURES ---

1. Encapsulation    — All class data is private/protected; accessed via getters
2. Inheritance      — Patient and Doctor inherit from abstract Person base class
3. Polymorphism     — display() overridden in Patient and Doctor;
                      bill() overridden in GeneralBill and EmergencyBill
4. Abstraction      — Person and Billing are abstract classes with pure virtual functions
5. Templates        — show<T>() is a function template that works for any displayable vector
6. STL Containers   — vector<Patient>, vector<Doctor>, queue<Patient> used
7. Exception Handling — try/catch/throw for invalid age and invalid menu choice
8. File I/O         — Patients and Doctors saved/loaded from patients.txt and doctors.txt
9. Design Pattern   — Singleton pattern used in Hospital class (one instance only)
10. Static Member   — Hospital::instance is a static data member

--- FILE STRUCTURE ---

Person.h / Person.cpp       — Abstract base class
Patient.h / Patient.cpp     — Patient (inherits Person)
Doctor.h / Doctor.cpp       — Doctor (inherits Person)
Billing.h / Billing.cpp     — Abstract Billing + GeneralBill + EmergencyBill
Hospital.h / Hospital.cpp   — Singleton Hospital manager + show<T> template
main.cpp                    — Entry point and menu
