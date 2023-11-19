import java.util.*;

public class hashset{
    public static void main(String[] args){
        /* initialization */
        HashSet<Integer> nums1 = new HashSet<>();
        HashSet<Integer> nums2 = new HashSet<>();
        HashSet<Integer> res = new HashSet<>();
        Integer[] elements = {1, 9, 5, 6, 0, 2, 7, 3, 8, 4};

        for (Integer e: elements){
            nums1.add(e);
            if (e % 2 == 0){
                nums2.add(e);
            }
        }
        print("nums1:", nums1);
        print("nums2:", nums2);
        System.out.println("");

        /* add */
        nums1.add(3);
        nums2.add(3);
        print("add 3 to nums1:", nums1);
        print("add 3 to nums2:", nums2);

        /* remove */
        nums1.remove(4);
        print("remove 4 from nums1:", nums1);
        
        printBlank();

        print("nums1:", nums1);
        print("nums2:", nums2);
        System.out.println("");

        /* union */
        res.addAll(nums1);
        res.addAll(nums2);
        print("nums1 | nums2:", res);
        res.clear();

        /* intersection */
        res.addAll(nums1);
        res.retainAll(nums2);
        print("nums1 & nums2:", res);
        res.clear();

        /* difference */
        res.addAll(nums1);
        res.removeAll(nums2);
        print("nums1 - nums2:", res);
        res.clear();

        printBlank();

        /* isempty */
        print("isempty:", res.isEmpty());

        /* size */
        print("nums1 size:", nums1.size());

        /* contains */
        print("nusm1 contains 12:", nums1.contains(12));
        print("nums1 contains 1:", nums1.contains(1));

        printBlank();

        /* iterate */
        Iterator<Integer> iter = nums1.iterator();
        System.out.print("iterate: ");
        while (iter.hasNext()){
            System.out.print(iter.next() + " ");
        }
    }

    public static void print(String prompt, HashSet<Integer> nums){
        System.out.println(String.format("%-25s %-30s", prompt, nums));
    }

    public static void print(String prompt, boolean res){
        System.out.println(String.format("%-25s %-30s", prompt, res));
    }

    public static void print(String prompt, int num){
        System.out.println(String.format("%-25s %-30s", prompt, num));
    }

    public static void printBlank(){
        System.out.println("");
        System.out.println("------------------");
        System.out.println("");
    }
}
