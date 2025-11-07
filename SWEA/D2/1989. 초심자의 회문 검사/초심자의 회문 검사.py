T = int(input())

for t in range(T):
    s = input()
    if s == s[::-1]:
        print(f"#{t + 1} 1")
    else:
        print(f"#{t + 1} 0")