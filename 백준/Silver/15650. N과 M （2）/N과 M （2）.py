N, M = map(int, input().split())

result = []

def dfs(start: int) -> None:
    if len(result) == M:
        print(*result)
        return
    for i in range(start, N + 1):
        result.append(i)
        dfs(i + 1)
        result.pop()

dfs(1)
        
    