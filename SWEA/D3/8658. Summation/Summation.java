import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine().trim());

        for (int t = 1; t <= T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            ArrayList<Integer> arr = new ArrayList<>();

            while (st.hasMoreTokens()) {
                arr.add(Integer.parseInt(st.nextToken()));
            }

            ArrayList<Integer> result = new ArrayList<>();

            for (int num : arr) {
                String s = String.valueOf(num);
                int sum = 0;
                for (int i = 0; i < s.length(); i++) {
                    // 문자 '0'을 빼서 실제 숫자값으로 변환
                    sum += s.charAt(i) - '0';
                }
                result.add(sum);
            }

            int maxVal = Integer.MIN_VALUE;
            int minVal = Integer.MAX_VALUE;

            for (int v : result) {
                if (v > maxVal) maxVal = v;
                if (v < minVal) minVal = v;
            }

            System.out.println("#" + t + " " + maxVal + " " + minVal);
        }
    }
}