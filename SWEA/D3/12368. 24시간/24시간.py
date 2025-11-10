T = int(input())

for t in range(T):
    A, B = map(int, input().split())
    result = (A + B) % 24
    print(f"#{t + 1} {result}")