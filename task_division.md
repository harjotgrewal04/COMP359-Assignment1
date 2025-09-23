# Task Division for COMP359 Assignment 1

## Team Members and Responsibilities

### 1. Tanisha Ahuja
- **Language**: Python
- **Components Implemented**:
  - Employee class implementation
  - Three custom sorting methods:
    - Sort by name then salary
    - Sort by salary then ID
    - Sort by name length then alphabetical
  - Interactive command-line interface
  - Performance testing and analysis
  - Visualization of performance metrics
- **Files Created**:
  ```
  src/assignment1/usingpython/
  ├── employee.py
  ├── load_employee.py
  ├── comparators.py
  ├── main.py
  ├── test_sorting.py
  ├── performance_test.py
  ├── visualize_performance.py
  └── analysis.md
  ```

### 2. Harjot Grewal
- **Language**: Java
- **Components Implemented**:
  - Employee class in Java
  - Custom sorting implementation
  - Dataset creation (1000 employees)
- **Files Created**:
  ```
  src/assignment1/
  ├── Employee.java
  ├── LoadEmployees.java
  ├── QualityCheck.java
  └── employee_dataset_1000.txt
  ```

### 3. Charvi (Pending Implementation)
- **Language**: C++
- **Components Implemented**:
- Employee class implementation in C++
- Custom sorting implementation
   - sort by Name then Salary
    - sort by salary then ID
    - sort by name length then alphebetical
- **Files created**:
  ```
src/assignment1/usingcpp/
├── Employee.hpp, Comparators.hpp, LoadEmployees.hpp
├── main.cpp, LoadEmployees.cpp, test_sorting.cpp, performance_test.cpp
└── employee_dataset_sample.txt



      
  







## Collaboration Points

1. **Dataset Consistency**
   - Using same dataset format across all implementations
   - 1000 employee records with name, ID, and salary

2. **Common Sorting Requirements**
   - Each implementation provides multiple sorting criteria
   - Focus on maintaining sort stability
   - Performance analysis for comparison

3. **Testing Strategy**
   - Unit tests for sorting functionality
   - Performance measurements
   - Cross-language comparison of results

## Work Distribution Strategy

1. **Independent Implementation**
   - Each member implements in different language
   - Ensures broad comparison of language features
   - Demonstrates different approaches to same problem

2. **Shared Resources**
   - Common dataset
   - Consistent file format
   - Unified testing approach

3. **Performance Analysis**
   - Each implementation includes performance metrics
   - Allows cross-language performance comparison
   - Different sorting algorithm analysis

## Implementation Status

- [x] Dataset Creation and Java Implementation (Harjot)
  - Employee class in Java
  - Sorting implementation
  - Dataset of 1000 employees

- [x] Python Implementation (Tanisha)
  - Employee class and sorting implementation
  - Performance testing and analysis
  - Interactive menu and visualization
  - Documentation and test cases

- [ ] C++ Implementation (Charvi)
  - Employee class in C++
  - Three custom sorting methods
  - Sorting demo with tests and performance check

## Communication and Coordination

- Using GitHub for code sharing and version control
- Repository: harjotgrewal04/COMP359-Assignment1
- Each member works in separate language-specific directories
- Cross-review of implementations for learning purposes
