#ifndef DOCTOR_H
#define DOCTOR_H

#include "Person.h"

// Inherits from Person — demonstrates Inheritance & Polymorphism
class Doctor : public Person {
    string spec;

public:
    Doctor(int i, string n, int a, string s);

    void display() override;  // Polymorphism

    string getSpec();
};

#endif
