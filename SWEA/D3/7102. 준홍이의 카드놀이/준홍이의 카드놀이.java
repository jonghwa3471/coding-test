import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Collections;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine().trim());

        for (int t = 1; t <= T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            // 둘 중 큰 값을 N, 작은 값을 M
            if (N < M) {
                int tmp = N;
                N = M;
                M = tmp;
            }

            int[] arr = new int[N + M + 1]; 
            // 합의 최대값은 N+M 이므로 배열 크기는 N+M+1이어야 함

            // 경우의 수 채우기
            for (int n = 1; n <= N; n++) {
                for (int m = 1; m <= M; m++) {
                    arr[n + m]++;
                }
            }

            // 최댓값 찾기
            int maxVal = 0;
            for (int v : arr) {
                if (v > maxVal) maxVal = v;
            }

            // 최댓값을 가진 index(= 가능한 합) 수집
            ArrayList<Integer> result = new ArrayList<>();
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] == maxVal) {
                    result.add(i);
                }
            }

            Collections.sort(result);

            // 출력
            System.out.print("#" + t);
            for (int r : result) {
                System.out.print(" " + r);
            }
            System.out.println();
        }
    }
}