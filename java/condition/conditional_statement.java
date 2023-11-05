import java.util.Scanner;

public class conditional_statement {
    public static void main(String[] args){
        /* if else */
        boolean flag = false;
        if (!flag){
            System.out.println("yes!");
        } else {
            System.out.println("no!");
        }

        /* if else if else */
        int x = 0;
        for (; x < 20; x++){
            if (x % 4 == 0){
                System.out.print("a ");
            } else if (x % 4 == 1){
                System.out.print("b ");
            } else if (x % 4 == 2){
                System.out.print("c ");
            } else{
                System.out.print("d ");
            }
        }

        /* switch case */
        Scanner scanner = new Scanner(System.in);
        System.out.print("\nday = ");
        if (scanner.hasNextInt()){
            int day = scanner.nextInt();

            switch (day){
                case 1:
                    System.out.println("Monday");
                    break;
                case 2:
                    System.out.println("Tuesday");
                    break;
                case 3:
                    System.out.println("Wednesday");
                    break;
                case 4:
                    System.out.println("Thursday");
                    day += 1;
                    break;
                case 5:
                    System.out.println("Friday");
                    break;
                case 6:
                    System.out.println("Saturday");
                    break;
                case 7:
                    System.out.println("Sunday");
                    break;
                default:
                    System.out.println("Wrong input!");
            }
            System.out.println("\nday = " + day);
        }
        scanner.close();
    }
}
