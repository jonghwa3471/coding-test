T = int(input())

for t in range(T):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    B = Q
    if W > R:
        B = S * (W - R) + Q
    result = A if A < B else B
    print(f"#{t + 1} {result}")