arr = list(map(int, input().split()))

arr.sort()

A, B = arr

gap = B - A

if gap == 0:
    print(0)
else:
    print(gap - 1)

for i in range(A + 1, B):
    print(i, end = " ")