#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <string>

using namespace std;

class Person {
protected:
    int id, age;
    string name;

public:
    Person(int i, string n, int a)
        : id(i), name(n), age(a) {}

    virtual void display() = 0;

    int getId() {
        return id;
    }

    string getName() {
        return name;
    }

    int getAge() {
        return age;
    }
};

class Patient : public Person {
    string disease;

public:
    Patient(int i, string n, int a, string d)
        : Person(i, n, a), disease(d) {}

    void display() override {
        cout << "Patient: "
             << id << " | "
             << name << " | "
             << age << " | "
             << disease << endl;
    }

    string getDisease() {
        return disease;
    }
};

class Doctor : public Person {
    string spec;

public:
    Doctor(int i, string n, int a, string s)
        : Person(i, n, a), spec(s) {}

    void display() override {
        cout << "Doctor: "
             << id << " | "
             << name << " | "
             << age << " | "
             << spec << endl;
    }

    string getSpec() {
        return spec;
    }
};

class Billing {
public:
    virtual double bill() = 0;
};

class GeneralBill : public Billing {
public:
    double bill() override {
        return 500;
    }
};

class EmergencyBill : public Billing {
public:
    double bill() override {
        return 1500;
    }
};

template <typename T>
void show(vector<T>& v) {
    if (v.empty()) {
        cout << "No Data Found\n";
        return;
    }

    for (auto &x : v) {
        x.display();
    }
}

class Hospital {

    vector<Patient> patients;
    vector<Doctor> doctors;
    queue<Patient> emergencyQueue;

    static Hospital* instance;

    Hospital() {}

public:

    static Hospital* getInstance() {

        if (!instance) {
            instance = new Hospital();
        }

        return instance;
    }

    void addPatient(Patient p) {
        patients.push_back(p);
    }

    void addDoctor(Doctor d) {
        doctors.push_back(d);
    }

    void addEmergency(Patient p) {
        emergencyQueue.push(p);
    }

    void showPatients() {
        show(patients);
    }

    void showDoctors() {
        show(doctors);
    }

    void processEmergency() {

        if (!emergencyQueue.empty()) {

            cout << "\nProcessing Emergency Patient:\n";

            emergencyQueue.front().display();

            emergencyQueue.pop();
        }

        else {
            cout << "No emergency patients\n";
        }
    }
    void savePatients() {

        ofstream f("patients.txt");

        for (auto &p : patients) {

            f << p.getId() << endl;
            f << p.getName() << endl;
            f << p.getAge() << endl;
            f << p.getDisease() << endl;
        }

        f.close();
    }

    void loadPatients() {

        ifstream f("patients.txt");

        int id, age;
        string name, disease;

        while (f >> id) {

            f.ignore();

            getline(f, name);

            f >> age;
            f.ignore();

            getline(f, disease);

            patients.push_back(
                Patient(id, name, age, disease)
            );
        }

        f.close();
    }
    void saveDoctors() {

        ofstream f("doctors.txt");

        for (auto &d : doctors) {

            f << d.getId() << endl;
            f << d.getName() << endl;
            f << d.getAge() << endl;
            f << d.getSpec() << endl;
        }

        f.close();
    }
    void loadDoctors() {

        ifstream f("doctors.txt");

        int id, age;
        string name, spec;

        while (f >> id) {

            f.ignore();

            getline(f, name);

            f >> age;
            f.ignore();

            getline(f, spec);

            doctors.push_back(
                Doctor(id, name, age, spec)
            );
        }

        f.close();
    }
};

Hospital* Hospital::instance = nullptr;

int main() {

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

                h->addPatient(
                    Patient(id, name, age, disease)
                );

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

                cout << "Enter Specialization: ";
                getline(cin, spec);

                h->addDoctor(
                    Doctor(id, name, age, spec)
                );

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

                h->addEmergency(
                    Patient(id, name, age, disease)
                );

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

                Billing* b;

                if (type == 1)
                    b = new GeneralBill();

                else
                    b = new EmergencyBill();

                cout << "Generated Bill: Rs. "
                     << b->bill() << endl;

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
