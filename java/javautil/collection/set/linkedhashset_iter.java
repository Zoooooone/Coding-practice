import java.util.*;

public class linkedhashset_iter {
    public static void main(String[] args){
        /* initialization */
        LinkedHashSet<Integer> nums1 = new LinkedHashSet<>();
        Integer[] elements = {1, 3, 2, 4, 10, 6, 5};
        for (Integer e: elements){
            nums1.add(e);
        }

        /* iteration */
        Iterator<Integer> iter = nums1.iterator();
        System.out.print("iter: ");
        while (iter.hasNext()){
            System.out.print(iter.next() + " ");
        }
    }
}
