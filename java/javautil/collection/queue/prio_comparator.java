import java.util.Comparator;
import java.util.PriorityQueue;

public class prio_comparator {
    public static void main(String[] args){
        PriorityQueue<Integer> nums = new PriorityQueue<>(new CustomComparator());
        for (int i = 0; i < 10; i++){
            nums.offer(i);
        }
        System.out.println(String.format("%-10s %-10s", "nums:", nums));
    }
}

class CustomComparator implements Comparator<Integer>{
    @Override
    public int compare(Integer n1, Integer n2){
        if (n1 > n2){
            return -1;
        }
        else if (n1 == n2){
             return 0;
        }
        else{ 
            return 1;
        }
    }
}
