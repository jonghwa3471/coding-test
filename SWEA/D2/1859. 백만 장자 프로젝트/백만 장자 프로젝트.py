T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_ = 0
    result = 0
    for i in arr[::-1]:
        if i >= max_:
            max_ = i
        else:
            result +=  max_ - i
    print(f"#{t + 1} {result}")