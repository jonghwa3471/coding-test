T = int(input())

for t in range(T):
    arr = [list(map(int, input().split())) for _ in range(4)]
    numbers = set()
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(r, c, depth, path):
        if depth == 6:
            numbers.add(path)
            return
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 4 and 0 <= nc < 4:
                dfs(nr, nc, depth + 1, path + str(arr[nr][nc]))
    
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, str(arr[i][j]))
    result = len(numbers)
    print(f"#{t + 1} {result}")