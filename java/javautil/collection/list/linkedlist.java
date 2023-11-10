import java.util.*;

public class linkedlist {
    public static void main(String[] args){
        /* initialization */
        LinkedList<Integer> list1 = new LinkedList<>();
        print("initialization", list1);
        
        /* initialization with other collections */
        ArrayList<Integer> nums = createArrayList(1, 2, 3, 4, 5);
        LinkedList<Integer> list2 = new LinkedList<>(nums);
        print("initialization with other collections", list2);
    }

    public static ArrayList<Integer> createArrayList(Integer... nums){
        ArrayList<Integer> res = new ArrayList<>();
        res.addAll(Arrays.asList(nums));
        return res;
    }

    public static void print(String prompt, LinkedList<Integer> list){
        System.out.println(String.format("%-50s %-30s", prompt, "list = " + list));
    }
}
