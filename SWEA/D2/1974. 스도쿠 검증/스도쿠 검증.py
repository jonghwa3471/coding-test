T = int(input())

for t in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    
    for i in range(9):
        if len(set(arr[i])) != 9:
            result = 0
            break
    if result:
        for i in range(9):
            cols = []
            for j in range(9):
                cols.append(arr[j][i])
            if len(set(cols)) != 9:
                result = 0
                break
                
    if result:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid = []
                for k in range(i, i + 3):
                    grid.extend(arr[k][j : j + 3])
                if len(set(grid)) != 9:
                    result = 0
                    break
                    
    print(f"#{t + 1} {result}")