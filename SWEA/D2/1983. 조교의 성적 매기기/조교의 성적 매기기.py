T = int(input())

for t in range(T):
    grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    N, K = map(int, input().split())
    scores = []
    for i in range(1, N + 1):
        mid, fin, hw = map(int, input().split())
        total = 0.35 * mid + 0.45 * fin + 0.20 * hw
        scores.append((i, total))
    scores.sort(key = lambda item: item[1], reverse = True)
    rank_of = {sid: rank for rank, (sid, _) in enumerate(scores)}
    group = N // 10
    r = rank_of[K]
    result = grades[r // group]
    print(f"#{t + 1} {result}")