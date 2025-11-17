from collections import deque

for t in range(10):
    N = int(input())
    arr = deque(list(map(int, input().split())))
    while True:
        for i in range(1, 6):
            pop = arr.popleft()
            pop -= i
            if pop <= 0:
                arr.append(0)
                print(f"#{N}", *arr)
                break
            else:
                arr.append(pop)
        else:
            continue
        break