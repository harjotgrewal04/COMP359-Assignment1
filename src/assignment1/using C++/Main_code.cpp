#include <algorithm>
#include <iostream>
#include <vector>
#include <iomanip>
#include "Employee.hpp"
#include "Comparators.hpp"

void printSample(const std::vector<Employee>& v, const std::string& title, int n = 10) {
    std::cout << "\n=== " << title << " (first " << n << ") ===\n";
    std::cout << std::left << std::setw(24) << "Name"
              << std::setw(12) << "ID"
              << std::setw(10) << "Salary" << "\n";
    std::cout << std::string(46, '-') << "\n";
    for (int i = 0; i < n && i < (int)v.size(); ++i) {
        std::cout << std::left << std::setw(24) << v[i].name
                  << std::setw(12) << v[i].id
                  << std::setw(10) << v[i].salary << "\n";
    }
}

int main() {
    std::vector<Employee> data = loadDataset("employees.txt");
    if (data.empty()) {
        std::cerr << "No data loaded. Is employees.txt in the hello folder?\n";
        return 1;
    }

    auto a = data;
    std::sort(a.begin(), a.end(), ByNameThenSalaryDesc{});
    printSample(a, "Sort 1: Name A->Z, tie -> Salary High->Low");

    auto b = data;
    std::sort(b.begin(), b.end(), BySalaryDescThenIdAsc{});
    printSample(b, "Sort 2: Salary High->Low, tie -> ID Low->High");

    auto c = data;
    std::sort(c.begin(), c.end(), ByNameLenThenAlpha{});
    printSample(c, "Sort 3: NameLength Short->Long, tie -> Alphabetical");

    return 0;
}

