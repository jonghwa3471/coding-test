from collections import deque

T = int(input())
D = deque([])

def deque_fn(script):
    S = script.split()
    if S[0] == "push_front":
        D.appendleft(S[1])
    elif S[0] == "push_back":
        D.append(S[1])
    elif S[0] == "pop_front":
        if len(D) == 0:
            print(-1)
        else:
            print(D.popleft())
    elif S[0] == "pop_back":
        if len(D) == 0:
            print(-1)
        else:
            print(D.pop())
    elif S[0] == "size":
        print(len(D))
    elif S[0] == "empty":
        print(1 if len(D) == 0 else 0)
    elif S[0] == "front":
        if len(D) == 0:
            print(-1)
        else:
            print(D[0])
    elif S[0] == "back":
        if len(D) == 0:
            print(-1)
        else:
            print(D[-1])
            
for t in range(T):
    script = input()
    deque_fn(script)