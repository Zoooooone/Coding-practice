import java.util.*;

public class vector{
    public static void main(String[] args){
        /* default */
        Vector<Integer> v1 = new Vector<>();
        System.out.println("v1 capacity: " + v1.capacity());

        /* with a determined size */
        Vector<Integer> v2 = new Vector<>(20);
        System.out.println("v2 capacity: " + v2.capacity());

        /* initail size + increment */
        Vector<Integer> v3 = new Vector<>(2, 3);
        for (int i = 0; i < 6; i++){
            v3.add(1);
            System.out.println("i = " + i + "\t\tv3 capacity: " + v3.capacity());
        }

        /* initial set */
        ArrayList<Integer> nums = new ArrayList<>(3);
        nums.add(1);
        nums.add(2);
        Vector<Integer> v = new Vector<>(nums);
        System.out.println("v = " + v);

        /* methods */
        
        /* add */
        Vector<Integer> v4 = new Vector<>();
        for (int i = 0; i < 8; i++){
            v4.add(i);
        }
        System.out.println(String.format("%-60s %10s", "v4 = " + v4, "capacity = " + v4.capacity()));
        
        /* add with index */
        for (int i = 0; i < 5; i++){
            v4.add(1, 100);
            System.out.println(String.format("%-60s %10s", "v4 = " + v4, "capacity = " + v4.capacity()));
        }
        
        /* contains */
        System.out.println("v4 contains 98: " + v4.contains(98));
        System.out.println("v4 contains 1: " + v4.contains(1));

        /* get */
        System.out.println("v4[2] = " + v4.get(2));

        /* remove */
        for (int i = 0; i < 6; i++){
            v4.remove(0);
        }
        System.out.println("v4 = " + v4);

        /* subList */
        System.out.println("v4[2:6] = " + v4.subList(2, 6));
    }
}
