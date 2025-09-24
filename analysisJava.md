# Applying Analysis Framework to Custom Sorting

## 1. Algorithm Design Choice

### 1.1 Java Implementation Approach
- Included java comparator and comparable interfaces.
- Took in user input for choice and variability. 

### 1.2 Sorting Criteria Analysis

#### a) Sort by Name then Salary
- **Primary Key**: Name (alphabetical)
- **Secondary Key**: Salary (descending)
- **Use Case**: A business/company may need to locate a certain employee without knowing their employee ID.
- **Time Complexity**:O(n log n)
- **Space Complexity**:O(n)

#### b) Sort by Salary then Name
- **Primary Key**: Salary (descending)
- **Secondary Key**: Name (alphabetical)
- **Use Case**: An employer may need to view the highest paid workers or copmare productivity alongside salary. 
- **Time Complexity**:O(n log n)
- **Space Complexity**:O(n)

## 2. Comparison with Python & C++ Implementation

### 2.1 Language-Specific Differences
- **Java**:
  - Uses the compare() method to specify rules
  - Sorting algorithm is Timsort (modified version of mergesort)
  - Allows flexibilty & maintainability
  
- **Python**:
  - Also uses Timsort (modified version of mergesort)
  - Sort algorithms are stable

- **C++**:
  - Uses std::sort with a custom comparator
  - Uses Introsort a hybrid algorithm combining a couple others
  
### 2.2 Performance Analysis

#### 2.2.1 Empirical Results (Dataset of 1000 employees)
1. **Sort by Name then Salary**:
   - Execution Time: 0.004214375 seconds
   - About 0.00000421437 per item
   
2. **Sort by Salary then ID**:
   - Execution Time: 0.003463833 seconds
   - About 0.00000346383 per item

#### 2.2.2 Analysis of Results
- Name Sorting is quiet slower than sorting by salary
- Salary is much quicker as it only needs to compare two values
- Some strings can be a lot longer than others

#### 2.2.3 Language Comparison

## 3. Design Decisions

### 3.1 Why Custom Comparators?
- Allows you to specify how to order certain objects
- Also allows you to compare objects from a class without editing the source code
- Can use multiple sorting techniques and define them how we would like

### 3.2 Why Interactive Menu?
- Allows user to decide which way they may want it sorted
- Can split up the sorting rules to test efficieny
- Allows for further modifications

## 4. Future Improvements

### 4.1 Potential Enhancements
- Using UUID which is used an unique identifier for objects and data by using a 128-bit number to increase the amount of combinations
- Creating a larger real-world dataset to test efficiency. 
- Better display output of order or dividing into better sections (Percentiles)

### 4.2 Performance Optimization Opportunities
- Using java's built in parallelSort()
- Using a more sorted list or a list which is almost sorted

## 5. Conclusion
To sum up, the implementation created in java uses custom comparators for sorting the employees. The interactive menu allows the user or the employer in this case to decide how they would like to order these employees. Alongside each comparing method has its own tie breaker, when the same name is provided it will use the salary and when it has the same salary it will use the ordering of the name. Overall, this implementation demonstrates how custom sorting and the comparator and comparable interfaces are used in java. 

