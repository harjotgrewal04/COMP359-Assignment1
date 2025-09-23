#include "Employee.hpp"
#include <fstream>
#include <sstream>
#include <iostream>

static std::string trim(const std::string& s) {
    size_t a = s.find_first_not_of(" \t\r\n");
    size_t b = s.find_last_not_of(" \t\r\n");
    return (a == std::string::npos) ? "" : s.substr(a, b - a + 1);
}

std::vector<Employee> loadDataset(const std::string& path) {
    std::vector<Employee> v;
    std::ifstream in(path);
    if (!in) {
        std::cerr << "Could not open file: " << path << "\n";
        return v;
    }
    std::string line;
    while (std::getline(in, line)) {
        if (trim(line).empty()) continue;
        std::stringstream ss(line);
        std::string namePart, idPart, salaryPart;

        if (!std::getline(ss, namePart, ',')) continue;
        if (!std::getline(ss, idPart, ',')) continue;
        if (!std::getline(ss, salaryPart))   continue;

        Employee e;
        e.name   = trim(namePart);
        try {
            e.id     = std::stoll(trim(idPart));
            e.salary = std::stoll(trim(salaryPart));
        } catch (...) {
            // skip bad lines
            continue;
        }
        v.push_back(e);
    }
    return v;
}


