import java.util.*;

public class arraylist {
    public static void main(String[] args){
        /* initialize */
        ArrayList<String> S = new ArrayList<>();
        String[] s = {"hello", "good", "bad", "happy", "art"};
        for (String element: s){
            S.add(element);
        }
        print("initialize", S);

        /* add */
        S.add("code");
        print("default add", S);
        S.add(0, "ok");
        print("add using index 0", S);

        /* remove */
        S.remove("hello");
        print("remove 'hello'", S);
        S.remove(3);
        print("remove using index 3", S);

        /* get */
        print("get index 2", S.get(2));

        /* set */
        S.set(3, "science");
        print("set", S);

        /* sort */
        S.sort(null);
        print("sort", S);

        /* size */
        print("size", S.size());

        /* subList */
        print("subList", S.subList(1, 4));
    }

    public static void print(String prompt, ArrayList<String> x){
        System.out.println(String.format("%-30s %-20s", prompt, " S = " + x));
    }

    public static void print(String prompt, String x){
        System.out.println(String.format("%-30s %-20s", prompt, " string = " + x));
    }

    public static void print(String prompt, int x){
        System.out.println(String.format("%-30s %-20s", prompt, " size = " + x));
    }
    
    public static void print(String prompt, List<String> x){
        System.out.println(String.format("%-30s %-20s", prompt, " sublist = " + x));
    }
}
