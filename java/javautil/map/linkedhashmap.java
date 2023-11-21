import java.util.*;

public class linkedhashmap {
    public static void main(String[] args){
        HashMap<Integer, Integer> map1 = new HashMap<>();
        LinkedHashMap<Integer, Integer> map2 = new LinkedHashMap<>();
        Integer[] nums = {3, 4, 1, 2};

        for (Integer num: nums){
            map1.put(num, null);
            map2.put(num, null);
        }

        System.out.print(String.format("%-25s", "HashMap keys:"));
        for (Integer key: map1.keySet()) System.out.print(key + " ");

        System.out.println("");

        System.out.print(String.format("%-25s", "LinkedHashMap keys:"));
        for (Integer key: map2.keySet()) System.out.print(key + " ");
    }
}
