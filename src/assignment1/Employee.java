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
		int verdict1 = x.employeePay - this.employeePay;
		if(verdict1 !=0 ) {
			return verdict1;
		}
		return x.employeeName.compareTo(this.employeeName);
	
	}
	public static int compareByName(Employee e1, Employee e2) {
		int verdict2 = e1.employeeName.compareTo(e2.employeeName);
		if(verdict2 != 0) {
			return verdict2;
		}
		return e2.employeePay - e1.employeePay;
	}
}

