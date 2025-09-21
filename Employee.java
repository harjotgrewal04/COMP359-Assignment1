package assignment1;
import java.util.*;

public class Employee implements Comparable<Employee>{
	
	public String employeeName;
	public int employeeID;
	public int employeePay;
	
	Employee(String employeeName, int employeeID, int employeePay){
		this.employeeName = employeeName;
		this.employeeID = employeeID;
		this.employeePay = employeePay;
	}
	public int compareTo(Employee x) {
		return x.employeePay - this.employeePay;
	
	}
	public static int compareByName(Employee e1, Employee e2) {
		return e1.employeeName.compareTo(e2.employeeName);
	}
}
//just checking

