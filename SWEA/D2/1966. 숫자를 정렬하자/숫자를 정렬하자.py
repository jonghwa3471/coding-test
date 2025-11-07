T = int(input())

for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(f"#{t + 1}", *nums)