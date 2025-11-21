from collections import deque

for t in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(16)]
    sr = sc = -1
    for i in range(16):
        for j in range(16):
            if arr[i][j] == "2":
                sr, sc = i, j
                break
        if sr != -1:
            break
            
    q = deque()
    q.append((sr, sc))
    visited = [[False] * 16 for _ in range(16)]
    visited[sr][sc] = True
    
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = 0
    
    while q:
        r, c = q.popleft()
        if arr[r][c] == "3":
            answer = 1
            break
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 16 and 0 <= nc < 16:
                if not visited[nr][nc] and arr[nr][nc] != "1":
                    visited[nr][nc] = True
                    q.append((nr, nc))
                
    print(f"#{t + 1} {answer}")