import java.util.*;

public class treemap {
    public static void main(String[] args){
        /* initialization */
        Character[] letters = {'a', 'd', 'e', 'c', 'b', 'g', 'f'};
        Integer[] nums = {3, 4, 2, 1, 5, 7, 6};
        TreeMap<Character, Integer> map1 = new TreeMap<>();

        for (int i = 0; i < letters.length; i++) map1.put(letters[i], nums[i]);
        print("treemap:", map1);
        TreeMap<Character, Integer> map2 = new TreeMap<>(Comparator.comparing(map1::get));
        map2.putAll(map1);
        print("sort by value:",  map2);

        /* firstKey & lastKey */
        print("map1 first:", map1.firstKey());
        print("map1 last:", map1.lastKey());

        /* higherKey & ceilingKey */
        print("higher key c:", map1.higherKey('c'));
        print("ceiling key c:", map1.ceilingKey('c'));

        /* lowerKey & floorKey() */
        print("lower key b:", map1.lowerKey('b'));
        print("flooring key b:", map1.floorKey('b'));

        /* poll */
        print("poll first:", map1.pollFirstEntry());
        print("poll last", map1.pollLastEntry());
        print("current treemap:", map1);

        /* headMap */
        print("head c:", map1.headMap('c', true));

        /* tailMap */
        print("tail c:", map1.tailMap('c', false));

        /* subMap */
        print("sub b to e:", map1.subMap('b', false, 'e', true));
    }
    
    public static void print(String prompt, TreeMap<Character, Integer> map){
        System.out.println(String.format("%-25s %-25s", prompt, map));
    }

    public static void print(String prompt, Character key){
        System.out.println(String.format("%-25s %-25s", prompt, key));
    }

    public static void print(String prompt, Map.Entry<Character, Integer> entry){
        System.out.println(String.format("%-25s %-25s", prompt, entry));
    }

    public static void print(String prompt, NavigableMap<Character, Integer> map){
        System.out.println(String.format("%-25s %-25s", prompt, map));
    }
}
