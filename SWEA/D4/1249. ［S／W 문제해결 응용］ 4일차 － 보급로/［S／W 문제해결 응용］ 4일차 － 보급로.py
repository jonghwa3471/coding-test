import heapq

T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    inf = float("inf")
    dist = [[inf] * N for _ in range(N)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]
    while pq:
        cur_cost, r, c = heapq.heappop(pq)
        if cur_cost > dist[r][c]:
            continue
        if r == N - 1 and c == N - 1:
            break
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                next_cost = cur_cost + arr[nr][nc]
                if next_cost < dist[nr][nc]:
                    dist[nr][nc] = next_cost
                    heapq.heappush(pq, (next_cost, nr, nc))
    print(f"#{t + 1} {dist[N - 1][N - 1]}")