T = int(input())

for t in range(T):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    B = Q
    if W <= R :
        B = Q
    else:
        B = Q + (W - R) * S
    if A <= B:
        print(f"#{t + 1} {A}")
    else:
        print(f"#{t + 1} {B}")