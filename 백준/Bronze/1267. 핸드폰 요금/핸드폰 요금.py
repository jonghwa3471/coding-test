N = int(input())
arr = list(map(int, input().split()))

Y_total = 0
M_total = 0

for cost in arr:
    Y_cost = 10
    Y_cost += cost // 30 * 10
    Y_total += Y_cost
    
    M_cost = 15
    M_cost += cost // 60 * 15
    M_total += M_cost
    
if Y_total > M_total:
    print("M", M_total)
elif Y_total < M_total:
    print("Y", Y_total)
else:
    print("Y", "M", Y_total)
