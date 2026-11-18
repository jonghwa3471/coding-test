T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    ordered_scores = []
    for i in range(1, N + 1):
        scores = list(map(int, input().split()))
        total = scores[0] * 0.35 + scores[1] * 0.45 + scores[2] * 0.2
        ordered_scores.append(total)
    target = ordered_scores[K - 1]
    ordered_scores.sort(reverse=True)
    rank = ordered_scores.index(target)
    result = grade[rank // (N //10)]
    print(f"#{t + 1} {result}")