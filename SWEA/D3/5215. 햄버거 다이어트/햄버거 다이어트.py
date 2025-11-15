T = int(input())

for t in range(T):
    N, L = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    result = 0
    
    def dfs(index, cur_score, cur_cal):
        global result
        if cur_cal > L:
            return
        if index == N:
            if cur_score > result:
                result = cur_score
            return
        score, cal = arr[index]
        dfs(index + 1, cur_score + score, cur_cal + cal)
        dfs(index + 1, cur_score, cur_cal)
        
    dfs(0, 0, 0)
    print(f"#{t + 1} {result}")