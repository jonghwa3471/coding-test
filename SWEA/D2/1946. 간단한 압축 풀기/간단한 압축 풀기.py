T = int(input())

for t in range(T):
    N = int(input())
    arr = ""
    for i in range(N):
        ch, n = input().split()
        arr += ch * int(n)
    print(f"#{t + 1}")
    for i in range(0, len(arr), 10):
        if len(arr[i : i + 10]) != 10:
            line = "".join(arr[i : len(arr)])
            print(line)
        else:
            line = "".join(arr[i : i + 10])
            print(line)