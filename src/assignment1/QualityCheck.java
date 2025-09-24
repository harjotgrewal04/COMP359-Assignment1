package assignment1;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.IOException;

public class QualityCheck {
	public static void main(String[] args) throws FileNotFoundException, IOException{
		Scanner sc = new Scanner(System.in);
		int choice;
		ArrayList<Employee> list = LoadEmployees.loadEmployees();
		System.out.println("If you would like the list to be sorted by name please enter '1' or if you would like by income/pay please enter 2:" );
		choice = sc.nextInt();
		if(choice == 1) {
			double startTime = System.nanoTime();
			Collections.sort(list, Employee::compareByName);
			double endTime = System.nanoTime();
			double duration = (endTime - startTime)/1000000000;
			System.out.println("Employees sorted by name below: ");
			for(Employee x : list)
				System.out.println(x.employeeName + " " + x.employeeID + " " + x.employeePay);
			
			System.out.println("Time taken: " + duration + " seconds");

		}
		else if(choice == 2) {
			double startTime = System.nanoTime();
		Collections.sort(list,Employee::compareTo);
		double endTime = System.nanoTime();
		double duration = (endTime - startTime)/1000000000;
		System.out.println("Employees are sorted by pay/income below: ");
		for(Employee x : list)
			System.out.println(x.employeeName + " " + x.employeeID + " " + x.employeePay);
		System.out.println("Time taken: " + duration + " seconds");

		}else{
			System.out.println("Error, please enter a correct choice.");
			}
		}
		
	}
