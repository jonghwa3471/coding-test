T = int(input())

for t in range(T):
    N = int(input())
    arr = [2, 3, 5, 7, 11]
    result = [0, 0, 0, 0, 0]
    for i in range(len(arr)):
        while N % arr[i] == 0:
            N //= arr[i]
            result[i] += 1
    print(f"#{t + 1}", *result)