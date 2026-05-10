#ifndef PERSON_H
#define PERSON_H

#include <string>
using namespace std;

// Abstract Base Class — demonstrates Abstraction & Encapsulation
class Person {
protected:
    int id, age;
    string name;

public:
    Person(int i, string n, int a);

    virtual void display() = 0;  // Pure virtual — Abstraction

    int getId();
    string getName();
    int getAge();

    virtual ~Person() {}
};

#endif
