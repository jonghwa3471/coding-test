import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
            String X = br.readLine();
            HashSet<Character> unique = new HashSet<>();

            for (int i = 0; i < X.length(); i++) {
                unique.add(X.charAt(i));
            }

            int result = unique.size();
            System.out.println("#" + t + " " + result);
        }
    }
}