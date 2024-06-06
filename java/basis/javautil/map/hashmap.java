import java.util.*;

public class hashmap{
    public static void main(String[] args){
        /* initialization */
        Character[] letters = {'a', 'b', 'c', 'd', 'e'};
        Integer[] nums = {1, 2, 3, 4, 5};
        HashMap<Character, Integer> alpha2num = new HashMap<>();

        for (int i = 0; i < letters.length; i++){
            alpha2num.put(letters[i], nums[i]);
        }
        print("map:", alpha2num);

        /* get */
        print("get c:", alpha2num.get('c'));
        print("get r:", alpha2num.get('r'));

        /* getOrDefault */
        print("get or default c:", alpha2num.getOrDefault('c', 10));
        print("get or default r:", alpha2num.getOrDefault('r', 10));

        /* containsKey */
        print("contains b:", alpha2num.containsKey('b'));

        /* remove */
        print("remove d:", alpha2num.remove('d'));
        print("remove r:", alpha2num.remove('r'));
        print("current map:", alpha2num);

        /* keySet */
        print("key set:", alpha2num.keySet());

        /* values */
        print("values:", alpha2num.values());

        /* entrySet */
        printEntry("k-v pairs:", alpha2num.entrySet());

        /* forEach */
        for (Character key: alpha2num.keySet()) System.out.print(key + " ");
        System.out.println("");
        for (Integer value: alpha2num.values()) System.out.print(value + " ");
        System.out.println("");
        for (Map.Entry<Character, Integer> entry: alpha2num.entrySet()) System.out.print("(" + entry + " " + entry.getKey() + " " + entry.getValue() + ") ");
    }

    public static void print(String prompt, HashMap<Character, Integer> map){
        System.out.println(String.format("%-20s %-20s", prompt, map));
    }

    public static void print(String prompt, Integer num){
        System.out.println(String.format("%-20s %-20s", prompt, num));
    }

    public static void print(String prompt, boolean flag){
        System.out.println(String.format("%-20s %-20s", prompt, flag));
    }

    public static void print(String prompt, Set<Character> keys){
        System.out.println(String.format("%-20s %-20s", prompt, keys));
    }

    public static void print(String prompt, Collection<Integer> values){
        System.out.println(String.format("%-20s %-20s", prompt, values));
    }

    public static void printEntry(String prompt, Set<Map.Entry<Character, Integer>> entry){
        System.out.println(String.format("%-20s %-20s", prompt, entry));
    }
}