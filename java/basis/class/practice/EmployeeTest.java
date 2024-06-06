package practice;
public class EmployeeTest {
    public static void main(String[] args){
        Employee tom = new Employee("Tom");
        Employee mike = new Employee("mike");

        tom.setAge(40);
        tom.setPosition("manager");
        tom.setSalary(100);
        tom.printEmployee();

        System.out.println("");

        mike.setAge(25);
        mike.setPosition("engineer");
        mike.setSalary(60);
        mike.printEmployee();
    }
}
