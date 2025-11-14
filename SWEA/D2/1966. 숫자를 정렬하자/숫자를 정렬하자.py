T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"#{t + 1}", *arr)