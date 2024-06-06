public class stringbuilder{
    public static void main(String[] args){
        StringBuilder s = new StringBuilder("llllllllllllllllllkk");
        System.out.println(String.format("%-20s %10s", "original string:", s));
        stringbuilder.print("append: ", s.append("666666666"));
        stringbuilder.print("reverse: ", s.reverse());
        stringbuilder.print("delete: ", s.delete(4, 13));
        stringbuilder.print("insert: ", s.insert(2, "xxxxxx"));
        stringbuilder.print("replace: ", s.replace(0, 11, "oooooooooooooo"));
    }
    
    private static void print(String str, StringBuilder s){
        System.out.println(String.format("%-20s %10s", str, s));
    }
}