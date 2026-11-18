T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    ordered_scores = []
    for i in range(1, N + 1):
        scores = list(map(int, input().split()))
        total = scores[0] * 0.35 + scores[1] * 0.45 + scores[2] * 0.2
        ordered_scores.append((i, total))
    ordered_scores.sort(key=lambda x: x[1], reverse=True)
    rank_of = {index: rank for rank, (index, _) in enumerate(ordered_scores)}
    result = grade[rank_of[K] // (N // 10)]
    print(f"#{t + 1} {result}")