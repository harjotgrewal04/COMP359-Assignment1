package assignment1;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
public class LoadEmployees {

	public static ArrayList<Employee> loadEmployees() throws FileNotFoundException, IOException{
		ArrayList<Employee> list = new ArrayList<>();
		BufferedReader br = new BufferedReader(new FileReader("src/assignment1/employee_dataset_1000.txt"));
		String line;
		while((line = br.readLine()) != null) {
			String[] data = line.split(",");
			String employeeName = data[0].trim();
			int employeeID = Integer.parseInt(data[1].trim());
			int employeePay = Integer.parseInt(data[2].trim());
			Employee emp = new Employee(employeeName, employeeID, employeePay);
			list.add(emp);
		}
		
		
		br.close();
		return list;
	}

}
