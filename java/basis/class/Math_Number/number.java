public class number{
    public static void main(String[] args){
        /* xxxvalue */
        Integer x = 5;
        Double y = 5.0;
        System.out.println("int x -> double x: " + x.doubleValue());
        System.out.println("double y -> int y: " + y.intValue());

        /* valueOf */
        Integer a = Integer.valueOf(9);
        System.out.println("a = " + a);

        /* toString */
        String x_string = x.toString();
        System.out.println(x_string.getClass());

        /* parseInt */
        String s = "68";
        int s_int = Integer.parseInt(s);
        System.out.println(s_int);
    }
}
