T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    count  = [0] * (len(arr) + 1)
    for number in arr:
        count[number] += 1
    max_num = max(count)
    indexs = [idx for idx, value in enumerate(count) if value == max_num]
    result = max(indexs)
    print(f"#{i + 1} {result}")