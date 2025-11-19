T = int(input())

for t in range(T):
    scores = list(map(int, input().split()))
    need_study = list(map(lambda x: 40 if x < 40 else x, scores))
    result = sum(need_study) // 5
    print(f"#{t + 1} {result}")