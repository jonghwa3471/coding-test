T = int(input())

for t in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    arr.pop(0)
    arr.pop()
    avg = round(sum(arr) / len(arr))
    print(f"#{t + 1} {avg}")