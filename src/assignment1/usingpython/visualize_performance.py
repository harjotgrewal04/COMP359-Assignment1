import matplotlib.pyplot as plt
import numpy as np
from functools import cmp_to_key
import time
from src.assignment1.usingpython.load_employee import load_employees
from src.assignment1.usingpython.comparators import (
    compare_by_name_then_salary,
    compare_by_salary_then_id,
    compare_by_name_length_then_name
)

def measure_sort(employees, comparator_func, num_runs=5):
    """Measure sorting time with multiple runs for accuracy"""
    times = []
    for _ in range(num_runs):
        start = time.time()
        sorted(employees, key=cmp_to_key(comparator_func))
        end = time.time()
        times.append((end - start) * 1000)  # Convert to milliseconds
    return np.mean(times), np.std(times)

def create_performance_chart(results):
    """Create a bar chart of sorting performance"""
    methods = list(results.keys())
    means = [result[0] for result in results.values()]
    stds = [result[1] for result in results.values()]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(methods, means, yerr=stds, capsize=5)
    
    # Customize the chart
    plt.title('Sorting Performance Comparison\n(Lower is Better)', pad=20)
    plt.ylabel('Time (milliseconds)')
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.4f}ms',
                ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('sorting_performance.png')
    plt.close()

def main():
    # Load data
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(current_dir, "employee_dataset.txt")
    employees = load_employees(dataset_path)
    
    # Measure performance
    results = {
        'Name then Salary': measure_sort(employees, compare_by_name_then_salary),
        'Salary then ID': measure_sort(employees, compare_by_salary_then_id),
        'Name Length': measure_sort(employees, compare_by_name_length_then_name)
    }
    
    # Print results
    print("\nDetailed Performance Analysis")
    print("=" * 50)
    for method, (mean, std) in results.items():
        print(f"\n{method}:")
        print(f"Average time: {mean:.4f} ms")
        print(f"Standard deviation: {std:.4f} ms")
        print(f"Coefficient of variation: {(std/mean)*100:.2f}%")
    
    # Create visualization
    create_performance_chart(results)
    print("\nPerformance chart saved as 'sorting_performance.png'")

if __name__ == "__main__":
    main()
