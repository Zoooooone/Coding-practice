import java.util.*;

public class treeset_comparator{
    public static void main(String[] args){
        TreeSet<Integer> nums = new TreeSet<>(new CustomComparator());
        Integer[] elements = {1, 10, 3, 5, 6, 2, 4, 8, 7, 9};
        for (Integer e: elements){
            nums.add(e);
        }
        System.out.println(nums);
    }
}

class CustomComparator implements Comparator<Integer>{
    @Override
    public int compare(Integer n1, Integer n2) {
        return n2 - n1;
    }
}