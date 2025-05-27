import java.util.*;
public class Day36_sol
{
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        System.out.print("Input: ");

        String[] sentence = sc.nextLine().toLowerCase().split(" ");

        Map<String, Integer> map= new HashMap<>();
        for (String word : sentence)
        {
            map.put(word, map.getOrDefault(word,0)+1);
        }

        for (String key : map.keySet()) {
            System.out.println(key + ": " + map.get(key));
        }

    }
}