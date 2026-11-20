for t in range(10):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    result = 0
    for i in range(N):
        col = ""
        for j in range(N):
            if arr[j][i] != "0":
                col += arr[j][i]
        result += col.count("12")
    print(f"#{t + 1} {result}")