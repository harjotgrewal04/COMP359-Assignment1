import os
from src.assignment1.usingpython.employee import Employee

def load_employees(filename: str):
    employees = []

    if os.path.isabs(filename):
        filepath = filename
    else:
        base_dir = os.path.dirname(__file__)
        filepath = os.path.join(base_dir, filename)

    print(f"[DEBUG] Loading dataset from: {filepath}")

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Could not find dataset at {filepath}")

    with open(filepath, "r") as f:
        for i, line in enumerate(f):
            if i < 5:  # just show first 5 lines for debugging
                print(f"[RAW LINE {i}]: {repr(line)}")
            
            # Skip empty lines
            line = line.strip()
            if not line:
                continue
                
            # Parse the line (expected format: "name,id,salary")
            try:
                # Split on comma but limit to 3 parts to handle names with commas
                parts = line.split(",", 2)
                if len(parts) != 3:
                    raise ValueError(f"Expected 3 parts, got {len(parts)}")
                    
                name = parts[0].strip()
                emp_id = int(parts[1].strip())
                salary = int(parts[2].strip())
                
                if not name or emp_id < 0 or salary < 0:
                    raise ValueError("Invalid data: name cannot be empty, id and salary must be positive")
                
                employees.append(Employee(name, emp_id, salary))
            except (ValueError, IndexError) as e:
                print(f"Warning: Skipping invalid line {i+1}: {line} ({str(e)})")

    print(f"Successfully loaded {len(employees)} employees")
    return employees
