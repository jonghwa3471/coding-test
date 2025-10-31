T = int(input())

for t in range(T):
    ok = 1
    arr = [list(map(int, input().split())) for _ in range(9)]
    
    for i in range(9):
        if not len(set(arr[i])) == 9:
            ok = 0
            break
            
    if ok:
        for i in range(9):
            nums = []
            for j in range(9):
                nums.append(arr[j][i])
            if not len(set(nums)) == 9:
                    ok = 0
                    break
                    
    if ok:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = []
                for k in range(i, i + 3):
                    nums.extend(arr[k][j : j + 3])
                if not len(set(nums)) == 9:
                                ok = 0
                                break
            if not ok:
                break
    print(f"#{t + 1} {ok}")