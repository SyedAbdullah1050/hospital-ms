#include "Hospital.h"
#include <fstream>
#include <iostream>

// Initialize static Singleton pointer
Hospital* Hospital::instance = nullptr;

Hospital* Hospital::getInstance() {
    if (!instance) {
        instance = new Hospital();
    }
    return instance;
}

void Hospital::addPatient(Patient p) {
    patients.push_back(p);
}

void Hospital::addDoctor(Doctor d) {
    doctors.push_back(d);
}

void Hospital::addEmergency(Patient p) {
    emergencyQueue.push(p);
}

void Hospital::showPatients() {
    show(patients);
}

void Hospital::showDoctors() {
    show(doctors);
}

void Hospital::processEmergency() {
    if (!emergencyQueue.empty()) {
        cout << "\nProcessing Emergency Patient:\n";
        emergencyQueue.front().display();
        emergencyQueue.pop();
    } else {
        cout << "No emergency patients\n";
    }
}

void Hospital::savePatients() {
    ofstream f("patients.txt");
    for (auto& p : patients) {
        f << p.getId()      << endl;
        f << p.getName()    << endl;
        f << p.getAge()     << endl;
        f << p.getDisease() << endl;
    }
    f.close();
}

void Hospital::loadPatients() {
    ifstream f("patients.txt");
    int id, age;
    string name, disease;
    while (f >> id) {
        f.ignore();
        getline(f, name);
        f >> age;
        f.ignore();
        getline(f, disease);
        patients.push_back(Patient(id, name, age, disease));
    }
    f.close();
}

void Hospital::saveDoctors() {
    ofstream f("doctors.txt");
    for (auto& d : doctors) {
        f << d.getId()   << endl;
        f << d.getName() << endl;
        f << d.getAge()  << endl;
        f << d.getSpec() << endl;
    }
    f.close();
}

void Hospital::loadDoctors() {
    ifstream f("doctors.txt");
    int id, age;
    string name, spec;
    while (f >> id) {
        f.ignore();
        getline(f, name);
        f >> age;
        f.ignore();
        getline(f, spec);
        doctors.push_back(Doctor(id, name, age, spec));
    }
    f.close();
}
