N, M = map(int, input().split())

result = []

def dfs(start):
    if len(result) == M:
        print(*result)
    for i in range(start, N + 1):
        result.append(i)
        dfs(i + 1)
        result.pop()
        
dfs(1)