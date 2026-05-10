#include "Person.h"

Person::Person(int i, string n, int a)
    : id(i), name(n), age(a) {}

int Person::getId() {
    return id;
}

string Person::getName() {
    return name;
}

int Person::getAge() {
    return age;
}
