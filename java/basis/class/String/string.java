import java.util.Arrays;

public class string {
    public static void main(String[] args){
        /* create strings */
        String s1 = "hello";
        String s2 = new String("hello");
        
        char [] chars = {'h', 'e', 'l', 'l', 'o'};
        String s3 = new String(chars);

        System.out.println("s1: " + s1);
        System.out.println("s2: " + s2);
        System.out.println("s3: " + s3);

        /* methods */
        System.out.println("\ncharAt: " + s1.charAt(0));
        System.out.println("concat: " + s1.concat(s2));
        System.out.println("equals: " + s1.equals(s3));
        System.out.println("indexOf: " + s1.indexOf("l"));
        System.out.println("lastIndexOf: " + s1.lastIndexOf("l"));
        System.out.println("length: " + s1.length());
        System.out.println("replace: " + s1.replace('l', 'x'));
        System.out.println("substring: " + s1.substring(1, 3));
        char [] s1_array = s1.toCharArray();
        System.out.println(Arrays.toString(s1_array));
        System.out.println("contains: " + s1.contains("l"));
        System.out.println("isEmpty: " + s1.isEmpty());
    }
}
