#include <iostream>
#include "Hospital.h"
#include "Billing.h"

using namespace std;

int main() {

    // Singleton pattern — get the one Hospital instance
    Hospital* h = Hospital::getInstance();

    h->loadPatients();
    h->loadDoctors();

    int ch;

    while (true) {

        cout << "\n========== HOSPITAL MANAGEMENT ==========\n";
        cout << "1. Add Patient\n";
        cout << "2. Add Doctor\n";
        cout << "3. View Patients\n";
        cout << "4. View Doctors\n";
        cout << "5. Add Emergency Patient\n";
        cout << "6. Process Emergency\n";
        cout << "7. Generate Bill\n";
        cout << "8. Exit\n";
        cout << "Enter Choice: ";
        cin >> ch;

        try {

            if (ch == 1) {

                int id, age;
                string name, disease;

                cin.ignore();

                cout << "Enter Patient ID: ";
                cin >> id;
                cin.ignore();

                cout << "Enter Patient Name: ";
                getline(cin, name);

                cout << "Enter Age: ";
                cin >> age;
                cin.ignore();

                cout << "Enter Disease: ";
                getline(cin, disease);

                if (age < 0)
                    throw "Invalid age";

                h->addPatient(Patient(id, name, age, disease));
                cout << "Patient Added Successfully\n";
            }

            else if (ch == 2) {

                int id, age;
                string name, spec;

                cin.ignore();

                cout << "Enter Doctor ID: ";
                cin >> id;
                cin.ignore();

                cout << "Enter Doctor Name: ";
                getline(cin, name);

                cout << "Enter Age: ";
                cin >> age;
                cin.ignore();

                if (age < 0)
                    throw "Invalid age";

                cout << "Enter Specialization: ";
                getline(cin, spec);

                h->addDoctor(Doctor(id, name, age, spec));
                cout << "Doctor Added Successfully\n";
            }

            else if (ch == 3) {
                cout << "\n===== PATIENTS =====\n";
                h->showPatients();
            }

            else if (ch == 4) {
                cout << "\n===== DOCTORS =====\n";
                h->showDoctors();
            }

            else if (ch == 5) {

                int id, age;
                string name, disease;

                cin.ignore();

                cout << "Enter Emergency Patient ID: ";
                cin >> id;
                cin.ignore();

                cout << "Enter Name: ";
                getline(cin, name);

                cout << "Enter Age: ";
                cin >> age;
                cin.ignore();

                cout << "Enter Disease: ";
                getline(cin, disease);

                h->addEmergency(Patient(id, name, age, disease));
                cout << "Emergency Patient Added\n";
            }

            else if (ch == 6) {
                h->processEmergency();
            }

            else if (ch == 7) {

                int type;
                cout << "1. General Bill\n";
                cout << "2. Emergency Bill\n";
                cout << "Choose Bill Type: ";
                cin >> type;

                // Polymorphism via base pointer
                Billing* b;

                if (type == 1)
                    b = new GeneralBill();
                else
                    b = new EmergencyBill();

                cout << "Generated Bill: Rs. " << b->bill() << endl;

                delete b;
            }

            else if (ch == 8) {
                h->savePatients();
                h->saveDoctors();
                cout << "Data Saved Successfully\n";
                cout << "Exiting Program...\n";
                break;
            }

            else {
                throw "Invalid choice";
            }
        }

        catch (const char* msg) {
            cout << "Error: " << msg << endl;
        }
    }

    return 0;
}
