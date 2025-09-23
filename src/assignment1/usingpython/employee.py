class Employee:
    def __init__(self, name: str, emp_id: int, salary: int):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def __repr__(self):
        return f"{self.name}, {self.emp_id}, {self.salary}"
