# Custom comparator functions that return -1, 0, or 1

def compare_by_name_then_salary(e1, e2):
    # First compare names lexicographically
    if e1.name < e2.name:
        return -1
    elif e1.name > e2.name:
        return 1
    else:
        # Tie-breaker: salary descending
        if e1.salary < e2.salary:
            return 1
        elif e1.salary > e2.salary:
            return -1
        else:
            return 0


def compare_by_salary_then_id(e1, e2):
    # First compare salary (descending)
    if e1.salary < e2.salary:
        return 1
    elif e1.salary > e2.salary:
        return -1
    else:
        # Tie-breaker: ID ascending
        if e1.emp_id < e2.emp_id:
            return -1
        elif e1.emp_id > e2.emp_id:
            return 1
        else:
            return 0


def compare_by_name_length_then_name(e1, e2):
    # Compare by length of name
    if len(e1.name) < len(e2.name):
        return -1
    elif len(e1.name) > len(e2.name):
        return 1
    else:
        # Tie-breaker: normal lexicographic
        if e1.name < e2.name:
            return -1
        elif e1.name > e2.name:
            return 1
        else:
            return 0
