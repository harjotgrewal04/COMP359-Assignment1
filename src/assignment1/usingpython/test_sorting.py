import unittest
from functools import cmp_to_key
import os
from src.assignment1.usingpython.employee import Employee
from src.assignment1.usingpython.load_employee import load_employees
from src.assignment1.usingpython.comparators import (
    compare_by_name_then_salary,
    compare_by_salary_then_id,
    compare_by_name_length_then_name,
)

class TestEmployeeSorting(unittest.TestCase):

    def setUp(self):
        # Small dataset for unit tests
        self.employees = [
            Employee("Alice Smith", 200, 60000),
            Employee("Bob Jones", 150, 75000),
            Employee("Alice Smith", 300, 80000),
            Employee("Charlie Brown", 100, 75000),
        ]

    def test_compare_by_name_then_salary(self):
        sorted_list = sorted(self.employees, key=cmp_to_key(compare_by_name_then_salary))
        self.assertEqual(sorted_list[0].emp_id, 300)
        self.assertEqual(sorted_list[1].emp_id, 200)

    def test_compare_by_salary_then_id(self):
        sorted_list = sorted(self.employees, key=cmp_to_key(compare_by_salary_then_id))
        self.assertEqual(sorted_list[0].salary, 80000)
        self.assertEqual(sorted_list[1].emp_id, 100)

    def test_compare_by_name_length_then_name(self):
        sorted_list = sorted(self.employees, key=cmp_to_key(compare_by_name_length_then_name))
        self.assertEqual(sorted_list[0].name, "Bob Jones")

    def test_integration_with_real_dataset(self):
        employees = load_employees("employee_dataset.txt")
        self.assertGreater(len(employees), 0, "Dataset should not be empty")

        sorted_by_name = sorted(employees, key=cmp_to_key(compare_by_name_then_salary))
        sorted_by_salary = sorted(employees, key=cmp_to_key(compare_by_salary_then_id))

        self.assertEqual(len(employees), len(sorted_by_name))
        self.assertEqual(len(employees), len(sorted_by_salary))



if __name__ == "__main__":
    unittest.main()
