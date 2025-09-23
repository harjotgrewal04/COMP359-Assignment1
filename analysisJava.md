# Applying Analysis Framework to Custom Sorting

## 1. Algorithm Design Choice

### 1.1 Java Implementation Approach
- Included java comparator and comparable interfaces.

### 1.2 Sorting Criteria Analysis

#### a) Sort by Name then Salary
- **Primary Key**: Name (alphabetical)
- **Secondary Key**: Salary (descending)
- **Use Case**: A business/company may need to locate a certain employee without knowing their employee ID.
- **Time Complexity**:
- **Space Complexity**:

#### b) Sort by Salary then Name
- **Primary Key**: Salary (descending)
- **Secondary Key**: Name (alphabetical)
- **Use Case**: An employer may need to view the highest paid workers or copmare productivity alongside salary. 
- **Time Complexity**:
- **Space Complexity**:


## 2. Comparison with Python & C++ Implementation

### 2.1 Language-Specific Differences
- **Java**:
  
- **Python**:
  
### 2.2 Performance Analysis

#### 2.2.1 Empirical Results (Dataset of 1000 employees)
1. **Sort by Name then Salary**:
   
2. **Sort by Salary then ID**:

#### 2.2.2 Analysis of Results


#### 2.2.3 Language Comparison

## 3. Design Decisions

### 3.1 Why Custom Comparators?

### 3.2 Why Interactive Menu?

## 4. Future Improvements

### 4.1 Potential Enhancements

### 4.2 Performance Optimization Opportunities

## 5. Conclusion
