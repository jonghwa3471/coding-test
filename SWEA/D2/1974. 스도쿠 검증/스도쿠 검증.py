T = int(input())

for t in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        row = set()
        row.update(arr[i])
        if len(row) != 9:
            result = 0
            break
    
    if result:
        for i in range(9):
            col = set()
            for j in range(9):
                col.add(arr[j][i])
            if len(col) != 9:
                result = 0
                break
   
    if result:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid = set()
                for k in range(i, i + 3):
                    grid.update(arr[k][j : j + 3])
                if len(grid) != 9:
                    result = 0
                    break
            if not result:
                break
    print(f"#{t + 1} {result}")