package practice;
public class Puppy{
    int puppyAge;
    public Puppy(String name){
        System.out.println("Puppy's name is : " + name);
    }

    public void setAge(int age){
        puppyAge = age;
    }

    public int getAge(){
        System.out.println("Puppy' s age is : " + puppyAge);
        return puppyAge;
    }

    public static void main(String[] args){
        Puppy tom = new Puppy("tom");
        System.out.println(tom.getAge());
        tom.setAge(10);
        System.out.println(tom.getAge());
    }
}

