public class type_conversion{
    public static void main(String[] args){
        /* explicit conversion */
        int i = 128;
        byte b = (byte) i;
        System.err.println("explicit conversion: int -> byte, b = " + b);

        /* float -> int */
        System.out.println("double -> int: 23.7 = " + (int) 23.7);
        System.out.println("float -> int, -45.89f = " + (int) -45.89f);

        char c1 = 'a';
        int i1 = c1;
        System.out.println("char -> int, i1 = " + i1);
        
        char c2 = 'A';
        int i2 = c2 + 1;
        System.out.println("char -> int, i2 = " + i2);
    }
}