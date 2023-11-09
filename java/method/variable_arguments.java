public class variable_arguments {
    public static void main(String[] args){
        max(10, 4, 1, -9, 8, 100, 2);
        max();
    }

    public static void max(int... nums){
        if (nums.length == 0){
            System.out.println("No arguments");
            return;
        }
        int res = nums[0];
        for (int i = 1; i < nums.length; i++){
            res = nums[i] > res ? nums[i] : res;
        }
        System.out.println("Maximum: " + res);
    }
}
