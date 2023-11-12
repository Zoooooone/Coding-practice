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

        System.out.println();

        /* add */
        list2.add(5, 6);
        print("add", list2);
        list2.addFirst(0);
        print("add first 0", list2);
        list2.addLast(7);
        print("add last 7", list2);
        
        /* remove */
        list2.remove(2);
        print("remove element in index 2", list2);
        list2.removeFirst();
        print("remove first", list2);
        list2.removeLast();
        print("remove last", list2);

        /* get */
        print("get index 3", list2.get(3));
        print("get first", list2.getFirst());
        print("get last", list2.getLast());

        /* set */
        list2.set(2, 10);
        print("set element in index 2 to 10", list2);

        /* size */
        print("size of list", list2.size());
    }

    public static ArrayList<Integer> createArrayList(Integer... nums){
        ArrayList<Integer> res = new ArrayList<>();
        res.addAll(Arrays.asList(nums));
        return res;
    }

    public static void print(String prompt, LinkedList<Integer> list){
        System.out.println(String.format("%-50s %-30s", prompt, "list = " + list));
    }

    public static void print(String prompt, Integer num){
        System.out.println(String.format("%-50s %-30s", prompt, "num = " + num));
    }
}
