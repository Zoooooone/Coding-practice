package basis.Arrays;
import java.util.Arrays;

public class arrays_methods {
    public static void main(String[] args){
        int[] nums1 = {1, 5, 6, 2, 9, -1, 3, -4, -10};
        int[] nums2 = nums1;
        int[] nums3 = {0, 0};

        /* equals */
        System.out.println("nums1 = nums2: " + Arrays.equals(nums1, nums2) + "\t\tnums1 = nums3: " + Arrays.equals(nums1, nums3));
    
        /* sort */
        Arrays.sort(nums1);
        System.out.println("sorted nums1: " + Arrays.toString(nums1));

        /* binary search */
        System.out.println("index of 2: " + Arrays.binarySearch(nums1, 2) + "\t\tindex of 8: " + Arrays.binarySearch(nums1, 8));
        
        /* fill */
        Arrays.fill(nums1, 3);
        System.out.println("filled nums1: " + Arrays.toString(nums1));
    }
}
