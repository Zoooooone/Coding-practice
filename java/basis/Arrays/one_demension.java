package basis.Arrays;
import java.util.Arrays;

public class one_demension {
    public static void main(String[] args){
        /* create an array */
        double[] nums = new double[10];
        for (int i = 0; i < 10; i++){
            nums[i] = Math.pow(i, 2);
        }
        System.out.println(Arrays.toString(nums));

        /* update the element in this array */
        nums[2] = 2;
        System.err.println(Arrays.toString(nums));

        /* for each */
        double even_sum = 0;
        for (double num: nums){
            if (num % 2 == 0){
                even_sum += num;
            }
        }
        System.out.println("even_sum = " + even_sum);

        /* use array as a parameter */
        double[] reversed_num = one_demension.revese_array(nums);
        System.out.println("reversed_nums: " + Arrays.toString(reversed_num));
    }

    private static double[] revese_array(double[] array){
        int n = array.length;
        double[] res = new double[n];
        for (int i = 0; i < n; i++){
            res[i] = array[n - 1 - i];
        }
        return res;
    }
}
