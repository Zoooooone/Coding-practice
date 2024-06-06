public class math{
    public static void main(String[] args){
        /* ceil, floor, round, rint */
        double [] nums = {-2.5, -1.6, -1.5, -1.4, 1.4, 1.5, 1.6};
        for (double num: nums){
            double num_ceil = Math.ceil(num);
            double num_floor = Math.floor(num);
            double num_round = Math.round(num);
            double num_rint = Math.rint(num);
            
            System.out.print("num = " + num + " num_ceil = " + num_ceil);
            System.out.print(" num_floor = " + num_floor + " num_round = " + num_round);
            System.out.print(" num_rint = " + num_rint + "\n");
        }

        /* max, min */
        int a = 1, b = 2;
        System.out.println("\nmax: " + Math.max(a, b));
        System.out.println("min: " + Math.min(a, b));

        /* exp, log, pow, sqrt */
        System.out.println("\ne ^ log2 = " + Math.exp(Math.log(2)));
        System.out.println("log(e ^ 3) = " + Math.log(Math.pow(Math.E, 3)));
        System.out.println("sqrt(16) = " + Math.sqrt(16));

        /* random */
        System.out.println("\nrandom number: " + Math.random());
    }
}
