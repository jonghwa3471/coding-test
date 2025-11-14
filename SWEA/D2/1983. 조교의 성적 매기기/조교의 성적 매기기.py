T = int(input())

for t in range(T):
    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    score = []
    for i in range(N):
        mid, fin, hm = arr[i]
        total = mid * 0.35 + fin * 0.45 + hm * 0.2
        score.append((i + 1, total))
    score.sort(lambda x: x[1], reverse = True)
    rank_of = {num: rank for rank, (num, _) in enumerate(score)}
    group = N // 10
    r = rank_of[K]
    result = grade[r // group]
    print(f"#{t + 1} {result}")