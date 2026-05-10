#include "Doctor.h"
#include <iostream>

Doctor::Doctor(int i, string n, int a, string s)
    : Person(i, n, a), spec(s) {}

void Doctor::display() {
    cout << "Doctor: "
         << id << " | "
         << name << " | "
         << age << " | "
         << spec << endl;
}

string Doctor::getSpec() {
    return spec;
}
