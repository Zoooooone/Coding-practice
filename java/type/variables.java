public class variables {
    String instance_num = "instance variable";
    static final double PI = 3.14;

    public static void cal_sum(){
        int x = 10;
        int y = 15;
        System.out.println("sum: " + (x + y));
    }

    public static void cal_sum_2(int p, int q){
        System.out.println("p + q = " + (p + q));
    }

    public static void main(String[] args){
        /* local variable */
        for (int i = 0; i < 5; i++){
            System.out.print(i + " ");
        }
        // System.out.println(i);  i will not be stored after for loop
        
        // System.out.println(x);  x will not be stored out of the cal_sum block
        System.out.print("\n");
        cal_sum();


        /* instance variable */
        // System.out.println(instance_num); instance_num can not be accessed without a object
        variables obj = new variables();
        System.out.println(obj.instance_num); 
        
        
        /* class variable */
        System.out.println(PI);


        /* parameters */
        cal_sum_2(1, 2);
        // System.out.println(p); p can not be accessed out of the method
    }
}
