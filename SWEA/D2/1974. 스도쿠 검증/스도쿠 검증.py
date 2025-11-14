T = int(input())

for t in range(T):
    ok = True
    arr = [list(map(int, input().split())) for _ in range(9)]
    
    for i in range(9):
        if len(set(arr[i])) != 9:
            ok = False
            break
    if ok:
        for i in range(9):
            col = set()
            for j in range(9):
                col.add(arr[j][i])
            if len(col) != 9:
                ok = False
                break
            if not ok:
                break
    if ok:
        for i in range(0, 9, 3):
            for j in range(0, 9 , 3):
                grid = set()
                for k in range(i, i + 3):
                    grid.update(arr[k][j : j + 3])
                if len(grid) != 9:
                    ok = False
                    break
            if not ok:
                break
    if ok:
        print(f"#{t + 1} 1")
    else:
        print(f"#{t + 1} 0")