T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    def dfs(index, cur_sum):
        global result
        if cur_sum > K:
            return
        if index == N:
            if cur_sum == K:
                result += 1
            return
        dfs(index + 1, cur_sum)
        dfs(index + 1, cur_sum + arr[index])
    dfs(0, 0)
    print(f"#{t + 1} {result}")