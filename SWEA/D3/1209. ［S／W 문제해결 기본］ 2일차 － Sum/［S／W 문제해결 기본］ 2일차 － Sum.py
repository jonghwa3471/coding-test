for t in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = [0, 0, 0]
    for i in range(100):
        if sum(arr[i]) > result[0]:
            result[0] = sum(arr[i])
    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += arr[j][i]
        if col_sum > result[1]:
            result[1] = col_sum
    diagonal_sum = 0
    for i in range(100):
        diagonal_sum += arr[i][i]
        if result[2] < diagonal_sum:
            result[2] = diagonal_sum
    result.sort(reverse = True)
    print(f"#{t + 1}", result[0])
        