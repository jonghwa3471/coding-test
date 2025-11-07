T = int(input())

for t in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        ch, n = input().split()
        arr.append(ch * int(n))
    s = "".join(arr)
    print(f"#{t + 1}")
    for i in range(0, len(s), 10):
        result = s[i : i + 10]
        print(result)