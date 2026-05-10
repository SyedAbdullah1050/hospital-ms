#ifndef BILLING_H
#define BILLING_H

// Abstract Billing class — demonstrates Abstraction & Polymorphism
class Billing {
public:
    virtual double bill() = 0;  // Pure virtual

    virtual ~Billing() {}
};

// Concrete subclass — General billing
class GeneralBill : public Billing {
public:
    double bill() override;
};

// Concrete subclass — Emergency billing
class EmergencyBill : public Billing {
public:
    double bill() override;
};

#endif
