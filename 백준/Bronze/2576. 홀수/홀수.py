arr = []
odd = []
sum_ = 0;

for _ in range(7):
    arr.append(int(input()))
    
def odd_exists(arr):
    global odd
    odd = [x for x in arr if x % 2 == 1]
    if len(odd) == 0:
        return False
    else:
        return True

if odd_exists(arr):
    for a in odd:
        sum_ += a
    print(sum_)
    print(min(odd))
else:
    print(-1)