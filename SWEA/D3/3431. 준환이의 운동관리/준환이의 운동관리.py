T = int(input())

for t in range(T):
    L, U, X = map(int, input().split())
    if U < X:
        print(f"#{t + 1} -1")
    elif L <= X <= U:
        print(f"#{t + 1} 0")
    else:
        print(f"#{t + 1} {L - X}")