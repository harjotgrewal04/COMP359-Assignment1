package assignment1;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.IOException;

public class QualityCheck {
	public static void main(String[] args) throws FileNotFoundException, IOException{
		long startTime = System.nanoTime();
		Scanner sc = new Scanner(System.in);
		int choice;
		ArrayList<Employee> list = LoadEmployees.loadEmployees();
		System.out.println("If you would like the list to be sorted by name please enter '1' or if you would like by income/pay please enter 2:" );
		choice = sc.nextInt();
		if(choice ==1) {
			Collections.sort(list, Employee::compareByName);
			System.out.println("Employees sorted by name below: ");
			for(Employee x : list)
				System.out.println(x.employeeName + " " + x.employeeID + " " + x.employeePay);
		}
		else if(choice == 2) {
		Collections.sort(list,Employee::compareTo);
		System.out.println("Employees are sorted by pay/income below: ");
		for(Employee x : list)
			System.out.println(x.employeeName + " " + x.employeeID + " " + x.employeePay);
		}else{
			System.out.println("Error, please enter a correct choice.");
			}
		sc.close();
		long endTime = System.nanoTime();
		long duration = (endTime - startTime)/1000000;
		System.out.println("Time taken: " + duration + " miliseconds");
	}
}