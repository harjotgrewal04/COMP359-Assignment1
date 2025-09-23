from functools import cmp_to_key
from src.assignment1.usingpython.load_employee import load_employees
from src.assignment1.usingpython.comparators import (
    compare_by_name_then_salary,
    compare_by_salary_then_id,
    compare_by_name_length_then_name
)

def main():
    # Load employees from dataset in same folder
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(current_dir, "employee_dataset.txt")
    employees = load_employees(dataset_path)

    while True:
        print("\nChoose sorting method:")
        print("1. Sort by Name then Salary")
        print("2. Sort by Salary then ID")
        print("3. Sort by Length of Name then Alphabetical")
        print("4. Show first 5 employees (unsorted)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            sorted_employees = sorted(employees, key=cmp_to_key(compare_by_name_then_salary))
            print(f"\nShowing all {len(sorted_employees)} employees sorted by name then salary:")
            for e in sorted_employees:
                print(e)
        
        elif choice == "2":
            sorted_employees = sorted(employees, key=cmp_to_key(compare_by_salary_then_id))
            print(f"\nShowing all {len(sorted_employees)} employees sorted by salary then ID:")
            for e in sorted_employees:
                print(e)
        
        elif choice == "3":
            sorted_employees = sorted(employees, key=cmp_to_key(compare_by_name_length_then_name))
            print(f"\nShowing all {len(sorted_employees)} employees sorted by name length then alphabetically:")
            for e in sorted_employees:
                print(e)
        
        elif choice == "4":
            print("\n=== First 5 employees (unsorted) ===")
            for e in employees[:5]:
                print(e)
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
