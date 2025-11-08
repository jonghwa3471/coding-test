T = int(input())

for t in range(T):
    h1, s1, h2, s2 = map(int, input().split())
    h = h1 + h2
    s = s1 + s2
    if h > 12:
        h -= 12
    if s > 60:
        s -= 60
        h += 1
    print(f"#{t + 1} {h} {s}")