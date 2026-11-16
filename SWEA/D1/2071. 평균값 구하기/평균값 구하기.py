T = int(input())

for t in range(T):
    avg = int(sum(map(int, input().split())) / 10 + 0.5)
    print(f"#{t + 1} {avg}")