T = int(input())

for t in range(T):
    avg = round(sum(map(int, input().split())) / 10)
    print(f"#{t + 1} {avg}")