for t in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        col = []
        for j in range(N):
            if arr[j][i] != 0:
                col.append(arr[j][i])
        prev = 0
        for c in col:
            if prev == 1 and c == 2:
                result += 1
            prev = c
    print(f"#{t + 1} {result}")