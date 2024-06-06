import java.util.*;

public class stack {
    public static void main(String[] args){
        /* initialization */
        Stack<Integer> nums = new Stack<>();
        for (int i = 0; i < 10; i++){
            nums.add(i);
        }
        print("initialization", nums);

        /* empty */
        print("is empty", nums.empty());

        /* peek */
        print("peek", nums.peek());
        print("stack after peek", nums);

        /* pop */
        print("pop", nums.pop());
        print("stack after pop", nums);

        /* push */
        nums.push(10);
        print("stack after push", nums);

        /* search */
        print("the index of 5 in the stack", nums.search(5));
    }

    public static void print(String prompt, boolean is_empty){
        System.out.println(String.format("%-30s %-30s", prompt, is_empty));
    }

    public static void print(String prompt, Integer num){
        System.out.println(String.format("%-30s %-30s", prompt, num));
    }

    public static void print(String prompt, Stack<Integer> nums){
        System.out.println(String.format("%-30s %-30s", prompt, nums));
    }
}
