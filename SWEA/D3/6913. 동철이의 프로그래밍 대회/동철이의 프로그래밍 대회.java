import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine().trim());

        for (int t = 1; t <= T; t++) {

            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int[] scores = new int[N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int sum = 0;
                for (int j = 0; j < M; j++) {
                    sum += Integer.parseInt(st.nextToken());
                }
                scores[i] = sum;
            }

            // 최대 점수 찾기
            int maxScore = Integer.MIN_VALUE;
            for (int s : scores) {
                if (s > maxScore) {
                    maxScore = s;
                }
            }

            // 최대 점수를 받은 사람 수 카운트
            int count = 0;
            for (int s : scores) {
                if (s == maxScore) count++;
            }

            System.out.println("#" + t + " " + count + " " + maxScore);
        }
    }
}