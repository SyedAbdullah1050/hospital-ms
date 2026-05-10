#include "Patient.h"
#include <iostream>

Patient::Patient(int i, string n, int a, string d)
    : Person(i, n, a), disease(d) {}

void Patient::display() {
    cout << "Patient: "
         << id << " | "
         << name << " | "
         << age << " | "
         << disease << endl;
}

string Patient::getDisease() {
    return disease;
}
