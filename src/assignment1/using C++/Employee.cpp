// test.cpp
#include <iostream>
#include <string>

struct Employee {
    std::string name;
    int id = 0;
    double salary = 0.0;

    Employee() = default;
    Employee(const std::string& n, int i, double s) : name(n), id(i), salary(s) {}
};

int main() {
    Employee e1("Alice Smith", 1, 60000.0);
    std::cout << e1.name << ", id=" << e1.id << ", salary=" << e1.salary << "\n";
    return 0;
}
