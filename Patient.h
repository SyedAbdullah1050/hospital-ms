#ifndef PATIENT_H
#define PATIENT_H

#include "Person.h"

// Inherits from Person — demonstrates Inheritance & Polymorphism
class Patient : public Person {
    string disease;

public:
    Patient(int i, string n, int a, string d);

    void display() override;  // Polymorphism

    string getDisease();
};

#endif
