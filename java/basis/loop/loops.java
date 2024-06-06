public class loops {
    public static void main(String[] args){
        /* while loop */
        System.out.println("while loop:");
        int x = 5;
        while (x < 7){
            System.out.print(x + " ");
            x++;
        }

        /* do while loop */
        System.out.println("\ndo while loop:");
        x = 10;
        do{
            System.out.print(x + " ");
            x++;
        } while (x < 7);

        /* for loop */
        System.out.println("\nfor loop:");
        x = 5;
        for(; x < 7; x++){
            System.out.print(x + " ");
        }

        /* for each */
        System.out.println("\nfor each loop:");
        int [] nums = {1, 2, 3, 4 ,5};
        for (int num: nums){
            System.out.print(num + " ");
        }
        System.out.println();
        char [] alphabet = {'a', 'b', 'c'};
        for (char s: alphabet){
            System.out.print(s + " ");
        }
    }
}
