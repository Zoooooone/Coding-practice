import java.util.*;

public class hashset_iter {
    public static void main(String[] args){
        HashSet<Integer> nums1 = new HashSet<>();
        HashSet<Integer> nums2 = new HashSet<>();

        /* initialize nums1 */
        nums1.add(1);
        nums1.add(3);
        nums1.add(2);
        nums1.add(4);

        /* initialize nums2 */
        nums2.add(3);
        nums2.add(4);
        nums2.add(1);
        nums2.add(2);

        /* iterate nums1 */
        Iterator<Integer> iter1 = nums1.iterator();
        System.out.print("iterate nums1: ");
        while (iter1.hasNext()){
            System.out.print(iter1.next() + " ");
        }

        /* iterate nums2 */
        Iterator<Integer> iter2 = nums2.iterator();
        System.out.print("\niterate nums2: ");
        while (iter2.hasNext()){
            System.out.print(iter2.next() + " ");
        }
    }
}
