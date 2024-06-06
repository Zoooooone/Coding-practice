public class overload{
    public static void main(String[] args){
        print(max(1, 3));
        print(max(4.5, 9.3));
    }

    public static int max(int n1, int n2){
        return n1 > n2 ? n1 : n2;
    }

    public static double max(double n1, double n2){
        return n1 > n2 ? n1 : n2;
    }

    public static void print(int n){
        System.out.println(n);
    }

    public static void print(double n){
        System.out.println(n);
    }
}