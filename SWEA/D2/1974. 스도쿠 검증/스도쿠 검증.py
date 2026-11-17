T = int(input())

for t in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    row = True
    col = True
    grid = True
    result = 0
    for i in range(9):
        check_exists = []
        for j in range(9):
            if not arr[i][j] in check_exists:
                check_exists.append(arr[i][j])
        if not len(check_exists) == 9:
            row = False
            
    for i in range(9):
        check_exists = []
        for j in range(9):
            if not arr[j][i] in check_exists:
                check_exists.append(arr[j][i])
        if not len(check_exists) == 9:
            col = False
            
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check_exists = []
            for k in range(i, i + 3):
                grid_row = arr[k][j:j+3]
                for num in grid_row:
                    if not num in check_exists:
                        check_exists.append(num)
            if not len(check_exists) == 9:
                grid = False
    if row and col and grid:
        result = 1
    else:
        result = 0
    print(f"#{t + 1} {result}")