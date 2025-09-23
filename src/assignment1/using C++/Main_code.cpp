#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct Employee {
    string name;
    int id;
    double salary;
};

                                                                                    // 1) Sort by NAME then SALARY
struct ByNameThenSalary {
    bool operator()(const Employee& a, const Employee& b) const {
        if (a.name == b.name) return a.salary < b.salary;
        return a.name < b.name;
    }
};

                                                                                    // 2) Sort by SALARY then ID
struct BySalaryThenId {
    bool operator()(const Employee& a, const Employee& b) const {
        if (a.salary == b.salary) return a.id < b.id;
        return a.salary < b.salary;
    }
};

                                                                                    // 3) Sort by NAME LENGTH then ALPHABETICAL
struct ByNameLenThenAlpha {
    bool operator()(const Employee& a, const Employee& b) const {
        if (a.name.size() == b.name.size()) return a.name < b.name;
        return a.name.size() < b.name.size();
    }
};

// Print helper
void printSample(const vector<Employee>& v, int n = 10) {
    for (int i = 0; i < v.size() && i < n; i++) {
        cout << v[i].name << " | ID " << v[i].id
            << " | $" << v[i].salary << "\n";
    }
}

int main() {
                                                            // Small dataset hard-coded (you can expand with all 1000)
    vector<Employee> employees = {
        {"Aaliyah Carter", 824975, 96960},
        {"Aaliyah Flores", 48623, 72930},
        {"Aaliyah Gray", 837912, 87060},
        {"Aaliyah Ward", 958089, 93430},
        {"Aaliyah Wilson", 371858, 123530},
        {"Abigail Chavez", 747420, 94070},
        {"Abigail Davis", 741058, 65010},
        {"Abigail Edwards", 646239, 40850},
        {"Abigail Evans", 200659, 59800},
        {"Abigail Garcia", 667549, 85710},
        {"Aria Cruz", 479693, 37100},
        {"Camila Wilson", 96966, 40820},
        {"Dylan Carter", 501149, 41200},
        {"Carter Baker", 369074, 41310},
        {"Savannah Gomez", 288813, 42260},
        {"Jackson Morgan", 301614, 45570},
        {"Jack Rogers", 380404, 45900},
        {"Aiden Hughes", 310571, 46960},
        {"Lily Smith", 793911, 47170},
        {"Noah Lee", 847826, 112520},
        {"Noah Kim", 628094, 124090},
        {"Noah Wood", 603022, 73920},
        {"Noah Cruz", 908322, 170630},
        {"Noah Scott", 925457, 90760},
        {"Liam Hall", 969894, 90080},
        {"Liam Wood", 900908, 108750},
        {"Liam Ortiz", 469449, 97280},
        {"Liam Bailey", 950178, 169730},
        {"Liam Adams", 694024, 78920}
    };

                                                                            // 1) Sort by NAME then SALARY
    {
        auto v = employees;
        sort(v.begin(), v.end(), ByNameThenSalary{});
        cout << "\n=== Sort by NAME then SALARY ===\n";
        printSample(v, 10);
    }

                                                                              // 2) Sort by SALARY then ID
    {
        auto v = employees;
        sort(v.begin(), v.end(), BySalaryThenId{});
        cout << "\n=== Sort by SALARY then ID ===\n";
        printSample(v, 10);
    }

                                                                               // 3) Sort by NAME LENGTH then ALPHABETICAL
    {
        auto v = employees;
        sort(v.begin(), v.end(), ByNameLenThenAlpha{});
        cout << "\n=== Sort by NAME LENGTH then ALPHABETICAL ===\n";
        printSample(v, 10);
    }

    return 0;
}
