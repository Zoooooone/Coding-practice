public class character{
    public static void main(String[] args){
        Character [] chars = {'A', 'a', '1', ' '};
        for (Character c: chars){
            character.print_res(c);
        }
    }

    private static void print_res(Character c){
        System.out.print("\n\n" + c + "\tis letter: " + Character.isLetter(c));
        System.out.print("\tis digit: " + Character.isDigit(c));
        System.out.print("\tis white space: " + Character.isWhitespace(c));
        System.out.print("\tis uppercase: " + Character.isUpperCase(c));
        System.out.print("\tis lowercase: " + Character.isLowerCase(c));
        System.out.print("\tto uppercase: " + Character.toUpperCase(c));
        System.out.print("\tto lowercase: " + Character.toLowerCase(c));
        System.out.print("\tto string: " + Character.toString(c).getClass());
    }
}
