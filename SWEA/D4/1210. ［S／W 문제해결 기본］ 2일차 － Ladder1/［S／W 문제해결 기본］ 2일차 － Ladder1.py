for t in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    r = 99
    c = 0
    for j in range(100):
        if arr[r][j] == 2:
            c = j
            break
            
    while r > 0:
        arr[r][c] = 0
        if c - 1 >= 0 and arr[r][c - 1] == 1:
            while c - 1 >=0 and arr[r][c - 1] == 1:
                c -= 1
                arr[r][c] = 0
        elif c + 1 < 100 and arr[r][c + 1] == 1:
            while c + 1 < 100 and arr[r][c + 1] == 1:
                c += 1
                arr[r][c] = 0
        else:
            r -= 1
    print(f"#{t + 1} {c}")