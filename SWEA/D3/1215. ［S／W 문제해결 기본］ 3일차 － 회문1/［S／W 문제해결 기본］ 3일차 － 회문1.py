for t in range(10):
    N = int(input())
    arr = [input() for _ in range(8)]
    result = 0
    for i in range(8):
        for j in range(8 - N + 1):
            word = arr[i][j : j + N]
            if word == word[::-1]:
                result += 1
    for i in range(8):
        for j in range(8 - N + 1):
            word = ""
            for k in range(N):
                word += arr[j + k][i]
            if word == word[::-1]:
                result += 1
    print(f"#{t + 1} {result}")