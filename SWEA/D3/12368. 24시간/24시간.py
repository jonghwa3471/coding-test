T = int(input())

for t in range(T):
    h1, h2 = map(int, input().split())
    result = (h1 + h2) % 24
    print(f"#{t + 1} {result}")