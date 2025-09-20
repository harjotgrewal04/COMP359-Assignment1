import java.util.*;
public class Employee implements Comparable<Employee> {
	
	String employeeName;
	int employeeID;
	int employeePay;
	
	Employee(String employeeName, int employeeID, int employeePay){
		this.employeeName = employeeName;
		this.employeeID = employeeID;
		this.employeePay = employeePay;
	}
	public int compareTo(Employee x) {
		return x.employeePay - this.employeePay;
	}
	
	// Static method to compare by name
	public static int compareByName(Employee e1, Employee e2) {
		return e1.employeeName.compareTo(e2.employeeName);
	}
}

class QualityCheck{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		ArrayList<Employee> list = new ArrayList<Employee>();
		list.add(new Employee("Ryan",3016,37850));
		list.add(new Employee("Alex",5029,46750));
		list.add(new Employee("Amy",4185,42630));
		list.add(new Employee("James",2394,39620));
		
		System.out.println("How would you like to sort the employees?");
		System.out.println("1. By pay rate (highest to lowest)");
		System.out.println("2. By name (alphabetical)");
		System.out.print("Enter your choice (1 or 2): ");
		
		int choice = scanner.nextInt();
		
		if (choice == 1) {
			// Sort by pay rate (using the compareTo method)
			Collections.sort(list);
			System.out.println("\nEmployees sorted by pay rate (highest to lowest):");
		} else if (choice == 2) {
			// Sort by name using lambda expression with static method
			Collections.sort(list, (e1, e2) -> Employee.compareByName(e1, e2));
			System.out.println("\nEmployees sorted by name (alphabetical):");
		} else {
			System.out.println("Invalid choice. Sorting by pay rate by default.");
			Collections.sort(list);
			System.out.println("\nEmployees sorted by pay rate (highest to lowest):");
		}
		
		for(Employee x : list)
			System.out.println(x.employeeName + " " + x.employeeID + " " + x.employeePay);
		
		scanner.close();
	}
}
