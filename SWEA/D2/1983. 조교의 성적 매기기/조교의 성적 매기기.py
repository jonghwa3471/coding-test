T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    scores = []
    for i in range(1, N + 1):
        mid, fin, hm = map(int, input().split())
        total = mid * 0.35 + fin * 0.45 + hm * 0.2
        scores.append((i, total))
    scores.sort(key = lambda x: x[1], reverse = True)
    rank_of = {sid: rank for rank, (sid, _) in enumerate(scores)}
    group = N // 10
    r = rank_of[K]
    result = grades[r // group]
    print(f"#{t + 1} {result}")