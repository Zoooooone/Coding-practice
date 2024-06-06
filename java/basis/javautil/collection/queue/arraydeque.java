import java.util.*;

public class arraydeque {
    public static void main(String[] args){
        /* initialization */
        ArrayDeque<Integer> nums = new ArrayDeque<>();
        nums.add(0);
        print("initial arrayqueue:", nums);
        System.out.println("");
        
        /* add */
        nums.add(1);
        print("add 1:", nums);
        nums.addFirst(2);
        print("addFirst 2:", nums);
        nums.addLast(3);
        print("addLast 3:", nums);
        System.out.println("");

        /* offer */
        nums.offer(4);
        print("offer 4:", nums);
        nums.offerFirst(5);
        print("offerFirst 5:", nums);
        nums.offerLast(6);
        print("offerLast 6:", nums);
        System.out.println("");

        Iterator<Integer> iter = nums.iterator();
        while (iter.hasNext()){
            print("iter:", iter.next());
        }
        System.out.println("");

        /* get */
        print("getFirst:", nums.getFirst());
        print("getLast:", nums.getLast());
        System.out.println("");

        /* peek */
        print("peek:", nums.peek());
        print("peekFirst:", nums.peekFirst());
        print("peekLast:", nums.peekLast());
        System.out.println("");

        /* remove */
        print("remove:", nums.remove());
        print("removeFirst:", nums.removeFirst());
        print("removeLast:", nums.removeLast());
        System.out.println("");

        /* poll */
        print("poll:", nums.poll());
        print("pollFirst:", nums.pollFirst());
        print("pollLast:", nums.pollLast());
    }

    public static void print(String prompt, ArrayDeque<Integer> nums){
        System.out.println(String.format("%-20s %-30s", prompt, nums));
    }

    public static void print(String prompt, Integer num){
        System.out.println(String.format("%-20s %-30s", prompt, num));
    }
}
