import java.util.*;

public class priorityqueue{
    public static void main(String[] args){
        /* initialization */
        PriorityQueue<Integer> nums = new PriorityQueue<>();

        /* add, offer */
        for (int i = 10; i > 0; i--){
            nums.offer(i);
        }
        print("offer:", nums);
        nums.add(0);
        print("add:", nums);

        /* iterator */
        System.out.println("");
        Iterator<Integer> iter = nums.iterator();
        while (iter.hasNext()){
            print("iter:", iter.next());
        }
        System.out.println("");

        /* element, peek */
        print("element(default):", nums.element());
        print("peek(default):", nums.peek());

        /* remove, poll */
        print("remove:", nums.remove());
        print("poll:", nums.poll());

        /* size */
        print("size:", nums.size());

        /* contains */
        print("contains 7:", nums.contains(7));
        print("contains 100:", nums.contains(100));
    }

    public static void print(String prompt, PriorityQueue<Integer> nums){
        System.out.println(String.format("%-30s %-30s", prompt, nums));
    }

    public static void print(String prompt, Object num){
        System.out.println(String.format("%-30s %-30s", prompt, num));
    }

    public static void print(String prompt, boolean contain){
        System.out.println(String.format("%-30s %-30s", prompt, contain));
    }
}