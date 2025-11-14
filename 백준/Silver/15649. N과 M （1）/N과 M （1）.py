N, M = map(int, input().split())

arr = [False] * (N + 1)
result = []

def dfs():
    if len(result) == M:
        print(*result)
    for i in range(1, N + 1):
        if not arr[i]:
            arr[i] = True
            result.append(i)
            dfs()
            result.pop()
            arr[i] = False
dfs()