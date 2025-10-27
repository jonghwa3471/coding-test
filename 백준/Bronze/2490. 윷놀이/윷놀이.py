one = list(map(int, input().split()))
two = list(map(int, input().split()))
three = list(map(int, input().split()))
    
def check_zero(arr):
    zero_count = arr.count(0)
    if zero_count == 1:
        print("A")
    elif zero_count == 2:
        print("B")
    elif zero_count == 3:
        print("C")
    elif zero_count == 4:
        print("D")
    else:
        print("E")
        
check_zero(one)
check_zero(two)
check_zero(three)