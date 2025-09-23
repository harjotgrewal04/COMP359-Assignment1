import time
from functools import cmp_to_key
from src.assignment1.usingpython.load_employee import load_employees
from src.assignment1.usingpython.comparators import (
    compare_by_name_then_salary,
    compare_by_salary_then_id,
    compare_by_name_length_then_name
)

def measure_sort_performance(employees, comparator_func, sort_name):
    """Measure sorting performance for a given comparator"""
    start_time = time.time()
    sorted_employees = sorted(employees, key=cmp_to_key(comparator_func))
    end_time = time.time()
    
    duration = end_time - start_time
    print(f"\n{sort_name}:")
    print(f"Time taken: {duration:.4f} seconds")
    print(f"Number of employees: {len(employees)}")
    print(f"Average time per item: {(duration/len(employees))*1000:.4f} milliseconds")
    return sorted_employees

def main():
    # Load dataset
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(current_dir, "employee_dataset.txt")
    employees = load_employees(dataset_path)
    
    print(f"Performance Analysis for {len(employees)} employees")
    print("=" * 50)
    
    # Test all sorting methods
    sorts = [
        (compare_by_name_then_salary, "Sort by Name then Salary"),
        (compare_by_salary_then_id, "Sort by Salary then ID"),
        (compare_by_name_length_then_name, "Sort by Name Length then Alphabetical")
    ]
    
    for comparator, name in sorts:
        sorted_emps = measure_sort_performance(employees, comparator, name)
        
        # Verify sort is stable
        print("Verifying sort stability...")
        # Check first few items meet sorting criteria
        if name == "Sort by Name then Salary":
            # First few names should be in alphabetical order
            names = [emp.name for emp in sorted_emps[:5]]
            print(f"First 5 names: {names}")
            assert all(names[i] <= names[i+1] for i in range(len(names)-1))
            
        elif name == "Sort by Salary then ID":
            # First few salaries should be in descending order
            salaries = [emp.salary for emp in sorted_emps[:5]]
            print(f"First 5 salaries: {salaries}")
            assert all(salaries[i] >= salaries[i+1] for i in range(len(salaries)-1))
            
        elif name == "Sort by Name Length then Alphabetical":
            # First few names should be shortest
            lengths = [len(emp.name) for emp in sorted_emps[:5]]
            print(f"First 5 name lengths: {lengths}")
            assert all(lengths[i] <= lengths[i+1] for i in range(len(lengths)-1))
        
        print("Sort verification passed!")
        print("-" * 50)

if __name__ == "__main__":
    main()
