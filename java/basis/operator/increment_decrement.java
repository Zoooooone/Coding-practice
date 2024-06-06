package operator;
public class increment_decrement {
    public static void main(String[] args){
        int x = 20;
        System.out.println(++x);  // ++ first, then print x
        System.out.println(x++);  // print x first, then ++
        System.out.println(x);    
    }
}
