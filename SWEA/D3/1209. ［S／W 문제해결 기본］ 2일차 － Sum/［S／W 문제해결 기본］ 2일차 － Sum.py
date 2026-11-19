for t in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    row_max = 0
    col_max = 0
    cross_max = 0
    for row in arr:
        if sum(row) > row_max:
            row_max = sum(row)
    
    for i in range(100):
        cols = 0
        for j in range(100):
            cols += arr[j][i]
        if cols > col_max:
            col_max = cols
            
    cross1 = 0        
    for i in range(100):
        cross1 += arr[i][i]
        
    cross2 = 0
    for i in range(100):
        cross2 += arr[99 - i][99 - i]
        
    cross_max = max(cross1, cross2)
    result = max(row_max, col_max, cross_max)
    print(f"#{N} {result}")