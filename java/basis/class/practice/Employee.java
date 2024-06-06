package practice;
public class Employee {
    String name;
    int age;
    String position;
    double salary;

    public Employee(String name){
        this.name = name;
    }

    public void setAge(int age){
        this.age = age;
    }

    public void setPosition(String position){
        this.position = position;
    }

    public void setSalary(double salary){
        this.salary = salary;
    }

    public void printEmployee(){
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Position: " + position);
        System.out.println("Salary: " + salary);
    }
}
