import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine().trim());

        for (int t = 1; t <= T; t++) {
            int K = Integer.parseInt(br.readLine().trim());
            StringTokenizer st = new StringTokenizer(br.readLine());

            ArrayList<Integer> arr = new ArrayList<>();
            while (st.hasMoreTokens()) {
                arr.add(Integer.parseInt(st.nextToken()));
            }

            int result = 0;

            // while len(arr) > 1:
            while (arr.size() > 1) {
                ArrayList<Integer> next = new ArrayList<>();

                // for i in range(0, len(arr), 2):
                for (int i = 0; i < arr.size(); i += 2) {
                    int first = arr.get(i);
                    int second = arr.get(i + 1);
                    int gap = Math.abs(first - second);
                    result += gap;
                    next.add(Math.max(first, second));
                }

                arr = next;
            }

            System.out.println("#" + t + " " + result);
        }
    }
}