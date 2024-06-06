import java.util.*;

public class treeset {
    public static void main(String[] args){
        /* initialization */
        TreeSet<Integer> nums = new TreeSet<>();
        Integer[] elements = {1, 10, 4, 2, 3, 8, 7, 5, 9, 6};
        for (Integer e: elements){
            nums.add(e);
        }
        print("nums:", nums);
        System.out.println("");

        /* first */
        print("first:", nums.first());

        /* last */
        print("last:", nums.last());
        System.out.println("");

        /* higher & ceiling*/
        print("higher:", nums.higher(9));
        print("ceiling:", nums.ceiling(9));

        /* lower & floor */
        print("lower:", nums.lower(9));
        print("floor:", nums.floor(9));
        System.out.println("");

        /* poll */
        print("pollfirst:", nums.pollFirst());
        print("nums:", nums);
        print("polllast:", nums.pollLast());
        print("nums:", nums);
        System.out.println("");

        /* headset */
        print("headset 5:", nums.headSet(5));
        print("headset 5 true:", nums.headSet(5, true));
        System.out.println("");

        /* tailset */
        print("tailset 6:", nums.tailSet(6));
        print("tailset 6 false:", nums.tailSet(6, false));
        System.out.println("");

        /* subset */
        print("subset 3 7:", nums.subSet(3, 7));
        print("subset 3 false 7 false:", nums.subSet(3, false, 7, false));
        print("subset 3 true 7 true:", nums.subSet(3, true, 7, true));
    }

    public static void print(String prompt, TreeSet<Integer> nums){
        System.out.println(String.format("%-25s %-20s", prompt, nums));
    }   

    public static void print(String prompt, int num){
        System.out.println(String.format("%-25s %-20s", prompt, num));
    }

    public static void print(String prompt, SortedSet<Integer> nums){
        System.out.println(String.format("%-25s %-20s", prompt, nums));
    }
}
