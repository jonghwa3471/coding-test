T = int(input())

for t in range(T):
    N, L = map(int, input().split())
    arr = []
    result = 0
    for n in range(N):
        T, K = map(int, input().split())
        arr.append((T, K))
        
    def dfs(index, cur_taste, cur_cal):
        global result
        if cur_cal > L:
            return
        if index == N:
            if cur_taste > result:
                result = cur_taste
            return
        taste, cal = arr[index]
        dfs(index + 1, cur_taste + taste, cur_cal + cal)
        dfs(index + 1, cur_taste, cur_cal)
        
    dfs(0, 0, 0)
    print(f"#{t + 1} {result}")