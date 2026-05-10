#ifndef HOSPITAL_H
#define HOSPITAL_H

#include <vector>
#include <queue>
#include <iostream>
#include "Patient.h"
#include "Doctor.h"

// Template function — must stay in .h because templates
// cannot be split across .h and .cpp
template <typename T>
void show(vector<T>& v) {
    if (v.empty()) {
        cout << "No Data Found\n";
        return;
    }
    for (auto& x : v) {
        x.display();
    }
}

// Singleton Design Pattern — only one Hospital instance allowed
class Hospital {

    vector<Patient> patients;   // Composition: Hospital owns Patients
    vector<Doctor>  doctors;    // Composition: Hospital owns Doctors
    queue<Patient>  emergencyQueue;

    static Hospital* instance;  // Static member — Singleton

    Hospital() {}               // Private constructor — Singleton

public:

    // Singleton: returns the one global instance
    static Hospital* getInstance();

    void addPatient(Patient p);
    void addDoctor(Doctor d);
    void addEmergency(Patient p);

    void showPatients();
    void showDoctors();

    void processEmergency();

    void savePatients();
    void loadPatients();

    void saveDoctors();
    void loadDoctors();
};

#endif
